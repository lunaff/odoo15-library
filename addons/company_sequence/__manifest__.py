{
    'name': 'Company Sequence',
    "version": '17.0.1.0.0',
    "category": 'Company',    
    'description': 'Creates companies when the module is installed.',
    'depends': ['web', 'mail', 'base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/sales_sequence.xml',
    ],
    'assets': {

    },
    "installable": True,
    "auto_install": False,
}
