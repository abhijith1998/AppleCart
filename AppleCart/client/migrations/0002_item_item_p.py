# Generated by Django 2.2.4 on 2019-10-10 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_p',
            field=models.IntegerField(default=0),
        ),
    ]
