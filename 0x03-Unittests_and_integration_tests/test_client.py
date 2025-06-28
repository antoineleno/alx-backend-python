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
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns correct repos_url"""

        expected_url = "https://api.github.com/orgs/google/repos"

        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            # Arrange: mock the .org property
            mock_org.return_value = {"repos_url": expected_url}

            # Act
            client = GithubOrgClient("google")
            result = client._public_repos_url

            # Assert
            self.assertEqual(result, expected_url)