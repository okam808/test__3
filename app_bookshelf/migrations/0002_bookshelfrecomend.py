# Generated by Django 2.1.5 on 2020-01-25 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookShelfRecomend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_shelf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.BookShelfMaster', verbose_name='本棚(FK)')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー(FK)')),
            ],
            options={
                'verbose_name_plural': 'おススメ本棚',
                'db_table': 'book_shelf_recomend',
            },
        ),
    ]
