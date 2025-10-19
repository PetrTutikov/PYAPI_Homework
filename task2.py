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


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """Принимает сп. блюд и кол-во персон, возвращает словарь"""
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                name = ing['ingredient_name']
                quantity = ing['quantity'] * person_count
                measure = ing['measure']

                if name in shop_list:
                    # Если ингредиент уже есть, увеличиваем количество
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюдо '{dish}' не найдено.")

    return shop_list

# Проверка
cook_book = read_recipes('recipes.txt')

dishes_to_cook = ['Запеченный картофель', 'Омлет']
person_count = 2

shopping_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)

print(shopping_list)