from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ReadersDetail(models.Model):
    _name = "readers.detail"
    _description = "Library books reader"

    name = fields.Char()
    email = fields.Char()
    gender = fields.Selection([("male", "Male"), ("female", "Female")])
    address = fields.Text()
    phone = fields.Char()
    is_reader = fields.Boolean(default=False)
    reader_ids = fields.One2many("borrow.books", "reader_id")

    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", " high"), ("3", "very high")],
        string="Status",
        default="1",
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("borrowed", "Borrowed"),
            ("returned", "Returned"),
            ("lost", "Lost"),
        ],
        string="State",
        default="draft",
    )

    @api.onchange("borrowed_books")
    def _onchange_borrowed_books(self):
        self.is_reader = True if self.reader_ids else False

    @api.constrains("phone")
    def _check_mobile_no(self):
        for record in self:
            if len(record.phone) > 15 or len(record.phone) < 6:

                raise ValidationError("Invalid mobile_number %s" % record.phone)
