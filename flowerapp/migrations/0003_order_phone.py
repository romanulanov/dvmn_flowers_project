# Generated by Django 4.2.4 on 2023-08-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerapp', '0002_alter_bouquet_options_alter_order_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(blank=True, default=89999999, verbose_name='Телефон'),
            preserve_default=False,
        ),
    ]
