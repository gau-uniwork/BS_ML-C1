from abc import ABC, abstractmethod


class Scraper(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError()
