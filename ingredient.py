class Ingredient:
    """Represents one portion of ingredient. Contains the name and description of the given ingredient.

    Example:
        The Ingredient class is contructed like so:
        ::
            $ Ingredient("steak", "ideally ribeye")
    """
    def __init__(self,  name:str, desc:str) -> None:
        self.name = name
        self.desc = desc
    
    @property
    def name(self):
        """Retrieves the name of the ingredient

        Returns:
            str
        """
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = str(value)
    
    @property
    def desc(self):
        """Retrieves the description of the ingredient

        Returns:
            str
        """
        return self._desc
    
    @desc.setter
    def desc(self, value):
        self._desc = value

    def __str__(self) -> str:
        return str(self.ingredient_dict)
    

test = Ingredient("testname", "desc")
print(test.name)
