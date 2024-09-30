# Copyright 2016-2017 LasLabs Inc.
# Copyright 2017-2018 Tecnativa - Jairo Llopis
# Copyright 2018-2019 Tecnativa - Alexandre Díaz
# Copyright 2021 ITerra - Sergey Shebanin
# Copyright 2023 Onestein - Anjeel Haria
# Copyright 2023 Taras Shabaranskyi
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Master Customer",
    "summary": "Master Customer",
    "version": "17.0.1.0.1",
    "category": "Customer",    
    "depends": ["web", "mail", "sale", "base"],
    "data": [
        "security/ir.model.access.csv",
        "views/customer_menu.xml",
        "views/customer_type_form.xml",
        "views/customer_type_sales.xml",
    ],
    "assets": {
    },
    "installable": True,
    "auto_install": False,
}
