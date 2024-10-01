from odoo import fields, models, api
from odoo.exceptions import UserError

class LibraryLoan(models.Model):
    _name = "library.loan"
    _description = "Book Loan"

    book_id = fields.Many2one("library.book", string="Book", required=True)
    borrower_id = fields.Many2one("res.partner", string="Borrower", required=True)
    loan_date = fields.Date(string="Loan Date", default=fields.Date.context_today)
    return_date = fields.Date(string="Return Date")
    state = fields.Selection(
        [("draft", "Draft"), ("borrowed", "Borrowed"), ("returned", "Returned")],
        default="draft",
        string="Status"
    )
    
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

    def action_borrow_book(self):
        for loan in self:
            if loan.book_id.available_copies <= 0:
                raise UserError("No copies available for this book.")
            loan.state = 'borrowed'

    def action_return_book(self):
        for loan in self:
            loan.state = 'returned'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(LibraryLoan, self).fields_view_get(view_id, view_type, toolbar, submenu)
        if view_type == 'form':
            if self.state == 'draft':
                res['arch'] = res['arch'].replace('class="btn-primary"', 'class="btn-primary"')
            elif self.state == 'borrowed':
                res['arch'] = res['arch'].replace('class="btn-secondary"', 'class="btn-secondary"')
        return res


class WizardLoan(models.TransientModel):
    _name = 'wizard.loan'
    
    company_id = fields.Many2one('res.company', string="Company", required=True, default=lambda self: self.env.company)
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    
    def action_search_loans(self):
        domain = [('company_id', '=', self.company_id.id),
                  ('loan_date', '>=', self.start_date),
                  ('loan_date', '<=', self.end_date)]
        
        loans = self.env['library.loan'].search(domain)
        return {
            'name': 'Loans',
            'type': 'ir.actions.act_window',
            'res_model': 'library.loan',
            'view_mode': 'tree,form',
            'domain': domain,
            'target': 'current',
        }