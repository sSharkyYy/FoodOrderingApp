# Generated by Django 3.1.7 on 2021-05-04 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0016_auto_20210504_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personal.restaurantprofile'),
        ),
    ]
