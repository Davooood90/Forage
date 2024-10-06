def find_foods_without_allergens(menu, allergens):
    foods_without_allergens = {}
    for food, details in menu.items():
        if all(allergen not in details.get('allergens', []) for allergen in allergens):
            foods_without_allergens[food] = details

    return foods_without_allergens

def find_foods_with_special_diets(menu, diets):
    foods_with_diets = {}

    for food, details in menu.items():
        if all(diet in details.get('special diets', []) for diet in diets):
            foods_with_diets[food] = details

    return foods_with_diets

