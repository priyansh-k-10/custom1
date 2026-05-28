{
    'name': 'Sample Custom Module',

    'version': '1.0.0',

    'category': 'Custom',

    'summary': 'Learning custom module',

    'description': """
Sample Custom Module
====================

Learning custom module development in Odoo.
""",

    'author': 'Priyansh Khatri',

    'license': 'LGPL-3',

    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/sample_module_views.xml',
        'views/res_partner_views.xml',
    ],

    'installable': True,

    'application': True,

    'auto_install': False,
}