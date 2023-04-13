from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish('food', 23)
    dish2 = Dish('food', 23)
    dish3 = Dish('drink', 3)
    ingredient = Ingredient('bacon')
    ingredient_restrition = ({
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        })

    assert dish1 == Dish('food', 23)
    assert dish2 == Dish('food', 23)
    assert dish3 == Dish('drink', 3)

    assert dish1 == dish2
    assert dish2 != dish3
    assert dish3 != dish1

    assert dish1.name == 'food'
    assert dish2.name == 'food'
    assert dish3.name == 'drink'

    assert dish1.price == 23
    assert dish2.price == 23
    assert dish3.price == 3

    assert dish1.__repr__() == "Dish('food', R$23.00)"
    assert dish2.__repr__() == "Dish('food', R$23.00)"
    assert dish3.__repr__() == "Dish('drink', R$3.00)"

    assert dish1.__hash__() == dish2.__hash__()
    assert dish2.__hash__() != dish3.__hash__()
    assert dish3.__hash__() != dish1.__hash__()

    assert dish1.add_ingredient_dependency(ingredient, 1) is None
    assert dish2.add_ingredient_dependency(ingredient, 2) is None
    assert dish3.add_ingredient_dependency(ingredient, 3) is None

    assert dish1.recipe == {ingredient: 1}
    assert dish2.recipe == {ingredient: 2}
    assert dish3.recipe == {ingredient: 3}

    assert dish1.get_ingredients() == {ingredient}
    assert dish2.get_ingredients() == {ingredient}
    assert dish3.get_ingredients() == {ingredient}

    assert dish1.get_restrictions() == ingredient_restrition
    assert dish2.get_restrictions() == ingredient_restrition
    assert dish3.get_restrictions() == ingredient_restrition

    assert dish1.get_restrictions() == dish2.get_restrictions()
    assert dish2.get_restrictions() == dish3.get_restrictions()
    assert dish3.get_restrictions() == dish1.get_restrictions()

    with pytest.raises(TypeError):
        Dish('food')

    with pytest.raises(ValueError):
        Dish('food', -3)
