from django.shortcuts import render
from recipes.models import RecipeItem, Author


# Create your views here.
def index (request):
    foodInfo = RecipeItem.objects.all()
    return render(request, 'index.html', {'foodData': foodInfo})

def authorView (request):
    authorInfo= Author.objects.all()
    return render(request, 'author.html', {'authorData': authorInfo})

def recipeView (request):
    foodInfo = RecipeItem.objects.all()
    return render(request, 'recipe.html', {'foodData': foodInfo})