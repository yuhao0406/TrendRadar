# coding=utf-8
"""
爬虫模块 - 数据抓取功能

支持:
- NewsNow API
- HTML Source
"""

from trendradar.crawler.fetcher import DataFetcher
from trendradar.crawler.collector import Collector


__all__ = [
    "DataFetcher",
    "Collector",
]
