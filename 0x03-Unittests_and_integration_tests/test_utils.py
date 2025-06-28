#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map
"""
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json, memoize
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the correct value"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({"a": 1}, ("a", "b")), ({}, ("a",))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test_get_json method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Patch requests.get to return the mock_response
        with patch('requests.get', return_value=mock_response) as mock_get:
            # Call the function under test
            result = get_json(test_url)

            # Ensure requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)

            # Ensure the result of get_json is test_payload
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches the result of a method"""

        class TestClass:
            """Test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            test_obj = TestClass()

            # Access the property twice (without calling)
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Should return correct result
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # a_method should only be called once due to caching
            mock_method.assert_called_once()
