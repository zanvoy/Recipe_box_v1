from django.shortcuts import render
from recipes.models import RecipeItem, Author


# Create your views here.
def index (request):
    foodInfo = RecipeItem.objects.all()
    return render(request, 'index.html', {'foodData': foodInfo})

def authorView (request, author_id):
    authorInfo = Author.objects.filter(id=author_id)
    authorInfo = authorInfo.first()
    allRecipes = RecipeItem.objects.filter(author=author_id)
    return render(request, 'author.html', {'authorData': authorInfo, 'allRecipes': allRecipes})

def recipeView (request, recipe_id):
    foodInfo = RecipeItem.objects.filter(id=recipe_id)
    foodInfo = foodInfo.first()
    return render(request, 'recipe.html', {'foodData': foodInfo})