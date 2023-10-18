import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .forms import RecipeForm
from .mixins import RecipeAuthorCheckMixin
from .models import Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'recipes/recipe_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(RecipeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новый рецепт'
        return context


class RecipeDeleteView(LoginRequiredMixin, RecipeAuthorCheckMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/delete_confirm.html'
    pk_url_kwarg = 'recipe_id'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить рецепт?'
        context['cancel_url'] = self.object.get_absolute_url()
        return context


class RecipeUpdateView(LoginRequiredMixin, RecipeAuthorCheckMixin, UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name = 'recipes/recipe_edit.html'
    pk_url_kwarg = 'recipe_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение рецепта'
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/recipe_detail.html'
    pk_url_kwarg = 'recipe_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class RecipeListViewBase(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class RecipeListAllView(RecipeListViewBase):
    title = 'Все рецепты'


class RecipeListMyView(RecipeListViewBase):
    title = 'Мои рецепты'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author_id=self.request.user.pk)


class RecipeListRandomView(RecipeListViewBase):
    title = 'Случайные рецепты'

    def get_queryset(self):
        queryset = super().get_queryset()
        all_pk = list(queryset.values_list("pk", flat=True))
        random_pk = random.sample(all_pk, 5)
        return queryset.filter(pk__in=random_pk)
