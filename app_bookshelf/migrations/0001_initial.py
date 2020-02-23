# Generated by Django 2.1.5 on 2020-01-25 15:43

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(blank=True, max_length=255, null=True, verbose_name='性別')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年齢')),
                ('favorite_genre', models.CharField(blank=True, max_length=255, null=True, verbose_name='好きなジャンル')),
                ('keyword_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='キーワード１')),
                ('keyword_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='キーワード２')),
                ('keyword_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='キーワード３')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'custom_user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='著者名')),
            ],
            options={
                'verbose_name_plural': '著者マスタ',
                'db_table': 'author_master',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='書籍名')),
                ('image_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品画像URL')),
                ('publish_date', models.DateTimeField(verbose_name='出版日')),
                ('book_detail', models.CharField(blank=True, max_length=10000, null=True, verbose_name='書籍詳細')),
                ('size_page', models.IntegerField(blank=True, null=True, verbose_name='ページ数')),
                ('size_height', models.IntegerField(blank=True, null=True, verbose_name='寸法（高さ）')),
                ('size_width', models.IntegerField(blank=True, null=True, verbose_name='寸法（幅）')),
                ('isbn_10', models.IntegerField(blank=True, null=True, verbose_name='ISBN-10')),
                ('isbn_13', models.IntegerField(blank=True, null=True, verbose_name='ISBN-13')),
                ('purchase_page_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='購入ページURL')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.Author', verbose_name='著者(FK)')),
            ],
            options={
                'verbose_name_plural': '書籍マスタ',
                'db_table': 'book_master',
            },
        ),
        migrations.CreateModel(
            name='BookReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_review', models.CharField(blank=True, max_length=5000, null=True, verbose_name='書籍レビュー')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.Book', verbose_name='書籍(FK)')),
            ],
            options={
                'verbose_name_plural': '書籍レビューテーブル',
                'db_table': 'book_reviews_table',
            },
        ),
        migrations.CreateModel(
            name='BookShelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.Book', verbose_name='書籍(FK)')),
            ],
            options={
                'verbose_name_plural': '本棚',
                'db_table': 'book_shelf',
            },
        ),
        migrations.CreateModel(
            name='BookShelfMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_shelf_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='本棚名')),
            ],
            options={
                'verbose_name_plural': '本棚マスタ',
                'db_table': 'book_shelf_master',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.Book', verbose_name='書籍(FK)')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー(FK)')),
            ],
            options={
                'verbose_name_plural': '閲覧履歴テーブル',
                'db_table': 'history_table',
            },
        ),
        migrations.CreateModel(
            name='LargeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learge_category_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='大カテゴリ名')),
            ],
            options={
                'verbose_name_plural': '大カテゴリマスタ',
                'db_table': 'large_category_master',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.Book', verbose_name='書籍(FK)')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー(FK)')),
            ],
            options={
                'verbose_name_plural': 'いいねテーブル',
                'db_table': 'like_table',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='出版社名')),
            ],
            options={
                'verbose_name_plural': '出版社マスタ',
                'db_table': 'publisher_master',
            },
        ),
        migrations.CreateModel(
            name='SmallCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_catogory_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='小カテゴリ名')),
                ('learge_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.LargeCategory', verbose_name='大カテゴリ(FK)')),
            ],
            options={
                'verbose_name_plural': '小カテゴリマスタ',
                'db_table': 'small_category_master',
            },
        ),
        migrations.AddField(
            model_name='bookshelf',
            name='book_shelf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.BookShelfMaster', verbose_name='本棚(FK)'),
        ),
        migrations.AddField(
            model_name='book',
            name='learge_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.LargeCategory', verbose_name='大カテゴリ(FK)'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.Publisher', verbose_name='出版社(FK)'),
        ),
        migrations.AddField(
            model_name='book',
            name='small_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_bookshelf.SmallCategory', verbose_name='小カテゴリ(FK)'),
        ),
    ]