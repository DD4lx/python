# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nums', models.IntegerField(default=0, verbose_name='数量')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('is_select', models.BooleanField(default=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户')),
            ],
            options={
                'db_table': 'f_shopping_cart',
            },
        ),
    ]
