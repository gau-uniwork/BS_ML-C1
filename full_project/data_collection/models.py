from dataclasses import dataclass


@dataclass
class Image:
    """Class to represent the downloadable image"""

    url: str
    slug: str
    emotion: str
