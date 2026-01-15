
from ingredient import Ingredient

test_ingredient = Ingredient("Prawn", "Frozen is fine")

def test_get_name():
    assert test_ingredient.name == "Prawn"

def test_get_desc():
    assert test_ingredient.desc == "Frozen is fine"