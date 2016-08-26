# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'NGMessageFolder.folder_name'
        db.delete_column('ngmail_ngmessagefolder', 'folder_name')


    def backwards(self, orm):
        # Adding field 'NGMessageFolder.folder_name'
        db.add_column('ngmail_ngmessagefolder', 'folder_name',
                      self.gf('django.db.models.fields.CharField')(max_length=30, default=1),
                      keep_default=False)


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