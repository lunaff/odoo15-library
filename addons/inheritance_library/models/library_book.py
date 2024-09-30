from odoo import fields, models

class LibraryBook(models.Model):
    _inherit = "library.book"

    attachment = fields.Binary(string="Attachment")
