# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulhandbuch', '0011_auto_20170217_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulteilpruefungen',
            fields=[
                ('namedentity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='modulhandbuch.NamedEntity')),
                ('beschreibungDe', models.TextField(help_text='Ausf\xfchrliche Beschreibung', verbose_name=b'Beschreibung', blank=True)),
                ('beschreibungEn', models.TextField(help_text=b'Extensive description', verbose_name=b'Beschreibung (engl.)', blank=True)),
            ],
            options={
                'ordering': ['nameDe'],
                'verbose_name': 'Modulteilpr\xfcfungsform',
                'verbose_name_plural': 'Modulteilpr\xfcfungsformen',
            },
            bases=('modulhandbuch.namedentity',),
        ),
        migrations.AddField(
            model_name='modul',
            name='wahlmoeglichkeitenDe',
            field=models.TextField(verbose_name='Wahlm\xf6glichkeiten innerhalb eines Moduls (de)', blank=True),
        ),
        migrations.AddField(
            model_name='modul',
            name='wahlmoeglichkeitenEn',
            field=models.TextField(verbose_name='Wahlm\xf6glichkeiten innerhalb eines Moduls (en)', blank=True),
        ),
        migrations.AlterField(
            model_name='lehrveranstaltung',
            name='teilnehmerUE',
            field=models.PositiveIntegerField(default=0, help_text='Von Verwaltung geforderte Angabe zur Teilnehmerzahl f\xfcr der Veranstaltung zugeordnete \xdcbungsGRUPPE. (Nicht: Anzahl der Gruppen!) Angeblich wegen Kapazit\xe4tsverordnung; Relevanz unklar; Datengrundlage unklar; Verwendung unklar; Vereinheitlichung unklar. Im Zweifel Fantasiezahl eintragen.', null=True, verbose_name=b'Teilnehmerzahl LV/VL', blank=True),
        ),
        migrations.AlterField(
            model_name='lehrveranstaltung',
            name='teilnehmerVL',
            field=models.PositiveIntegerField(default=0, help_text='Von Verwaltung geforderte Angabe zur Teilnehmerzahl f\xfcr Veranstaltung (typischerweise: Vorlesung) an sich. Angeblich wegen Kapazit\xe4tsverordnung; Relevanz unklar; Datengrundlage unklar; Verwendung unklar; Vereinheitlichung unklar. Im Zweifel Fantasiezahl eintragen.', null=True, verbose_name='Teilnehmerzahl LV/VL', blank=True),
        ),
        migrations.AddField(
            model_name='modul',
            name='modulteilpruefunen',
            field=models.ForeignKey(blank=True, to='modulhandbuch.Modulteilpruefungen', help_text=b'W\xc3\xa4hlen Sie der Liste eine evtl. erlaubte oder durchgef\xc3\xbchrte Teilpr\xc3\xbcfungsform aus.', null=True, verbose_name='Modulteilpr\xfcfungsformen'),
        ),
    ]
