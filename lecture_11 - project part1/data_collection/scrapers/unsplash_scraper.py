import requests
from .image import Image
from .base import Scraper


search_url = (
    "https://unsplash.com/napi/search/photos?page={p}&per_page=20&plus=none"
    + "&query=happy+person&xp=search-region-awareness%3Aexperiment"
)


class UnsplashScraper(Scraper):
    def get_image_specs(self):
        image_specs = []
        total_pages = 5
        for page in range(total_pages):
            print(f"Page: {page + 1} - {total_pages}")
            url = search_url.format(p=page + 1)
            response = requests.get(url)
            images = response.json()["results"]
            for image in images:
                url = image["urls"]["small"]
                slug = image["slug"]
                image_specs.append(Image(url=url, slug=slug))
        return image_specs

    def download_images(self, image_specs):
        for idx, spec in enumerate(image_specs):
            print(f"downloading: {idx + 1} - {len(image_specs)}")
            response = requests.get(spec.url)
            with open(f"images/{spec.slug}.png", "wb") as f:
                f.write(response.content)

    def run(self):
        #image_specs = self.get_image_specs()
        #self.download_images(image_specs)
        print("runing unsplash")


if __name__ == "__main__":
    scraper = UnsplashScraper()
    scraper.run()
