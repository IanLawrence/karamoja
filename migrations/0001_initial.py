# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Districts'
        db.create_table(u'Karamoja_districts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Karamoja', ['Districts'])

        # Adding model 'Years'
        db.create_table(u'Karamoja_years', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yearly', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Karamoja', ['Years'])

        # Adding model 'Months'
        db.create_table(u'Karamoja_months', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('monthly', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Karamoja', ['Months'])

        # Adding model 'LivelihoodZones'
        db.create_table(u'Karamoja_livelihoodzones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Karamoja', ['LivelihoodZones'])

        # Adding model 'Sectors'
        db.create_table(u'Karamoja_sectors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'Karamoja', ['Sectors'])

        # Adding model 'RiskOfDrought'
        db.create_table(u'Karamoja_riskofdrought', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('risk_of_drought_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'Karamoja', ['RiskOfDrought'])

        # Adding model 'Trends'
        db.create_table(u'Karamoja_trends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('trends_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'Karamoja', ['Trends'])

        # Adding model 'Indicators'
        db.create_table(u'Karamoja_indicators', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Sectors'])),
            ('indicator_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'Karamoja', ['Indicators'])

        # Adding model 'Phase'
        db.create_table(u'Karamoja_phase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phase_id', self.gf('django.db.models.fields.IntegerField')(unique=True)),
        ))
        db.send_create_signal(u'Karamoja', ['Phase'])

        # Adding model 'Report'
        db.create_table(u'Karamoja_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'Karamoja', ['Report'])

        # Adding model 'Documentation'
        db.create_table(u'Karamoja_documentation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'Karamoja', ['Documentation'])

        # Adding model 'Map'
        db.create_table(u'Karamoja_map', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Districts'])),
        ))
        db.send_create_signal(u'Karamoja', ['Map'])

        # Adding model 'LivelihoodZonePhaseClassification'
        db.create_table(u'Karamoja_livelihoodzonephaseclassification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.IntegerField')()),
            ('years', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Years'])),
            ('months', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Months'])),
            ('riskofdrought', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.RiskOfDrought'], to_field='risk_of_drought_id')),
            ('livelihoodzones', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.LivelihoodZones'])),
            ('phase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Phase'], to_field='phase_id')),
            ('trends', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Trends'], to_field='trends_id')),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('sequenceid', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'Karamoja', ['LivelihoodZonePhaseClassification'])

        # Adding model 'VulnerabilityIndicators'
        db.create_table(u'Karamoja_vulnerabilityindicators', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.IntegerField')()),
            ('years', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Years'])),
            ('months', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Months'])),
            ('livelihoodzones', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.LivelihoodZones'])),
            ('sectors', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Sectors'])),
            ('indicators', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Indicators'])),
            ('phase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Karamoja.Phase'])),
            ('datavalue', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sequenceid', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'Karamoja', ['VulnerabilityIndicators'])


    def backwards(self, orm):
        # Deleting model 'Districts'
        db.delete_table(u'Karamoja_districts')

        # Deleting model 'Years'
        db.delete_table(u'Karamoja_years')

        # Deleting model 'Months'
        db.delete_table(u'Karamoja_months')

        # Deleting model 'LivelihoodZones'
        db.delete_table(u'Karamoja_livelihoodzones')

        # Deleting model 'Sectors'
        db.delete_table(u'Karamoja_sectors')

        # Deleting model 'RiskOfDrought'
        db.delete_table(u'Karamoja_riskofdrought')

        # Deleting model 'Trends'
        db.delete_table(u'Karamoja_trends')

        # Deleting model 'Indicators'
        db.delete_table(u'Karamoja_indicators')

        # Deleting model 'Phase'
        db.delete_table(u'Karamoja_phase')

        # Deleting model 'Report'
        db.delete_table(u'Karamoja_report')

        # Deleting model 'Documentation'
        db.delete_table(u'Karamoja_documentation')

        # Deleting model 'Map'
        db.delete_table(u'Karamoja_map')

        # Deleting model 'LivelihoodZonePhaseClassification'
        db.delete_table(u'Karamoja_livelihoodzonephaseclassification')

        # Deleting model 'VulnerabilityIndicators'
        db.delete_table(u'Karamoja_vulnerabilityindicators')


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
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
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