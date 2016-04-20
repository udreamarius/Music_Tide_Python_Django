# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tide', '0003_song_is_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_favourite',
            new_name='is_favorite',
        ),
    ]
