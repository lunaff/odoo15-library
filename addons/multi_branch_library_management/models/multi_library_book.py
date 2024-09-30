from odoo import models, fields, api

class LibraryBook(models.Model):
    _inherit = 'library.book'
    
    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company, required=True
    )