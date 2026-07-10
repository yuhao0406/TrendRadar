"""
HTML crawler parser.

Parse title, link and time from HTML pages.
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin


class HTMLParser:
    """
    Generic HTML parser.
    """

    def __init__(
        self,
        list_selector: str,
        title_selector: str = None,
        link_selector: str = None,
        time_selector: str = None,
    ):
        self.list_selector = list_selector
        self.title_selector = title_selector
        self.link_selector = link_selector
        self.time_selector = time_selector


    def parse(self, html: str, base_url: str):
        """
        Parse HTML.

        Returns:
            [
                {
                    title:"",
                    url:"",
                    time:""
                }
            ]
        """

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        results = []

        items = soup.select(
            self.list_selector
        )

        for item in items:

            # title
            if self.title_selector:
                title_node = item.select_one(
                    self.title_selector
                )
            else:
                title_node = item

            if not title_node:
                continue

            title = title_node.get_text(
                strip=True
            )

            if not title:
                continue


            # link
            if self.link_selector:
                link_node = item.select_one(
                    self.link_selector
                )
            else:
                link_node = item.find("a")


            url = ""

            if link_node:
                url = link_node.get("href", "")

                if url:
                    url = urljoin(
                        base_url,
                        url
                    )


            # time
            time = ""

            if self.time_selector:
                time_node = item.select_one(
                    self.time_selector
                )

                if time_node:
                    time = time_node.get_text(
                        strip=True
                    )


            results.append(
                {
                    "title": title,
                    "url": url,
                    "time": time
                }
            )


        return results
