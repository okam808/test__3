# Generated by Django 2.1.5 on 2020-02-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookshelf', '0005_auto_20200205_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_10',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ISBN-10'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn_13',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ISBN-13'),
        ),
    ]