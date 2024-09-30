from odoo import fields, models, api

class SaleSequence(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        customer_id = vals.get('partner_id')
        if customer_id:
            customer = self.env['res.partner'].browse(customer_id)
            company_registry = customer.company_registry or '00'
        else:
            company_registry = '00'

        sequence_number = self.env['ir.sequence'].next_by_code('company.quotation.sequence')
        vals['name'] = f"{company_registry}-{sequence_number}"

        return super(SaleSequence, self).create(vals)