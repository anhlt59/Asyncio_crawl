# -*- coding: utf8 -*-
import asyncio
import logging
import re
import json
import sys
import urllib.error
import urllib.parse

import aiohttp
from aiohttp import ClientSession
from scrapy.selector import Selector
from pprint import pprint


assert sys.version_info >= (3, 7), "Script requires Python 3.7+."

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.WARNING,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

URLS = [
    "https://www.goodreads.com/quotes?page=1",
    "https://www.goodreads.com/quotes?page=2",
    "https://www.goodreads.com/quotes?page=3",
    "https://www.goodreads.com/quotes?page=4",
    "https://www.goodreads.com/quotes?page=5",
    "https://www.goodreads.com/quotes?page=6",
    "https://www.goodreads.com/quotes?page=7",
    "https://www.goodreads.com/quotes?page=8",
    "https://www.goodreads.com/quotes?page=9",
]


async def fetch_html(url, session, **kwargs):
    """ Request url to get html response."""
    resp = await session.request(method="GET", url=url, **kwargs)
    # raise exception if status is not 200
    resp.raise_for_status()
    logger.info(f"Got response [{resp.status}] for URL: {url}")
    html = await resp.text()
    return html


async def parse(url, session, **kwargs):
    """ Parse html (author, tags, text)."""
    crawled_data = list()

    try:
        html = await fetch_html(url=url, session=session, **kwargs)
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
    ) as e:
        logger.error(f"aiohttp exception {url} - [{e.status}]: {e.message}")
    except Exception as e:
        logger.exception(f"Non-aiohttp exception:  {repr(e)}")
    else:
        selector = Selector(text=html)
        for quote in selector.xpath(".//div[@class='quote']"):
            item = {
                'text': quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                'author': quote.xpath(".//span[@class='authorOrTitle']/text()").extract_first(),
                'tags': quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract(),
            }
            crawled_data.append(item)
        logger.info(f"Get {len(crawled_data)} item from {url}")
    pprint(crawled_data)
    # return crawled_data


async def async_crawl(urls, **kwargs):
    """ Crawl for multiple urls."""
    async with ClientSession() as session:
        tasks = [parse(url=url, session=session, **kwargs) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(async_crawl(urls=URLS))
