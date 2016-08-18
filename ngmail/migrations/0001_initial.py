# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NGUser'
        db.create_table('ngmail_nguser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('avatar_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('ngmail', ['NGUser'])

        # Adding model 'NGMessage'
        db.create_table('ngmail_ngmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['ngmail.NGUser'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipient', to=orm['ngmail.NGUser'])),
            ('date_and_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('ngmail', ['NGMessage'])


    def backwards(self, orm):
        # Deleting model 'NGUser'
        db.delete_table('ngmail_nguser')

        # Deleting model 'NGMessage'
        db.delete_table('ngmail_ngmessage')


    models = {
        'ngmail.ngmessage': {
            'Meta': {'object_name': 'NGMessage'},
            'date_and_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient'", 'to': "orm['ngmail.NGUser']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': "orm['ngmail.NGUser']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'ngmail.nguser': {
            'Meta': {'object_name': 'NGUser'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'avatar_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['ngmail']