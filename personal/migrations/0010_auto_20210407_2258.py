# Generated by Django 3.1.7 on 2021-04-07 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0009_auto_20210407_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='allergen',
            field=models.ManyToManyField(blank=True, to='personal.Allergen'),
        ),
    ]
