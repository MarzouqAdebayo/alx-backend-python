#!#!/usr/bin/env python3
""""""
import unittest
from typing import Dict
from unittest.mock import MagicMock, patch
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """"""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org: str, response: Dict, mocked_fn: MagicMock):
        mocked_fn.return_value = lambda: response
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), response)
        mocked_fn.assert_called_once_with("https://api.github.com/orgs/{}".format(org))
