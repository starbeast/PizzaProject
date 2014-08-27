# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductCategory'
        db.create_table(u'mainapp_productcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mainapp', ['ProductCategory'])

        # Adding model 'Ingredient'
        db.create_table(u'mainapp_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mainapp', ['Ingredient'])

        # Adding model 'Product'
        db.create_table(u'mainapp_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.ProductCategory'])),
        ))
        db.send_create_signal(u'mainapp', ['Product'])

        # Adding model 'ProductsIngredient'
        db.create_table(u'mainapp_productsingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Product'])),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.Ingredient'])),
        ))
        db.send_create_signal(u'mainapp', ['ProductsIngredient'])


    def backwards(self, orm):
        # Deleting model 'ProductCategory'
        db.delete_table(u'mainapp_productcategory')

        # Deleting model 'Ingredient'
        db.delete_table(u'mainapp_ingredient')

        # Deleting model 'Product'
        db.delete_table(u'mainapp_product')

        # Deleting model 'ProductsIngredient'
        db.delete_table(u'mainapp_productsingredient')


    models = {
        u'mainapp.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mainapp.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.ProductCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mainapp.Ingredient']", 'through': u"orm['mainapp.ProductsIngredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'mainapp.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mainapp.productsingredient': {
            'Meta': {'object_name': 'ProductsIngredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Ingredient']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Product']"})
        }
    }

    complete_apps = ['mainapp']