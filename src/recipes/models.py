from django.db import models
from src.settings import AUTH_USER_MODEL


class Recipe(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание")
    steps = models.TextField(verbose_name="Шаги приготовления")
    time = models.TimeField(verbose_name="Время приготовления")
    image = models.ImageField(verbose_name="Изображение")
    author = models.ForeignKey(AUTH_USER_MODEL, related_name="recipes", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Сategory", verbose_name="Категории", blank=True, related_name="recipes")

    class Meta:
        ordering = ["name"]
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name


class Сategory(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=100)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
