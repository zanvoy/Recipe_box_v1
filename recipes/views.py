from django.shortcuts import render, reverse, HttpResponseRedirect
from recipes.models import RecipeItem, Author
from recipes.forms import AddRecipeForm, AddAuthorForm

# Create your views here.
def index (request):
    foodInfo = RecipeItem.objects.all()
    return render(request, 'index.html', {'foodData': foodInfo})


def addRecipeView(request):
    html = "recipeAdd.html"
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeItem.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect('/')
    form = AddRecipeForm()
    return render(request, html, {'form': form})


def addAuthorView(request):
    html = "authorAdd.html"
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect('/')
    form = AddAuthorForm()
    return render(request, html, {'form': form})


def authorView (request, author_id):
    authorInfo = Author.objects.filter(id=author_id)
    authorInfo = authorInfo.first()
    allRecipes = RecipeItem.objects.filter(author=author_id)
    return render(request, 'author.html', {'authorData': authorInfo, 'allRecipes': allRecipes})


def recipeView (request, recipe_id):
    foodInfo = RecipeItem.objects.filter(id=recipe_id)
    foodInfo = foodInfo.first()
    return render(request, 'recipe.html', {'foodData': foodInfo})