# Generated by Django 4.2.4 on 2023-08-16 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bouquet',
            options={'verbose_name': 'Букет', 'verbose_name_plural': 'Букеты'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
