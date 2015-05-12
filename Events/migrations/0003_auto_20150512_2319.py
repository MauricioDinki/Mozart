# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Events.models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20150512_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover',
            field=models.FileField(null=True, upload_to=Events.models.event_cover_url, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='finish_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Dia'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30'), (b'31', b'31')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='month',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'', b'Mes'), (b'Enero', b'Enero'), (b'Febrero', b'Febrero'), (b'Marzo', b'Marzo'), (b'Abril', b'Abril'), (b'Mayo', b'Mayo'), (b'Junio', b'Junio'), (b'Julio', b'Julio'), (b'Agosto', b'Agosto'), (b'Septiembre', b'Septiembre'), (b'Octubre', b'Octubre'), (b'Noviembre', b'Noviembre'), (b'Diciembre', b'Diciembre')]),
            preserve_default=True,
        ),
    ]
