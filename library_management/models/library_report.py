from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class LibraryReport(models.Model):
    _name = "library.report"
    _description = "Library report"

    name = fields.Char()
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
        for rec in self:
            if rec.report_type == "borrowed_books":
                rec.data = rec._get_borrowed_books()
            elif rec.report_type == "available_books":
                rec.data = rec._get_available_books()
            elif rec.report_type == "overdue_books":
                rec.data = rec._get_overdue_books()
            else:
                value = ""
                rec.data = value

    def _get_borrowed_books(self):
        borrowed_books = self.env["borrow.books"].search([])
        return "\n".join(
            [
                f"{borrow.reader_id.name}({borrow.book_id.title})"
                for borrow in borrowed_books
            ]
        )

    def _get_available_books(self):
        available_books = self.env["books.detail"].search(
            [("id", "not in", self.env["borrow.books"].search([]).mapped("book_id.id"))]
        )
        return "\n".join([book.title for book in available_books])

    def _get_overdue_books(self):
        overdue_books = self.env["borrow.books"].search(
            ["return_date", "<", fields.Date.today()]
        )
        return "\n".join(
            [
                f"{borrow.book_id.title}({borrow.reader_id.name})"
                for borrow in overdue_books
            ]
        )
