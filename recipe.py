from typing import List
from ingredient import Ingredient

class Recipe:
    """Represents a recipe for one meal.

    Attributes:
        name (str): The name of the recipe.
        desc (str): The description of the recipe.
        ingredients (List[Ingredient]): List of ingredients needed for the recipe
    """
    def __init__(self,  name:str, desc:str, ingredients:List[Ingredient]) -> None:
        self.recipe_dict = {
            "Name": name,
            "Description": desc,
            "Ingredients": ingredients
        }

    def __str__(self) -> str:
        return str(self.ingredient_dict)