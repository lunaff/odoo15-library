from odoo import models, fields, api

class ResConfigSettings(models.Model):
    _inherit = 'sale.order'

    customer_type = fields.Selection([
        ('toko', 'Toko'),
        ('bengkel', 'Bengkel'),
        ('modern_market', 'Modern Market'),
        ('ex_dealer_danapaint', 'Ex Dealer Danapaint')
    ], string='Customer Type' 
    #config_parameter='master_customer.customer_type'
    )
