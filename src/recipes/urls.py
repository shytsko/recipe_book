from django.urls import path
from .views import RecipeCreateView, RecipeDetailView, RecipeListAllView, RecipeDeleteView, RecipeUpdateView, \
    RecipeListMyView, RecipeListRandomView

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('list/all/', RecipeListAllView.as_view(), name='recipe_list_all'),
    path('list/my/', RecipeListMyView.as_view(), name='recipe_list_my'),
    path('list/random/', RecipeListRandomView.as_view(), name='recipe_list_random'),
    path('delete/<slug:slug>/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('update/<slug:slug>/', RecipeUpdateView.as_view(), name='recipe_update'),
]
