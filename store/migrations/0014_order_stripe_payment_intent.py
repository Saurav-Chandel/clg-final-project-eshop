# Generated by Django 3.0.6 on 2022-06-16 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_payment_intent',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
