{
    "name": "Freeze Category in POS",
    "description": """ Freeze Category in POS.""",
    "version": "15.0.0.0",
    "data": [
        # 'views/views.xml'
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_freeze_category/static/src/js/pos.js'
        ],
        'web.assets_qweb': [
            'pos_freeze_category/static/src/xml/**/*',
        ],
    },
    "depends": ["base", 'pos_restaurant', 'point_of_sale'],
}
