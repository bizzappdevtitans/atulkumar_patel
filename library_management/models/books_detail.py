from odoo import models, fields, api


class BooksDetail(models.Model):
    """Books detail model to create books #T00316"""

    _name = "books.detail"
    _description = "Library books"
    _rec_name = "title"

    title = fields.Char(required=True)
    book_seq = fields.Char(readonly=True)
    # T00316 Created borrow_ids field which is related to borrow books model
    img = fields.Image()
    borrow_ids = fields.One2many("borrow.books", "book_id")
    author = fields.Char(required=True)
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

    @api.model
    def create(self, vals):
        """Created sequence model for books detail model #T00316"""
        vals["book_seq"] = self.env["ir.sequence"].next_by_code("books.detail")
        return super(BooksDetail, self).create(vals)
