# Generated by Django 3.2.7 on 2021-09-21 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_subcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
    ]
