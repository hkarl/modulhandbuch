# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulhandbuch', '0013_auto_20170222_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='modul',
            name='gewichtung',
            field=models.PositiveIntegerField(default=0, help_text=b'Gewichtung dieses Moduls f\xc3\xbcr die Gesamtnote.', verbose_name=b'Gewichtung f\xc3\xbcr Gesamtnote', blank=True),
        ),
        migrations.AddField(
            model_name='modul',
            name='voraussetzungenDe',
            field=models.TextField(help_text='Formale Voraussetzungen f\xfcr die Teilnahme an MODUL', verbose_name=b'Voraussetzungen', blank=True),
        ),
        migrations.AddField(
            model_name='modul',
            name='voraussetzungenEn',
            field=models.TextField(help_text='Formale Voraussetzungen f\xfcr die Teilnahme (englische Beschreibung)', verbose_name=b'Voraussetzungen (engl.)', blank=True),
        ),
        migrations.AlterField(
            model_name='modul',
            name='modulteilpruefung',
            field=models.ForeignKey(blank=True, to='modulhandbuch.Modulteilpruefung', help_text='W\xe4hlen Sie der Liste eine evtl. erlaubte oder durchgef\xfchrte Teilpr\xfcfungsform aus.', null=True, verbose_name='Modulteilpr\xfcfungsformen'),
        ),
    ]
