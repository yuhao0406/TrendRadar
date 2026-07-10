"""
HTML crawler runner.

Load config and run HTML sources.
"""

from .config import HTMLConfigLoader
from .__main__ import run_html_source


class HTMLCrawlerRunner:
    """
    Run multiple HTML sources.
    """

    def __init__(self, config_path):

        self.loader = HTMLConfigLoader(
            config_path
        )


    def run(self):

        sources = self.loader.load()

        results = []

        for source in sources:

            try:

                news = run_html_source(
                    source
                )

                results.extend(
                    news
                )

            except Exception as e:

                print(
                    f"HTML crawler failed: "
                    f"{source.get('name')}: {e}"
                )

        return results
