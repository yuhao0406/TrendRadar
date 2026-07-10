"""
HTML crawler spider.

Combine fetcher and parser.
"""

from .fetcher import HTMLFetcher
from .parser import HTMLParser


class HTMLSpider:
    """
    Generic HTML spider.
    """

    def __init__(self, source_config):

        self.name = source_config.get(
            "name",
            ""
        )

        self.url = source_config.get(
            "url",
            ""
        )

        self.parser = HTMLParser(
            list_selector=source_config.get(
                "list_selector"
            ),
            title_selector=source_config.get(
                "title_selector"
            ),
            link_selector=source_config.get(
                "link_selector"
            ),
            time_selector=source_config.get(
                "time_selector"
            )
        )

        self.fetcher = HTMLFetcher()


    def crawl(self):
        """
        Crawl one website.

        Returns:
            list of news items
        """

        html = self.fetcher.fetch(
            self.url
        )


        items = self.parser.parse(
            html,
            self.url
        )


        results = []

        for item in items:

            results.append(
                {
                    "source": self.name,
                    "title": item.get(
                        "title",
                        ""
                    ),
                    "url": item.get(
                        "url",
                        ""
                    ),
                    "time": item.get(
                        "time",
                        ""
                    ),
                    "type": "html"
                }
            )


        return results
