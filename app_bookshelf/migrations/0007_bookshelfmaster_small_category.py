# Generated by Django 2.1.5 on 2020-02-05 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookshelf', '0006_auto_20200205_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshelfmaster',
            name='small_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.SmallCategory', verbose_name='小カテゴリ(FK)'),
        ),
    ]
