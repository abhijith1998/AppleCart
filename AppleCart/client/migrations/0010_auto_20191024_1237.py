# Generated by Django 2.2.4 on 2019-10-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_auto_20191024_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='', upload_to='images/client'),
        ),
    ]
