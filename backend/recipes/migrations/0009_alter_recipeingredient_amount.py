# Generated by Django 3.2.19 on 2023-06-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20230623_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
    ]
