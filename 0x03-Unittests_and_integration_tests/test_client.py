#!/usr/bin/env python3
"""Module 'client.py' """
import unittest
from typing import Dict
from unittest.mock import MagicMock, patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
            self.assertEqual(
                GithubOrgClient("google")
                .public_repos(), ["episodes.dart", "dagger"]
            )
            mocked.assert_called_once()
        mocked_fn.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Test that the has_license methods works properly"""
        org_client = GithubOrgClient("google")
        has_license = org_client.has_license(repo, key)
        self.assertEqual(has_license, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_payload': TEST_PAYLOAD[0][2],
        'apache2_payload': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for GithubOrgClient class"""
    @classmethod
    def setUpClass(cls) -> None:
        """Set up class before test runs"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test the public_repos method """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Test public_repos method with a license"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0")
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Remove the class fixtures after tests run"""
        cls.get_patcher.stop()
