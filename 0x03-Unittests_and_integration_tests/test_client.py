#!/usr/bin/env python3
"""Module 'client.py' """
import unittest
from typing import Dict
from unittest.mock import MagicMock, patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org: str, response: Dict, mocked_fn: MagicMock) -> None:
        """Test that GithubOrgClient returns the correct value"""
        mocked_fn.return_value = lambda: response
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), response)
        mocked_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Test the _public_repos_url property"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mocked_fn: MagicMock) -> None:
        """
        Test that GithubOrgClient public_repos method returns correct value
        """
        payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                    "name": "episodes.dart",
                },
                {
                    "name": "dagger",
                },
            ],
        }
        mocked_fn.return_value = payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mocked:
            mocked.return_value = payload["repos_url"]
            print(GithubOrgClient("google").public_repos())
            self.assertEqual(
                GithubOrgClient("google")
                .public_repos(), ["episodes.dart", "dagger"]
            )
            mocked.assert_called_once()
        mocked_fn.assert_called_once()
