# Generated by Django 4.2.4 on 2023-08-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerapp', '0004_alter_bouquet_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='type',
            field=models.CharField(choices=[('на день рождения', 'на день рождения'), ('на свадьбу', 'на свадьбу'), ('в школу', 'в школу'), ('без повода', 'без повода')], default='без повода', max_length=50, verbose_name='Тип букета'),
        ),
    ]