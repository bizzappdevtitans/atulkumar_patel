from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class LibraryReport(models.Model):
    """created library report model to get Available books, borrowed books and overdue books #T00316"""

    _name = "library.report"
    _description = "Library report"

    name = fields.Char()
    report_seq = fields.Char(readonly=True)
    description = fields.Text()

    report_type = fields.Selection(
        [
            ("borrowed_books", "Borrowed Books"),
            ("overdue_books", "Overdue Books"),
            ("available_books", "Available Books"),
        ]
    )

    data = fields.Text(compute="_compute_data")

    @api.depends("report_type")
    def _compute_data(self):
        """created depends decorator to compute borrowed books, available books and overdue books # T00316"""
        for rec in self:
            if rec.report_type == "borrowed_books":
                rec.data = rec._get_borrowed_books()
                # T00316: calling get borrowed books method to get borrowed books
            elif rec.report_type == "available_books":
                rec.data = rec._get_available_books()
                # T00316: calling get available books method to get available books
            elif rec.report_type == "overdue_books":
                rec.data = rec._get_overdue_books()
                # T00316: calling get overdue books method to get overdue books
            else:
                value = ""
                rec.data = value

    def _get_borrowed_books(self):
        """created get borrowed books compute method to get borrowed books data #T00316"""
        borrowed_books = self.env["borrow.books"].search([])
        return "\n".join(
            [
                f"{borrow.reader_id.name}({borrow.book_id.title})"
                for borrow in borrowed_books
            ]
        )

    def _get_available_books(self):
        """created get available books compute method to get available books data #T00316"""
        available_books = self.env["books.detail"].search(
            [("id", "not in", self.env["borrow.books"].search([]).mapped("book_id.id"))]
        )
        return "\n".join([book.title for book in available_books])

    def _get_overdue_books(self):
        """created get overdue books compute method to get overdue books data #T00316"""

        overdue_books = self.env["borrow.books"].search(
            [("return_date", "<", fields.Date.today())]
        )
        return "\n".join(
            [
                f"{borrow.book_id.title}({borrow.reader_id.name})"
                for borrow in overdue_books
            ]
        )

    @api.model
    def create(self, vals):
        """created sequence model for readers #T00316"""
        vals["report_seq"] = self.env["ir.sequence"].next_by_code("library.report")
        return super(LibraryReport, self).create(vals)
