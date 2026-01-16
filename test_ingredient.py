import pytest
from ingredient import Ingredient



def test_get_name():
    test_ingredient = Ingredient("Prawn", "Frozen is fine")
    assert test_ingredient.name == "Prawn"

def test_empty_name():
    with pytest.raises(ValueError) as exc_info:
        Ingredient("", "No space")
    assert "The name of the ingredient cannot be blank" in str(exc_info.value)

def test_space_name():
    with pytest.raises(ValueError) as exc_info:
        Ingredient(" ", "One space")
    assert "The name of the ingredient cannot be blank" in str(exc_info.value)

def test_long_name():
    with pytest.raises(ValueError) as exc_info:
        Ingredient('a' * 33, "one two three")
    assert "Ingredient name cannot exceed 32 characters" in str(exc_info.value)

def test_number_name():
    with pytest.raises(TypeError) as exc_info:
        Ingredient(123, "one two three")
    assert "Ingredient name must be a string" in str(exc_info.value)
    
def test_get_desc():
    test_ingredient = Ingredient("Prawn", "Frozen is fine")
    assert test_ingredient.desc == "Frozen is fine"

def test_long_desc():
    with pytest.raises(ValueError) as exc_info:
        Ingredient("big name", 'a' * 129)
    assert "Ingredient description cannot exceed 128 characters" in str(exc_info.value)