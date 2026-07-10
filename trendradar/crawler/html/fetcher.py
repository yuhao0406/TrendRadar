"""
HTML crawler fetcher.

Fetch HTML pages for websites without RSS.
"""

import requests


class HTMLFetcher:
    """
    Basic HTML page fetcher.
    """

    def __init__(self, timeout=15):
        self.timeout = timeout

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "Chrome/120 Safari/537.36"
            )
        }

    def fetch(self, url: str) -> str:
        """
        Fetch webpage HTML.

        Args:
            url: webpage URL

        Returns:
            HTML text
        """

        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout
            )

            response.raise_for_status()

            response.encoding = response.apparent_encoding

            return response.text

        except Exception as e:
            raise RuntimeError(
                f"HTML fetch failed: {url}, error: {e}"
            )
