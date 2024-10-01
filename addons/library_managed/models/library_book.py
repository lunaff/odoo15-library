from odoo import fields, models, api

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"

    name = fields.Char(string="Category Name", required=True)
    description = fields.Text()

    _sql_constraints = [
        ("name_uniq", "unique(name)", "The category name must be unique"),
    ]

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Book"

    attachment = fields.Binary(string="Attachment")
    name = fields.Char(string="Title", required=True)
    date_release = fields.Date()
    author_ids = fields.Many2many("res.partner", string="Authors")
    category_id = fields.Many2one("library.book.category", string="Category")
    description = fields.Html()
    total_borrows = fields.Integer(string="Total Borrows", compute="_compute_total_borrows", store=True)
    total_copies = fields.Integer(string="Total Copies", default=1)
    available_copies = fields.Integer(string="Available Copies", compute="_compute_available_copies", store=True)
    loan_ids = fields.One2many("library.loan", "book_id", string="Loans")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, required=True)
    _sql_constraints = [
        ("name_uniq", "unique(name)", "The book title must be unique"),
    ]

    @api.depends('loan_ids.state', 'total_copies')
    def _compute_available_copies(self):
        for book in self:
            borrowed_copies = len(book.loan_ids.filtered(lambda l: l.state == 'borrowed'))
            book.available_copies = book.total_copies - borrowed_copies

    @api.depends('loan_ids.state')
    def _compute_total_borrows(self):
        for book in self:
            total_borrows = len(book.loan_ids.filtered(lambda l: l.state in ['borrowed']))
            book.total_borrows = total_borrows 