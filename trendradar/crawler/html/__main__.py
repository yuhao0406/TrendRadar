"""
HTML crawler entry point.
"""

from .spider import HTMLSpider


def run_html_source(source_config):
    """
    Run one HTML source.

    Args:
        source_config:
            website configuration

    Returns:
        news list
    """

    spider = HTMLSpider(
        source_config
    )

    return spider.crawl()
