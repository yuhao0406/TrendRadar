# coding=utf-8
"""
统一数据采集器

整合:
- NewsNow API
- HTML crawler
"""

from typing import List, Dict

from trendradar.crawler.fetcher import DataFetcher
from trendradar.crawler.html.runner import HTMLCrawlerRunner


class Collector:
    """
    Unified crawler collector.
    """

    def __init__(
        self,
        html_config="config/html_sources.yaml"
    ):

        self.data_fetcher = DataFetcher()

        self.html_runner = HTMLCrawlerRunner(
            html_config
        )


    def collect_html(self) -> List[Dict]:
        """
        获取 HTML 新闻
        """

        return self.html_runner.run()


    def collect_newsnow(
        self,
        ids,
        domain_rules=None
    ):

        return self.data_fetcher.crawl_websites(
            ids,
            domain_rules=domain_rules
        )


    def collect_all(
        self,
        ids=None,
        domain_rules=None
    ):

        result = {
            "newsnow": None,
            "html": []
        }


        if ids:

            result["newsnow"] = self.collect_newsnow(
                ids,
                domain_rules
            )


        result["html"] = self.collect_html()


        return result
