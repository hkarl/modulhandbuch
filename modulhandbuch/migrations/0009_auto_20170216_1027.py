# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulhandbuch', '0008_auto_20170216_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modul',
            name='klausurdauer',
        ),
        migrations.RemoveField(
            model_name='modul',
            name='muendlichedauer',
        ),
        migrations.AddField(
            model_name='modul',
            name='andereStudiengaengeText',
            field=models.TextField(help_text=b'Benennen Sie die Studieng\xc3\xa4nge, in denen dieses Modul noch benutzt wird.Nutzen Sie dieses Feld f\xc3\xbcr Studieng\xc3\xa4nge, die noch nicht in dieser Anwendung erfasst sind und nicht automatisch identifiziert werden.', verbose_name=b'Verwendung des Moduls in anderen Studieng\xc3\xa4ngen', blank=True),
        ),
        migrations.AddField(
            model_name='modul',
            name='qualteilnahme',
            field=models.ForeignKey(blank=True, to='modulhandbuch.QualTeilnahme', help_text=b'Gibt es eine qualfizierte Teilnahme f\xc3\xbcr dieses Modul?', null=True, verbose_name=b'Qualifizierte Teilnahme'),
        ),
        migrations.AddField(
            model_name='modul',
            name='studienleistung',
            field=models.ForeignKey(blank=True, to='modulhandbuch.Studienleistung', help_text=b'Gibt es eine Studienleistung f\xc3\xbcr dieses Modul?', null=True, verbose_name=b'Studienleistung'),
        ),
    ]
