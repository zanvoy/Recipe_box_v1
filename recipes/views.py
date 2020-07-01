from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from recipes.models import RecipeItem, Author
from recipes.forms import AddRecipeForm, AddAuthorForm, loginForm, EditRecipeForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index (request):
    foodInfo = RecipeItem.objects.all()
    return render(request, 'index.html', {'foodData': foodInfo})


def loginView(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = loginForm()
    return render(request, 'login.html', {'form':form})


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
                bio=data['bio'],
                username=data['username'],
                password=data['password']
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


def favoriteView (request, author_id):
    author = Author.objects.get(id=author_id)
    favorites= author.favorite.all()
    return render(request, 'favorite.html', {'author': author, 'favorites': favorites})

@login_required
def recipeEdit(request, recipe_id):
    recipe = RecipeItem.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.author = data['author']
            recipe.description = data['description']
            recipe.time_required = data['time_required']
            recipe.instructions = data['instructions']
            recipe.save()
            return HttpResponseRedirect('/recipe/'+ str(recipe_id))

    form = EditRecipeForm(initial={
        'title':recipe.title,
        'author':recipe.author,
        'description':recipe.description,
        'time_required':recipe.time_required,
        'instructions':recipe.instructions
    })
    return render(request, 'recipeAdd.html', {'form': form})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def favoriteAddView(request, id):
    author = request.user.author
    # breakpoint()
    author.favorite.add(RecipeItem.objects.get(id=id))
    author.save()
    return HttpResponseRedirect('/author/'+ str(author.id)+'/favorite')