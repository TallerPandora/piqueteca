# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Autora'
        db.create_table(u'piqueteca_app_autora', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Autora'])

        # Adding model 'Lectora'
        db.create_table(u'piqueteca_app_lectora', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Lectora'])

        # Adding model 'Estado_libro'
        db.create_table(u'piqueteca_app_estado_libro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Estado_libro'])

        # Adding model 'Estado_prestamo'
        db.create_table(u'piqueteca_app_estado_prestamo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Estado_prestamo'])

        # Adding model 'Editorial'
        db.create_table(u'piqueteca_app_editorial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Editorial'])

        # Adding model 'Licencia'
        db.create_table(u'piqueteca_app_licencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('licencia', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Licencia'])

        # Adding model 'Categoria'
        db.create_table(u'piqueteca_app_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Categoria'])

        # Adding model 'Tipo'
        db.create_table(u'piqueteca_app_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'piqueteca_app', ['Tipo'])

        # Adding model 'Libro'
        db.create_table(u'piqueteca_app_libro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('anio_edicion', self.gf('django.db.models.fields.IntegerField')()),
            ('editorial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['piqueteca_app.Editorial'])),
            ('resenia', self.gf('django.db.models.fields.CharField')(max_length=3000, null=True, blank=True)),
            ('enlace_descarga', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['piqueteca_app.Estado_libro'])),
            ('licencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['piqueteca_app.Licencia'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['piqueteca_app.Tipo'])),
        ))
        db.send_create_signal(u'piqueteca_app', ['Libro'])

        # Adding M2M table for field autora on 'Libro'
        m2m_table_name = db.shorten_name(u'piqueteca_app_libro_autora')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('libro', models.ForeignKey(orm[u'piqueteca_app.libro'], null=False)),
            ('autora', models.ForeignKey(orm[u'piqueteca_app.autora'], null=False))
        ))
        db.create_unique(m2m_table_name, ['libro_id', 'autora_id'])

        # Adding M2M table for field categoria on 'Libro'
        m2m_table_name = db.shorten_name(u'piqueteca_app_libro_categoria')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('libro', models.ForeignKey(orm[u'piqueteca_app.libro'], null=False)),
            ('categoria', models.ForeignKey(orm[u'piqueteca_app.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['libro_id', 'categoria_id'])

        # Adding model 'Prestamos'
        db.create_table(u'piqueteca_app_prestamos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lectora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['piqueteca_app.Lectora'])),
            ('fecha_prestamo', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('fecha_devolucion', self.gf('django.db.models.fields.DateTimeField')()),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['piqueteca_app.Estado_prestamo'])),
        ))
        db.send_create_signal(u'piqueteca_app', ['Prestamos'])

        # Adding M2M table for field libros on 'Prestamos'
        m2m_table_name = db.shorten_name(u'piqueteca_app_prestamos_libros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('prestamos', models.ForeignKey(orm[u'piqueteca_app.prestamos'], null=False)),
            ('libro', models.ForeignKey(orm[u'piqueteca_app.libro'], null=False))
        ))
        db.create_unique(m2m_table_name, ['prestamos_id', 'libro_id'])


    def backwards(self, orm):
        # Deleting model 'Autora'
        db.delete_table(u'piqueteca_app_autora')

        # Deleting model 'Lectora'
        db.delete_table(u'piqueteca_app_lectora')

        # Deleting model 'Estado_libro'
        db.delete_table(u'piqueteca_app_estado_libro')

        # Deleting model 'Estado_prestamo'
        db.delete_table(u'piqueteca_app_estado_prestamo')

        # Deleting model 'Editorial'
        db.delete_table(u'piqueteca_app_editorial')

        # Deleting model 'Licencia'
        db.delete_table(u'piqueteca_app_licencia')

        # Deleting model 'Categoria'
        db.delete_table(u'piqueteca_app_categoria')

        # Deleting model 'Tipo'
        db.delete_table(u'piqueteca_app_tipo')

        # Deleting model 'Libro'
        db.delete_table(u'piqueteca_app_libro')

        # Removing M2M table for field autora on 'Libro'
        db.delete_table(db.shorten_name(u'piqueteca_app_libro_autora'))

        # Removing M2M table for field categoria on 'Libro'
        db.delete_table(db.shorten_name(u'piqueteca_app_libro_categoria'))

        # Deleting model 'Prestamos'
        db.delete_table(u'piqueteca_app_prestamos')

        # Removing M2M table for field libros on 'Prestamos'
        db.delete_table(db.shorten_name(u'piqueteca_app_prestamos_libros'))


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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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