from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import RecipeForm
from .models import Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'recipes/recipe_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(RecipeCreateView, self).form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/recipe_detail.html'
    pk_url_kwarg = 'recipe_id'
