# Generated by Django 3.2.6 on 2021-08-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='', upload_to='media/shop/images'),
        ),
    ]
