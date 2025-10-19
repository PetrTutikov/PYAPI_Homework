def read_recipes(filename):
    """читает файл с рецептами и возвращает словарь cook_book"""
    recipes = {}
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            # Название блюда.
            dish_name = file.readline()
            while dish_name and dish_name.strip() == "":
                dish_name = file.readline()
            if not dish_name:
                break
            dish_name = dish_name.strip()

            # Кол-во ингредиентов.
            ingredients_count = int(file.readline().strip())
            ingredients = []

            # Все ингредиенты.
            for _ in range(ingredients_count):
                line = file.readline().strip()
                name, quantity, unit = [part.strip() for part in line.split('|')]
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(quantity),
                    'measure': unit
                })

            recipes[dish_name] = ingredients
    return recipes


def print_recipes(recipes):
    """Вывод рецептов."""
    for dish, ingredients in recipes.items():
        print(f"\n{dish}:")
        for ing in ingredients:
            print(f"  {ing['ingredient_name']} - {ing['quantity']} {ing['measure']}")


# запуск программы
cook_book = read_recipes('recipes.txt')
print_recipes(cook_book)
