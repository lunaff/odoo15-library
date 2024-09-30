from odoo import models, fields, api

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