# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulhandbuch', '0012_auto_20170222_1614'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Modulteilpruefungen',
            new_name='Modulteilpruefung',
        ),
        migrations.RenameField(
            model_name='modul',
            old_name='modulteilpruefunen',
            new_name='modulteilpruefung',
        ),
    ]
