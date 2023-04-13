import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        try:
            with open(source_path, 'r') as f:
                file = csv.DictReader(f)
                self.dishes = self.__create_menu__(file)
        except FileNotFoundError:
            print('File not found.')

    def __create_menu__(self, file):
        dishes = {}
        for line in file:
            if dishes.get(line['dish']) is None:
                dish = Dish(line['dish'], float(line['price']))
                dishes[line['dish']] = dish
            dish.add_ingredient_dependency(
                Ingredient(line['ingredient']),
                int(line['recipe_amount'])
                )
        return set(dishes.values())
