class Ingredient:
    """Represents one portion of ingredient. Contains the name and description of the given ingredient.

    Example:
        The Ingredient class is contructed like so:
        ::

            $ Ingredient("steak", "ideally cheap")
    """

    NAME_MAX_LENGTH = 32
    DESCRIPTION_MAX_LENGTH = 128

    def __init__(self,  name:str, desc:str) -> None:
        self.name = name
        self.desc = desc
    
    @property
    def name(self):
        """Name of the ingredient.

        Returns:
            str: Non-empty string within 32 characters.
        """
        return self._name
    
    @name.setter
    def name(self, value):
        #First check if string
        if not isinstance(value, str):
            raise TypeError(f"Ingredient name must be a string, not {type(value).__name__}")
        
        #Check if string length is between 1 and max length
        _stripped_value = value.strip()
        if len(_stripped_value) == 0:
            raise ValueError("The name of the ingredient cannot be blank")
        elif len(_stripped_value) > self.NAME_MAX_LENGTH:
            raise ValueError("Ingredient name cannot exceed 32 characters")
        
        self._name = _stripped_value
    
    @property
    def desc(self):
        """Description of the ingredient

        Returns:
            str: String within 128 characters
        """
        return self._desc
    
    @desc.setter
    def desc(self, value):
        _stripped_value = str(value).strip()

        #Check if string exceeds length
        if len(_stripped_value) > self.DESCRIPTION_MAX_LENGTH:
            raise ValueError("Ingredient description cannot exceed 128 characters")

        self._desc = _stripped_value

    def __str__(self) -> str:
        return str(self.ingredient_dict)