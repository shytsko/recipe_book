from django.urls import path
from .views import RecipeCreateView, RecipeDetailView

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:recipe_id>/', RecipeDetailView.as_view(), name='recipe_detail'),
    # path('<int:workplace_id>/update', WorkplaceUpdateView.as_view(), name='workplace_update'),
    # path('<int:workplace_id>/delete', WorkplaceDeleteView.as_view(), name='workplace_delete'),
]
