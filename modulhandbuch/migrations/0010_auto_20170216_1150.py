# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulhandbuch', '0009_auto_20170216_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modul',
            name='andereStudiengaengeText',
            field=models.TextField(help_text='Benennen Sie die Studieng\xe4nge, in denen dieses Modul noch benutzt wird. Nutzen Sie dieses Feld f\xfcr Studieng\xe4nge, die noch nicht in dieser Anwendung erfasst sind und nicht automatisch identifiziert werden.', verbose_name='Verwendung des Moduls in anderen Studieng\xe4ngen', blank=True),
        ),
        migrations.AlterField(
            model_name='modul',
            name='qualteilnahme',
            field=models.ForeignKey(blank=True, to='modulhandbuch.QualTeilnahme', help_text='Gibt es eine qualfizierte Teilnahme f\xfcr dieses Modul?', null=True, verbose_name='Qualifizierte Teilnahme'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='studienleistung',
            field=models.ForeignKey(blank=True, to='modulhandbuch.Studienleistung', help_text='Gibt es eine Studienleistung f\xfcr dieses Modul?', null=True, verbose_name='Studienleistung'),
        ),
    ]
