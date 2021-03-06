# Generated by Django 3.0.6 on 2020-06-30 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20200509_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeitem',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite', to='recipes.Author'),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='recipes.Author'),
        ),
    ]
