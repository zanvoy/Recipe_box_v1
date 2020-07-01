from django.db import models
from django.utils import timezone

# Create your models here.
class Author (models.Model):
    name = models.CharField(max_length=50, default='your name')
    bio = models.TextField(default='a little about me')
    favorite = models.ManyToManyField('RecipeItem', related_name='favorite')
    def __str__(self):
        return self.name

class RecipeItem(models.Model):
    title = models.CharField(max_length=30, default='name of food')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    description = models.TextField(default='a little about this food')
    time_required = models.CharField(max_length=30, default='10 mins')
    instructions = models.TextField(default='begin with...')
    def __str__(self):
        return self.title 
