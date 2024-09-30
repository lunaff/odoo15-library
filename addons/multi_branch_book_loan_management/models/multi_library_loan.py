from odoo import models, fields, api

class LibraryLoan(models.Model):
    _inherit = 'library.loan'

    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, 
                                 default=lambda self: self.env.company)

    @api.onchange('book_id')
    def _onchange_book_id(self):
        if self.book_id:
            self.company_id = self.book_id.company_id

    @api.model
    def create(self, vals):
        if 'book_id' in vals:
            book = self.env['library.book'].browse(vals['book_id'])
            vals['company_id'] = book.company_id.id
        return super(LibraryLoan, self).create(vals)