# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Map.month'
        db.add_column(u'Karamoja_map', 'month',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=4, to=orm['Karamoja.Months']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Map.month'
        db.delete_column(u'Karamoja_map', 'month_id')


    models = {
        u'Karamoja.districts': {
            'Meta': {'object_name': 'Districts'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'district_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Karamoja.documentation': {
            'Meta': {'object_name': 'Documentation'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Karamoja.indicators': {
            'Meta': {'object_name': 'Indicators'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicator_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Sectors']"})
        },
        u'Karamoja.livelihoodzonephaseclassification': {
            'Meta': {'object_name': 'LivelihoodZonePhaseClassification'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dews_created': ('django.db.models.fields.DateTimeField', [], {}),
            'district': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'livelihoodzones': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.LivelihoodZones']"}),
            'months': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Months']"}),
            'phase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Phase']", 'to_field': "'phase_id'"}),
            'riskofdrought': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.RiskOfDrought']", 'to_field': "'risk_of_drought_id'"}),
            'sequenceid': ('django.db.models.fields.BigIntegerField', [], {}),
            'trends': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Trends']", 'to_field': "'trends_id'"}),
            'years': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Years']"})
        },
        u'Karamoja.livelihoodzones': {
            'Meta': {'object_name': 'LivelihoodZones'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Karamoja.map': {
            'Meta': {'object_name': 'Map'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Districts']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'month': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Months']"})
        },
        u'Karamoja.months': {
            'Meta': {'object_name': 'Months'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'Karamoja.phase': {
            'Meta': {'object_name': 'Phase'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phase_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'Karamoja.report': {
            'Meta': {'object_name': 'Report'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'Karamoja.riskofdrought': {
            'Meta': {'object_name': 'RiskOfDrought'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'risk_of_drought_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'Karamoja.sectors': {
            'Meta': {'object_name': 'Sectors'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Karamoja.trends': {
            'Meta': {'object_name': 'Trends'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trends_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'})
        },
        u'Karamoja.vulnerabilityindicators': {
            'Meta': {'object_name': 'VulnerabilityIndicators'},
            'datavalue': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'district': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicators': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Indicators']"}),
            'livelihoodzones': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.LivelihoodZones']"}),
            'months': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Months']"}),
            'phase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Phase']"}),
            'sectors': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Sectors']"}),
            'sequenceid': ('django.db.models.fields.BigIntegerField', [], {}),
            'years': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Karamoja.Years']"})
        },
        u'Karamoja.years': {
            'Meta': {'object_name': 'Years'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'yearly': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['Karamoja']