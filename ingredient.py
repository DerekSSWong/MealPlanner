class Ingredient:
    """Represents one portion of ingredient.

    Attributes:
        name (str): The name of the ingredient.
        desc (str): The description of the ingredient.

    Example:
        The Ingredient class is contructed like so:
        ::
            $ Ingredient("steak", "ideally ribeye")
    """
    def __init__(self,  name:str, desc:str) -> None:
        self.ingredient_dict = {
            "Name": name,
            "Description:": desc
        }

    def __str__(self) -> str:
        return str(self.ingredient_dict)