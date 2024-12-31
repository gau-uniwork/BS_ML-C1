import os
import logging
from pathlib import Path
import requests
from abc import ABC, abstractmethod
from data_collection.models import Image

logger = logging.getLogger("root")

class Scraper(ABC):
    queries = ["happy person", "sad person"]
    output_path = Path(__file__).parent.parent.parent / "images"

    @abstractmethod
    def run(self) -> None:
        """main method to execute the scraper"""
        raise NotImplementedError

    @property
    def name(self):
        """The scraped website name"""
        raise NotImplementedError
    
    def create_output_dirs(self) -> None:
        """Creates image output labeled directories"""
        for query in self.queries:
            emotion = query.split()[0]
            os.makedirs(self.output_path / f"raw/{emotion}", exist_ok=True)
            os.makedirs(self.output_path / f"raw/{emotion}", exist_ok=True)


    def download_images(self, image_urls: list[Image]) -> None:
        self.create_output_dirs()
        for idx, image in enumerate(image_urls):
            logger.info(f"Downloading images: {idx + 1} - {len(image_urls)}")
            response = requests.get(image.url)
            with open(f"./images/raw/{image.emotion}/{image.slug}.png", "wb") as img:
                img.write(response.content)
