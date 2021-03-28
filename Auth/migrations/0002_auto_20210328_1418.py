# Generated by Django 3.1.7 on 2021-03-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tenant_type',
            field=models.IntegerField(choices=[(1, 'Restaurant'), (2, 'Customer'), (3, 'Courier')], default=2),
        ),
    ]
