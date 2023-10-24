from .models import Category


def categories(request):
    """Добавляет в контекст переменную greeting с приветствием."""
    return {
        'categories': Category.objects.all()
    }
