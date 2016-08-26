# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NGMessageFolder'
        db.create_table('ngmail_ngmessagefolder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('folder_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('ngmail', ['NGMessageFolder'])

        # Adding field 'NGMessage.folder'
        db.add_column('ngmail_ngmessage', 'folder',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['ngmail.NGMessageFolder']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'NGMessageFolder'
        db.delete_table('ngmail_ngmessagefolder')

        # Deleting field 'NGMessage.folder'
        db.delete_column('ngmail_ngmessage', 'folder_id')


    models = {
        'ngmail.ngmessage': {
            'Meta': {'object_name': 'NGMessage'},
            'date_and_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ngmail.NGMessageFolder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ngmail.NGUser']", 'related_name': "'recipient'"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ngmail.NGUser']", 'related_name': "'sender'"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'ngmail.ngmessagefolder': {
            'Meta': {'object_name': 'NGMessageFolder'},
            'folder_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ngmail.nguser': {
            'Meta': {'object_name': 'NGUser'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'avatar_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['ngmail']