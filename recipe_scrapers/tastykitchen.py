from ._abstract import AbstractScraper
from ._utils import normalize_string


class TastyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "tastykitchen.com"

    def title(self):
        return self.soup.find("h1", {"itemprop": "name"}).get_text()

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class": "ingredients"}).findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find("span", {"itemprop": "instructions"}).findAll("p")

        return "\n".join(
            [normalize_string(direction.get_text()) for direction in instructions]
        )
