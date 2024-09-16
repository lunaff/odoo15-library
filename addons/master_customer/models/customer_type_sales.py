# from odoo import models, fields

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'

#     customer_type = fields.Selection(
#         related='partner_id.customer_type', 
#         string='Customer Type', 
#         readonly=True,
#         store=True
#     )

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_type_id = fields.Many2one('customer.type', string='Customer Type')
