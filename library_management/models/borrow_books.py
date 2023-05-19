from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BorrowBooks(models.Model):
    """Created borrow books model using this model one can borrow the books #T00316"""

    _name = "borrow.books"

    _description = "Library books borrower"
    _rec_name = "reader_id"

    borrow_seq = fields.Char(readonly=True)
    # T00316 Created readers id field to get readers data
    reader_id = fields.Many2one("readers.detail", required=True)

    # T00316 Created book id field to get books data
    book_id = fields.Many2one("books.detail", required=True)

    # T00316 Created borrow date field to borrow books
    borrow_date = fields.Date(default=fields.Date.today(), required=True)

    # T00316 Created return date field to return books
    return_date = fields.Date(required=True)

    @api.depends("return_date", "borrow_date")
    def _compute_duration(self):
        """Created compute duration method to calculate borrowed book duration #T00316"""
        for borrow in self:
            if borrow.borrow_date and borrow.return_date:
                borrow.duration = ((borrow.return_date) - (borrow.borrow_date)).days

            else:
                borrow.duration = 0

    duration = fields.Integer(
        compute="_compute_duration", string="Duration", store=True
    )

    @api.constrains("return_date")
    def _check_return_date(self):
        """Created return date constrains to get valid return date #T00316"""
        if self.return_date < self.borrow_date:
            raise ValidationError("return date cannot be earlier than borrow date")

    @api.model
    def create(self, vals):
        """Created sequence model for readers #T00316"""
        vals["borrow_seq"] = self.env["ir.sequence"].next_by_code("borrow.books")
        return super(BorrowBooks, self).create(vals)
