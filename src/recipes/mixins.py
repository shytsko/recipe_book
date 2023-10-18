from django.core.exceptions import PermissionDenied


class RecipeAuthorCheckMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.user.pk != obj.author_id:
            raise PermissionDenied(f"Вы не автор этого рецепта")
        return obj
