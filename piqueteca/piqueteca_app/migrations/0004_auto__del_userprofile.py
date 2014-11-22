# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'piqueteca_app_userprofile')


    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'piqueteca_app_userprofile', (
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'piqueteca_app', ['UserProfile'])


    models = {
        u'piqueteca_app.autora': {
            'Meta': {'object_name': 'Autora'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'piqueteca_app.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'piqueteca_app.editorial': {
            'Meta': {'object_name': 'Editorial'},
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'piqueteca_app.estado_libro': {
            'Meta': {'object_name': 'Estado_libro'},
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'piqueteca_app.estado_prestamo': {
            'Meta': {'object_name': 'Estado_prestamo'},
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'piqueteca_app.lectora': {
            'Meta': {'object_name': 'Lectora'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'piqueteca_app.libro': {
            'Meta': {'object_name': 'Libro'},
            'anio_edicion': ('django.db.models.fields.IntegerField', [], {}),
            'autora': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['piqueteca_app.Autora']", 'symmetrical': 'False'}),
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['piqueteca_app.Categoria']", 'symmetrical': 'False'}),
            'editorial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['piqueteca_app.Editorial']"}),
            'enlace_descarga': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['piqueteca_app.Estado_libro']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licencia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['piqueteca_app.Licencia']"}),
            'resenia': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['piqueteca_app.Tipo']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'piqueteca_app.licencia': {
            'Meta': {'object_name': 'Licencia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licencia': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'piqueteca_app.prestamos': {
            'Meta': {'object_name': 'Prestamos'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['piqueteca_app.Estado_prestamo']"}),
            'fecha_devolucion': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_prestamo': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lectora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['piqueteca_app.Lectora']"}),
            'libros': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['piqueteca_app.Libro']", 'symmetrical': 'False'})
        },
        u'piqueteca_app.tipo': {
            'Meta': {'object_name': 'Tipo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['piqueteca_app']