# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('path', models.FilePathField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('frequency', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('done', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='events',
            name='eventtype',
            field=models.ForeignKey(to='tracker.EventType', related_name='events'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='events',
            name='icon',
            field=models.ForeignKey(to='tracker.Icon', related_name='events'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='events',
            name='recurent',
            field=models.ForeignKey(to='tracker.Period', related_name='events'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='events',
            name='author',
            field=models.ForeignKey(to='tracker.User', related_name='events'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pad',
            name='user',
            field=models.OneToOneField(to='tracker.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(to='tracker.User', related_name='todo'),
            preserve_default=True,
        ),
    ]
