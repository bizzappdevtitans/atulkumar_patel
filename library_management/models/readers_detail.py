from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ReadersDetail(models.Model):
    """created readers detail model to get readers data #T00316"""

    _name = "readers.detail"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Library books reader"

    name = fields.Char(required=True)
    reader_seq = fields.Char(readonly=True)
    email = fields.Char()
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        default="male",
    )
    address = fields.Text()
    phone = fields.Char(tracking=True)

    # created is reader boolean field to check reader is a member of library or not
    is_reader = fields.Boolean(default=False, readonly=True)

    # created reader ids field to get borrowed book id
    reader_ids = fields.One2many("borrow.books", "reader_id")

    # created total borowed book field to get count of borrowed books
    total_borrowed_book = fields.Integer(compute="_count_book", store=True)

    # created count field to get the count of total books in library
    count = fields.Integer(compute="_count_books")
    get_borrowed_books = fields.Char(compute="get_books")

    # created priority widget to give rating to the readers
    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", " high"), ("3", "very high")],
        string="Status",
        default="1",
    )

    # created state fields to check the status of readers
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("borrowed", "Borrowed"),
            ("returned", "Returned"),
            ("lost", "Lost"),
        ],
        tracking=True,
        string="State",
        default="draft",
    )

    def get_books(self):
        if self.total_borrowed_book == 1:
            borrow_book_form = self.env.ref("library_management.borrow_books_view_form")

            return {
                "name": "borrowed",
                "res_model": "borrow.books",
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "views": [(borrow_book_form.id, "form")],
                "domain": [("reader_id", "=", self.id)],
            }

        return {
            "name": "borrowed",
            "res_model": "borrow.books",
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "domain": [("reader_id", "=", self.id)],
        }

    def action_lost(self):
        self.write({"state": "lost"})

    def action_draft(self):
        self.write({"state": "draft"})

    def action_borrowed(self):
        self.write({"state": "borrowed"})

    def action_returned(self):
        self.write({"state": "returned"})

    """ we can implement write method like this

     def write(self, vals):
          vals["state"] = "lost"
         return super(ReadersDetail, self).write(vals)"""

    @api.onchange("reader_ids")
    def _onchange_borrowed_books(self):
        """created the onchange decorator to check wheather a reader is member of library or not #T00316"""
        for rec in self:

            rec.is_reader = True if rec.reader_ids else False

    @api.constrains("phone")
    def _check_mobile_no(self):
        """created constrains for mobile no to get valid mobile no #T00316"""
        for record in self:
            if len(record.phone) > 15 or len(record.phone) < 10:

                raise ValidationError("Invalid contact no %s" % record.phone)

    @api.depends("reader_ids")
    def _count_book(self):
        """created count book compute method to get count of total borrowed books #T00316"""
        for book in self:
            book.total_borrowed_book = len(book.reader_ids)

    def _count_books(self):
        """created count books compute method to get count of total library books #T00316"""
        count = 0
        ids = self.env["books.detail"].search([])
        for id in ids:
            count += 1
        self.count = count

    @api.model
    def create(self, vals):
        """created sequence model for readers #T00316"""
        vals["reader_seq"] = self.env["ir.sequence"].next_by_code("readers.detail")
        return super(ReadersDetail, self).create(vals)
