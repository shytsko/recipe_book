from django.urls import path
from .views import RecipeCreateView

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    # path('<int:workplace_id>/', WorkplaceDetailView.as_view(), name='workplace_detail'),
    # path('<int:workplace_id>/update', WorkplaceUpdateView.as_view(), name='workplace_update'),
    # path('<int:workplace_id>/delete', WorkplaceDeleteView.as_view(), name='workplace_delete'),
]
