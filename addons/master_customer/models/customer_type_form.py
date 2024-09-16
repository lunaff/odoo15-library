from odoo import models, fields

class CustomerType(models.Model):
    _name = "customer.type"
    _description = "Customer Type"

    customer_type = fields.Selection([
        ('toko', 'Toko'),
        ('bengkel', 'Bengkel'),
        ('modern_market', 'Modern Market'),
        ('ex_dealer_danapaint', 'Ex Dealer Danapaint')
    ], string='Customer Type', default=lambda self: [('toko', 'Toko'), ('bengkel', 'Bengkel'), ('modern_market', 'Modern Market'), ('ex_dealer_danapaint', 'Ex Dealer Danapaint')], readonly=True)

    _sql_constraints = [
        ("name_uniq", "unique(customer_type)", "The customer type must be unique"),
    ]

# class CustomerTypeMenu(models.Model):
#     _inherit = "sale.order"

