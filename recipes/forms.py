from django import forms
from recipes.models import Author


class AddRecipeForm (forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)

class EditRecipeForm (forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)

class AddAuthorForm (forms.ModelForm):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)

class loginForm (forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)