# -*- coding: utf-8 -*-
{
    'name': "Purchase Product Multi Add",

    'summary': """
        Purchase Product Multi Add""",

    'author': "Exemax , Brenda Gauto",
    'website': "http://www.exemax.com.ar",

    'category': 'purchase',
    'version': '14.0.1',

    'depends': ['base','purchase','product'],

    'data': [
        'security/ir.model.access.csv',
        'wizards/purchase_import_products_view.xml',
        'views/purchase_view.xml',
    ],
}
