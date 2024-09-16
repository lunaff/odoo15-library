from odoo import models, fields

class CustomerType(models.Model):
    _name = "customer.type"
    _description = "Customer Type"

    name = fields.Char(string="Customer Type Name", required=True)
    customer_type = fields.Selection([
        ('toko', 'Toko'),
        ('bengkel', 'Bengkel'),
        ('modern_market', 'Modern Market'),
        ('ex_dealer_danapaint', 'Ex Dealer Danapaint')
    ], string='Customer Type', default='toko')


    _sql_constraints = [
        ("name_uniq", "unique(name)", "The customer type must be unique"),
    ]
