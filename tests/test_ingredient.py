import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngridient:

    @pytest.mark.parametrize("ingredient_type, name, price", 
                             [(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15),
                              (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337)])
    def test_ingridient_init_and_getters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
