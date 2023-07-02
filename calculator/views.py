from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe(request, recipe_name):
    recipe = DATA.get(recipe_name)
    if not recipe:
        return render(request, '404.html')

    servings = request.GET.get('servings')
    if servings:
        servings = int(servings)
        recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)
