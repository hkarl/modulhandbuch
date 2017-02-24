# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulhandbuch', '0014_auto_20170224_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modul',
            name='gewichtung',
            field=models.PositiveIntegerField(default=0, help_text='Gewichtung dieses Moduls f\xfcr die Gesamtnote.', verbose_name='Gewichtung f\xfcr Gesamtnote', blank=True),
        ),
    ]
