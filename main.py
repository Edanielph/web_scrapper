import argparse
import logging
logging.basicConfig(level=logging.INFO)

import news_page_objects as news_page_objects
from common import config 

logger = logging.getLogger(__name__)

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info(f'Beginning scrape for {host}')
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage.article_links:
        print(links)