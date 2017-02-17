# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulhandbuch', '0010_auto_20170216_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='lehrveranstaltung',
            name='teilnehmerUE',
            field=models.PositiveIntegerField(default=0, help_text=b'Von Verwaltung geforderte Angabe zur Teilnehmerzahl f\xc3\xbcr der Veranstaltung zugeordnete \xc3\x9cbungsGRUPPE. (Nicht: Anzahl der Gruppen!) Angeblich wegen Kapazit\xc3\xa4tsverordnung; Relevanz unklar; Datengrundlage unklar; Verwendung unklar; Vereinheitlichung unklar. Im Zweifel Fantasiezahl eintragen.', null=True, verbose_name=b'Teilnehmerzahl LV/VL', blank=True),
        ),
        migrations.AddField(
            model_name='lehrveranstaltung',
            name='teilnehmerVL',
            field=models.PositiveIntegerField(default=0, help_text=b'Von Verwaltung geforderte Angabe zur Teilnehmerzahl f\xc3\xbcr Veranstaltung (typischerweise: Vorlesung) an sich. Angeblich wegen Kapazit\xc3\xa4tsverordnung; Relevanz unklar; Datengrundlage unklar; Verwendung unklar; Vereinheitlichung unklar. Im Zweifel Fantasiezahl eintragen.', null=True, verbose_name=b'Teilnehmerzahl LV/VL', blank=True),
        ),
    ]
