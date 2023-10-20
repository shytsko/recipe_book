from django.db import models
from django.urls import reverse_lazy
from src.settings import AUTH_USER_MODEL

from services.utils import unique_slugify


class Recipe(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(verbose_name="Описание")
    ingredients = models.TextField(verbose_name="Ингридиенты")
    steps = models.TextField(verbose_name="Шаги приготовления")
    time = models.PositiveIntegerField(verbose_name="Время приготовления (мин)")
    image = models.ImageField(verbose_name="Изображение", upload_to='recipes_img/')
    author = models.ForeignKey(AUTH_USER_MODEL, related_name="recipes", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", verbose_name="Категории", related_name="recipes")

    class Meta:
        ordering = ["name"]
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('recipe_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('recipe_list_by_category', kwargs={'slug': self.slug})
