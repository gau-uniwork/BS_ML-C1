from .scrapers.pexels_scraper import PexelsScraper
from .scrapers.unsplash_scraper import UnsplashScraper


class ScraperFactory:
    scrapers = [PexelsScraper(), UnsplashScraper()]

    def execute(self):
        for scraper in self.scrapers:
            scraper.run()


if __name__ == "__main__":
    ScraperFactory().execute()
