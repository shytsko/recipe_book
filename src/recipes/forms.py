from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {'categories': CheckboxSelectMultiple(), }
