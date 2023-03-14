from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BorrowBooks(models.Model):
    _name = "borrow.books"
    _description = "Library books borrower"
    _rec_name = "reader_id"

    reader_id = fields.Many2one("readers.detail")
    book_id = fields.Many2one("books.detail")
    borrow_date = fields.Date(default=fields.Date.today())

    print("\n\n\n\n\n\n", fields.Date.today())
    return_date = fields.Date()

    @api.constrains("return_date")
    def _check_return_date(self):
        if self.return_date < self.borrow_date:
            raise ValidationError("return date cannot be earlier than borrow date")
