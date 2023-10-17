from django.forms import ModelForm, CheckboxSelectMultiple, TimeInput

from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {'categories': CheckboxSelectMultiple(),
                   'time': TimeInput(format='%H:%M')}
