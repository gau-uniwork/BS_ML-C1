import logging
import requests
from ..models import Image
from .base import Scraper

logger = logging.getLogger("root")

search_url = (
    "https://www.pexels.com/en-us/api/v3/search/photos?query={query}"
    + "&page={page}&per_page=24""&orientation=all&size=all&color=all&sort=popular&seo_tags=true"
)


class PexelsScraper(Scraper):
    name = "Pexels"

    def get_image_urls(self, page: int, query: str) -> list[Image]:
        response = requests.get(
            search_url.format(page=page, query=query),
            headers={
                "secret-key": "H2jk9uKnhRmL6WPwh89zBezWvr",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0"
            }
        )
        images = []
        for image in response.json()["data"]:
            images.append(
                Image(
                    url=image["attributes"]["image"]["small"],
                    slug=image["attributes"]["slug"],
                    emotion=query.split()[0]
                )
            )
        return images

    def get_all_images(self) -> list[Image]:
        images = []
        total_pages = 50
        for idx, query in enumerate(self.queries):
            logging.info(f"Query: {query}; {idx + 1} - {len(self.queries)}...")
            for page in range(1, total_pages + 1):
                logging.info(f"\tScraping page: {page} - {total_pages}")
                images.extend(self.get_image_urls(page, query))
        return images

    def run(self):
        image_urls = self.get_all_images()
        self.download_images(image_urls)


if __name__ == "__main__":
    PexelsScraper().run()
