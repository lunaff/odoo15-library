{
    "name": "Library Managed",
    "version": "17.0.1.0.0",
    "category": "Addons",
    "summary": "Library is an addons for Odoo 17 to manage library",
    "description": """Library is an addons for Odoo 17 to manage library""",
    "author": "April",
    "company": "April Company",
    "maintainer": "ERP Team April Company",
    "depends": ["web", "mail", "base"],
    "data": [
        "security/ir.model.access.csv",
        "report/library_book_report.xml",
        "report/library_loan_report.xml",
        "views/library_book_view.xml",
        "views/library_loan_view.xml",
        "views/library_menu.xml",
        "views/library_loan_report_templates.xml",
        "views/library_book_report_templates.xml",
        "wizard/library_loan_wizard_views.xml",    
    ],
    "assets": {},
    "images": ["static/description/icon.png"],
    "installable": True,
    "auto-install": False,
    "license": "LGPL-3",
}
