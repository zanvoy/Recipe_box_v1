# Generated by Django 3.0.6 on 2020-05-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20200509_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeitem',
            name='description',
            field=models.TextField(default='a little about this food'),
        ),
    ]
