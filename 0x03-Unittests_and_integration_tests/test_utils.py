#!/usr/bin/env python3
"""Module 'test_utils.py' to test functions in 'utils.py'"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test the 'access_nested_map' function"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple[str], expected: Union[Dict, int]
    ) -> None:
        """Tests 'access_nested_map' function from 'utils.py'"""
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Tuple[str], exception: Exception
    ) -> None:
        """Tests 'access_nested_map' exception function from 'utils.py'"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test the 'get_json' function"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url: str, payload: Dict) -> None:
        """Mocks and tests a request.get call"""
        data = {"json.return_value": payload}
        with patch("requests.get", return_value=Mock(**data)) as mock_get:
            self.assertEqual(get_json(url), payload)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test the 'memoize' decorator"""

    def test_memoize(self):
        """Mocks and testst the memoize decorator"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass,
            "a_method",
            return_value=lambda: 100
        ) as mock:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 100)
            self.assertEqual(test_class.a_property(), 100)
            mock.assert_called_once()
