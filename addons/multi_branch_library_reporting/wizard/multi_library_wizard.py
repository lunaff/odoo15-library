from odoo import models, fields, api
import io
import xlsxwriter
import base64

class LibraryBranchReportWizard(models.TransientModel):
    _name = 'multi.report.wizard'
    _description = 'Library Branch Report Wizard'

    company_id = fields.Many2one('res.company', string="Company", help="Select a company for the report. Choose 'All Companies' to include data for all companies.")
    report_period_start = fields.Date(string="Start Date", required=True)
    report_period_end = fields.Date(string="End Date", required=True)

    @api.model
    def default_get(self, fields_list):
        res = super(LibraryBranchReportWizard, self).default_get(fields_list)
        admin_company = self.env.user.company_id.id == 1
        if admin_company:
            res['company_id'] = None 
        return res

    def action_generate_report(self):
        company_ids = []
        if self.env.user.company_id.id == 1:
            if not self.company_id:
                company_ids = self.env['res.company'].search([]).ids  
            else:
                company_ids = [self.company_id.id]
        else:
            company_ids = [self.env.user.company_id.id]

        # Create an Excel file in memory
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()

        # Write headers
        sheet.write(0, 0, 'Company')
        sheet.write(0, 1, 'Start Date')
        sheet.write(0, 2, 'End Date')
        sheet.write(0, 3, 'Book Name')
        sheet.write(0, 4, 'Total Books')
        sheet.write(0, 5, 'Total Loans')
        sheet.write(0, 6, 'Available Books')

        row = 1
        for company in self.env['res.company'].browse(company_ids):
            # Get all books for the company
            books = self.env['library.book'].search([('company_id', '=', company.id)])
            total_books = len(books)  # Total number of books for the company

            for book in books:
                # Prepare the domain for loans
                domain = [
                    ('book_id', '=', book.id),
                    ('loan_date', '<=', self.report_period_end),  
                    ('return_date', '>=', self.report_period_start)
                ]

                loans = self.env['library.loan'].search(domain)
                total_loans = len(loans)
                available_books = total_books - total_loans

                # Write data for each book
                sheet.write(row, 0, company.name)
                sheet.write(row, 1, str(self.report_period_start))
                sheet.write(row, 2, str(self.report_period_end))
                sheet.write(row, 3, book.name)
                sheet.write(row, 4, total_books)
                sheet.write(row, 5, total_loans)
                sheet.write(row, 6, available_books)
                row += 1

        # Close the workbook
        workbook.close()

        # Save the file and convert it to base64 to store it in Odoo
        file_data = base64.b64encode(output.getvalue())
        output.close()

        # Create an attachment for the Excel file
        attachment = self.env['ir.attachment'].create({
            'name': f'Library Branch Report - {("All Companies" if not self.company_id else self.company_id.name)}.xlsx',
            'type': 'binary',
            'datas': file_data,
            'res_model': 'multi.report.wizard',
            'res_id': self.id,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        # Return action to download the file
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }
