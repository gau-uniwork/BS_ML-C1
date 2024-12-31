import logging
from concurrent.futures import ThreadPoolExecutor

from .scrapers.base import Scraper
from .scrapers.pexels_scraper import PexelsScraper
from .scrapers.unsplash_scraper import UnsplashScraper

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ScraperFactory:
    scrapers: list[Scraper] = [UnsplashScraper(), PexelsScraper()]

    def execute(self):
        with ThreadPoolExecutor() as executor:
            tasks = [executor.submit(scraper.run) for scraper in self.scrapers]
            for task in tasks:
                task.result()


if __name__ == "__main__":
    ScraperFactory().execute()
