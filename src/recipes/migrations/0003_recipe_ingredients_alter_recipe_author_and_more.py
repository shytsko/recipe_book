# Generated by Django 4.2.6 on 2023-10-17 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='', verbose_name='Ингридиенты'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(related_name='recipes', to='recipes.category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipes_img/', verbose_name='Изображение'),
        ),
    ]
