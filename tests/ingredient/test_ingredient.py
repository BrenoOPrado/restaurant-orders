from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
ingredient = Ingredient('Testando')


# Req 1
def test_ingredient():
    print('/-----------------------------------------/')
    print(ingredient.__eq__())
    print('/-----------------------------------------/')
    pass
