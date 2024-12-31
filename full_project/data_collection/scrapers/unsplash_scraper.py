import logging
import requests
from ..models import Image
from .base import Scraper


logger = logging.getLogger("root")

search_url = (
    "https://unsplash.com/napi/search/photos?page={page}&per_page=20"
    + "&plus=none&query={query}&xp=search-region-awareness:experiment"
)


class UnsplashScraper(Scraper):
    name = "Unsplash"

    def get_image_urls(self, page: int, query: str) -> list[Image]:
        url = search_url.format(page=page, query=query)
        response = requests.get(url)
        image_tags = response.json()["results"]
        image_urls = []
        for image in image_tags:
            image_url = image["urls"]["small"]
            slug = image["slug"]
            image_urls.append(Image(url=image_url, slug=slug, emotion=query.split()[0]))
        return image_urls

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
    UnsplashScraper().run()
