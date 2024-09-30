from odoo import models, fields, api

class LibraryBranchReport(models.Model):
    _name = 'multi.report'
    _description = 'Branch Library Reporting'

    company_id = fields.Many2one('res.company', string="Company", required=True)
    report_period_start = fields.Date(string="Report Start Date", required=True)
    report_period_end = fields.Date(string="Report End Date", required=True)
    total_books = fields.Integer(string="Total Books")
    total_loans = fields.Integer(string="Total Loans")
    available_books = fields.Integer(string="Available Books")