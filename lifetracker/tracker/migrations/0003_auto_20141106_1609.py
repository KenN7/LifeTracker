# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20141106_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='eventtype',
            field=models.CharField(default='Event', choices=[('Notif', 'Notification'), ('Event', 'Event')], max_length=20),
        ),
        migrations.DeleteModel(
            name='EventType',
        ),
    ]
