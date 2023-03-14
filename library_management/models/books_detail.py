from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BooksDetail(models.Model):
    _name = "books.detail"
    _description = "Library books"
    _rec_name = "title"

    title = fields.Char(required=True)
    borrow_ids = fields.One2many("borrow.books", "book_id")
    author = fields.Char()
    publisher = fields.Char()
    publication_year = fields.Integer()
    isbn = fields.Char()
    genre = fields.Selection(
        [
            ("fiction", "Fiction"),
            ("non-fiction", "Non-Fiction"),
            ("drama", "Drama"),
            ("study", "Study"),
        ]
    )
