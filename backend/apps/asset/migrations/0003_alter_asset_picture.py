# Generated by Django 3.2.6 on 2021-08-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20210826_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='picture',
            field=models.URLField(),
        ),
    ]