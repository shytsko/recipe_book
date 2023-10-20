from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'ingredients', 'steps', 'time', 'image', 'categories')
        widgets = {'categories': CheckboxSelectMultiple(), }
