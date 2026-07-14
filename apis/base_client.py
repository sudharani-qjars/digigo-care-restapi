"""
base_client.py

Simple HTTP client for API automation.
"""

import requests


class BaseClient:
    """
    Base HTTP Client
    """

    def __init__(self, base_url: str):
        """
        Initialize the client.

        Args:
            base_url (str): Base URL of the API.
        """
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint: str, params=None, headers=None):
        """
        Send GET request.
        """
        return self.session.get(
            url=f"{self.base_url}{endpoint}",
            params=params,
            headers=headers
        )

    def post(self, endpoint: str, json=None, data=None, headers=None):
        """
        Send POST request.
        """
        return self.session.post(
            url=f"{self.base_url}{endpoint}",
            json=json,
            data=data,
            headers=headers
        )

    def put(self, endpoint: str, json=None, headers=None):
        """
        Send PUT request.
        """
        return self.session.put(
            url=f"{self.base_url}{endpoint}",
            json=json,
            headers=headers
        )

    def patch(self, endpoint: str, json=None, headers=None):
        """
        Send PATCH request.
        """
        return self.session.patch(
            url=f"{self.base_url}{endpoint}",
            json=json,
            headers=headers
        )

    def delete(self, endpoint: str, headers=None):
        """
        Send DELETE request.
        """
        return self.session.delete(
            url=f"{self.base_url}{endpoint}",
            headers=headers
        )

    def close(self):
        """
        Close the HTTP session.
        """
        self.session.close()