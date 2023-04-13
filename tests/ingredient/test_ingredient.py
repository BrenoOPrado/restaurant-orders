from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_test1 = Ingredient('bacon')
    ingredient_test2 = Ingredient('bacon')
    ingredient_test3 = Ingredient('carne')

    assert ingredient_test1 == ingredient_test2

    assert ingredient_test1.__hash__() == ingredient_test2.__hash__()
    assert ingredient_test2.__hash__() != ingredient_test3.__hash__()
    assert ingredient_test3.__hash__() != ingredient_test1.__hash__()

    assert ingredient_test1.__repr__() == "Ingredient('bacon')"
    assert ingredient_test2.__repr__() == "Ingredient('bacon')"
    assert ingredient_test3.__repr__() == "Ingredient('carne')"

    assert ingredient_test1.name == 'bacon'
    assert ingredient_test2.name == 'bacon'
    assert ingredient_test3.name == 'carne'

    assert ingredient_test1.name != 'carne'
    assert ingredient_test2.name != 'carne'
    assert ingredient_test3.name != 'bacon'

    restrictions = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}

    assert ingredient_test1.restrictions == restrictions
    assert ingredient_test2.restrictions == restrictions
    assert ingredient_test3.restrictions == restrictions
