import os
import pytest
from ingredient_book import IngredientBook

def add_ingredient():
    ingredient_book = IngredientBook()
    ingredient_book.add_ingredient('shrimp', 'frozen is fine')

@pytest.mark.parametrize("value", [None, "", 48, 'a'*33])
def add_wrong_ingredient():
    None