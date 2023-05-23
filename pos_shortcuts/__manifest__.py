{
    'name': 'Arkane POS',
    'depends': ['base', 'point_of_sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_shortcuts_views.xml',
        'views/account.journals_view.xml',
        'views/pos_config_views.xml',
        'menu/pos_shortcut_menu.xml',



    ],


    'installable': True,
    'application': True,
    'auto_install': False,
}
