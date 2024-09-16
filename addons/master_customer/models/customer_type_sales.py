from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_type_id = fields.Many2one('customer.type', string='Customer Type')
