# Generated by Django 3.1.7 on 2021-03-28 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20210328_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='allergenfreeID',
            new_name='allergen_free',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='RestaurantID',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='StyleID',
            new_name='style',
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='TypeID',
            new_name='type',
        ),
    ]