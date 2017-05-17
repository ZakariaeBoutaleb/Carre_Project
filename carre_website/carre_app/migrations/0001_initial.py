# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id_categorie', models.AutoField(db_column='id_Categorie', primary_key=True, serialize=False)),
                ('name_categorie', models.CharField(blank=True, db_column='name_Categorie', max_length=50, null=True)),
            ],
            options={
                'db_table': 'categorie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id_collection', models.AutoField(db_column='id_Collection', primary_key=True, serialize=False)),
                ('name_collection', models.CharField(blank=True, db_column='name_Collection', max_length=50, null=True)),
            ],
            options={
                'db_table': 'collection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'comporter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(db_column='id_Product', primary_key=True, serialize=False)),
                ('name_product', models.CharField(blank=True, db_column='name_Product', max_length=50, null=True)),
                ('reference_product', models.CharField(blank=True, db_column='reference_Product', max_length=50, null=True)),
                ('couleur_product', models.CharField(blank=True, db_column='couleur_Product', max_length=50, null=True)),
                ('dimensions_product', models.CharField(blank=True, db_column='dimensions_Product', max_length=50, null=True)),
                ('url_product', models.CharField(blank=True, db_column='url_Product', max_length=50, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subcategorie',
            fields=[
                ('id_subcategorie', models.AutoField(db_column='id_SubCategorie', primary_key=True, serialize=False)),
                ('name_subcategorie', models.CharField(blank=True, db_column='name_SubCategorie', max_length=50, null=True)),
            ],
            options={
                'db_table': 'subcategorie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypeProduct',
            fields=[
                ('id_type', models.AutoField(db_column='id_Type', primary_key=True, serialize=False)),
                ('name_type', models.CharField(blank=True, db_column='name_Type', max_length=50, null=True)),
            ],
            options={
                'db_table': 'type_product',
                'managed': False,
            },
        ),
    ]