#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient.org
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""

        # Arrange
        expected = {"login": org_name, "id": 1234}
        mock_get_json.return_value = expected

        # Act
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns correct repos_url"""

        expected_url = "https://api.github.com/orgs/google/repos"

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            # Arrange: mock the .org property
            mock_org.return_value = {"repos_url": expected_url}

            # Act
            client = GithubOrgClient("google")
            result = client._public_repos_url

            # Assert
            self.assertEqual(result, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos returns expected repo names"""

        # Setup: fake payload from GitHub API
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # Set the mocked return value for get_json
        mock_get_json.return_value = test_payload

        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock) as mock_public_url:
            mock_public_url.return_value = "http://fake.url/repos"

            # Create client instance
            client = GithubOrgClient("google")

            # Call method under test
            result = client.public_repos()

            # Assert the repo names are returned
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Assert _public_repos_url and get_json were called exactly once
            mock_public_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://fake.url/repos")
