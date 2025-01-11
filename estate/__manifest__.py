{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': [
        'base',
    ],
    'author': 'Your Name',
    'category': 'Real Estate',
    'description': """
        Real Estate Module
    """,
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
}