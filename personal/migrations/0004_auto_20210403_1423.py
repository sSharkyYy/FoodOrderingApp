# Generated by Django 3.1.7 on 2021-04-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_remove_dish_allergen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='types',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.restaurantprofile'),
        ),
    ]
