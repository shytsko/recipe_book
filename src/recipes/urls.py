from django.urls import path
from .views import RecipeCreateView, RecipeDetailView, RecipeListAllViewBase, RecipeDeleteView, RecipeUpdateView

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:recipe_id>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('list/all/', RecipeListAllViewBase.as_view(), name='recipe_list_all'),
    path('delete/<int:recipe_id>/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('update/<int:recipe_id>/', RecipeUpdateView.as_view(), name='recipe_update'),
]
