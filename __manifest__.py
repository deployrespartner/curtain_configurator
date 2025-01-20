{
    'name': 'Curtain Configurator',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Configure and sell curtains',
    'description': """
        Module for configuring and selling curtains with specific measurements and options.
    """,
    'depends': ['sale_management', 'product'],
    'data': [
        'views/sale_views.xml',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}