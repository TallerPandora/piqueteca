# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Tipo'
        db.create_table(u'piqueteca_app_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Tipo'])


    models = {
    }

    complete_apps = ['piqueteca_app']
