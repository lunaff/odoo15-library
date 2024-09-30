from odoo import api, fields, models
from odoo.exceptions import ValidationError
import xlsxwriter
import base64
from io import BytesIO


class LibraryLoanExportWizard(models.TransientModel):
    _name = 'library.loan.export.wizard'
    _description = 'Export Library Loan to Excel'

    book_id = fields.Many2one("library.book", string="Books", required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    file_data = fields.Binary(string="File Data", readonly=True)
    file_name = fields.Char(string="File Name", readonly=True)

    def action_export_excel(self):
        domain = []

        if self.book_id:
            domain.append(('book_id', '=', self.book_id.id))
        if self.start_date:
            domain.append(('loan_date', '>=', self.start_date))
        if self.end_date:
            domain.append(('loan_date', '<=', self.end_date))

        loans = self.env['library.loan'].search(domain)

        # raise ValidationError(loans)

        # Mengelompokkan data peminjaman berdasarkan buku
        loan_data = {}
        for loan in loans:
            if loan.book_id.name not in loan_data:
                loan_data[loan.book_id.name] = {}
            borrower = loan.borrower_id.name
            days_borrowed = (loan.return_date - loan.loan_date).days if loan.return_date and loan.loan_date else 0
            if borrower in loan_data[loan.book_id.name]:
                loan_data[loan.book_id.name][borrower] += days_borrowed
            else:
                loan_data[loan.book_id.name][borrower] = days_borrowed

        # write data to excel file

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Library Loan')

        headers = ['Book', 'Borrower Name', 'Total Days']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        row = 1
        for book, borrowers in loan_data.items():
            for borrower, days in borrowers.items():
                worksheet.write(row, 0, book)
                worksheet.write(row, 1, borrower)
                worksheet.write(row, 2, days)
                row += 1

        workbook.close()

        output.seek(0)
        file_data = base64.b64encode(output.read()).decode()
        output.close()

        self.write({
            'file_data': file_data,
            'file_name': "library_loan_report.xlsx"
        })
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content?model={self._name}&id={self.id}&field=file_data&filename_field=file_name&download=true',
            'target': 'new',
        }
