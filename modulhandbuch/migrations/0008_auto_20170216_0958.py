# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulhandbuch', '0007_auto_20160817_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualTeilnahme',
            fields=[
                ('namedentity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='modulhandbuch.NamedEntity')),
                ('beschreibungDe', models.TextField(help_text='Ausf\xfchrliche Beschreibung', verbose_name=b'Beschreibung', blank=True)),
                ('beschreibungEn', models.TextField(help_text=b'Extensive description', verbose_name=b'Beschreibung (engl.)', blank=True)),
            ],
            options={
                'ordering': ['nameDe'],
                'verbose_name': 'Qualifizierte Teilnahme',
                'verbose_name_plural': 'Qualifizierte Teilnahmen',
            },
            bases=('modulhandbuch.namedentity',),
        ),
        migrations.CreateModel(
            name='Studienleistung',
            fields=[
                ('namedentity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='modulhandbuch.NamedEntity')),
                ('beschreibungDe', models.TextField(help_text='Ausf\xfchrliche Beschreibung', verbose_name=b'Beschreibung', blank=True)),
                ('beschreibungEn', models.TextField(help_text=b'Extensive description', verbose_name=b'Beschreibung (engl.)', blank=True)),
            ],
            options={
                'ordering': ['nameDe'],
                'verbose_name': 'Studienleistung',
                'verbose_name_plural': 'Studienleistungen',
            },
            bases=('modulhandbuch.namedentity',),
        ),
        migrations.AddField(
            model_name='lehrveranstaltung',
            name='voraussetzungenDe',
            field=models.TextField(help_text='Formale Voraussetzungen f\xfcr die Teilnahme', verbose_name=b'Voraussetzungen', blank=True),
        ),
        migrations.AddField(
            model_name='lehrveranstaltung',
            name='voraussetzungenEn',
            field=models.TextField(help_text='Formale Voraussetzungen f\xfcr die Teilnahme (englische Beschreibung)', verbose_name=b'Voraussetzungen (engl.)', blank=True),
        ),
        migrations.AddField(
            model_name='modul',
            name='klausurdauer',
            field=models.PositiveIntegerField(default=0, help_text=b'Dauer der Klausur (in Minuten)', verbose_name='Klausurdauer'),
        ),
        migrations.AddField(
            model_name='modul',
            name='muendlichedauer',
            field=models.PositiveIntegerField(default=0, help_text=b'Dauer einer m\xc3\xbcndlichen Pr\xc3\xbcfung (in Minuten)', verbose_name='Dauer einer m\xfcndlichen Pr\xfcfung'),
        ),
        migrations.AlterField(
            model_name='modul',
            name='anzahlLvs',
            field=models.IntegerField(default=0, help_text='Wie viele Lehrveranstaltungen m\xfcssen in diesem Modul belegt werden? Zur Berechung des Arbeitsaufwandes notwendig.', verbose_name=b'Anzahl Lehrveranstaltungen'),
        ),
    ]
