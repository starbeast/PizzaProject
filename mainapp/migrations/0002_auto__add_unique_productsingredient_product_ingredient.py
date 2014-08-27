# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'ProductsIngredient', fields ['product', 'ingredient']
        db.create_unique(u'mainapp_productsingredient', ['product_id', 'ingredient_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ProductsIngredient', fields ['product', 'ingredient']
        db.delete_unique(u'mainapp_productsingredient', ['product_id', 'ingredient_id'])


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
            'Meta': {'unique_together': "(['product', 'ingredient'],)", 'object_name': 'ProductsIngredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Ingredient']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mainapp.Product']"})
        }
    }

    complete_apps = ['mainapp']