import random

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .forms import RecipeForm
from .mixins import RecipeAuthorCheckMixin
from .models import Recipe, Category


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение рецепта'
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related("author")


class RecipeListViewBase(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    title = None
    paginate_by = 5
    paginate_orphans = 1

    def get_title(self):
        if self.title is not None:
            return self.title
        else:
            return ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
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


class RecipeListByCategoryView(RecipeListViewBase):
    category = None
    slug_url_kwarg = 'slug'

    def get_category(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get(self.slug_url_kwarg))
        return self.category

    def get_queryset(self):
        category = self.get_category()
        return category.recipes.all()

    def get_title(self):
        return f"{self.category.name}"


class RecipeListByAuthorView(RecipeListViewBase):
    author = None
    author_username_kwarg = 'username'

    def get_author(self):
        self.author = get_object_or_404(get_user_model(), username=self.kwargs.get(self.author_username_kwarg))
        return self.author

    def get_queryset(self):
        author = self.get_author()
        return author.recipes.all()

    def get_title(self):
        return f"Рецепты от {self.author.username}"
