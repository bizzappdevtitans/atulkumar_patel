from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ClosingText(models.Model):
    """created Closingtext model #T00316"""

    _name = "closing.text"
    _description = "closing text class"

    name = fields.Char(string="Name", required="1")
    closing_seq = fields.Char(readonly=True)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        default="male",
    )
    age = fields.Integer(string="Age")
    contact = fields.Char(string="Contact")
    address = fields.Text(string="Address")
    closing_text = fields.Text(string="Closing Text")

    @api.constrains("contact")
    def _check_mobile_no(self):
        """created constrains for mobile no to get valid mobile no #T00316"""
        for record in self:
            if len(record.contact) > 15 or len(record.contact) < 10:
                raise ValidationError("Invalid contact no %s" % record.contact)

    @api.model
    def create(self, vals):
        """created sequence for closing model  #T00316"""
        vals["closing_seq"] = self.env["ir.sequence"].next_by_code("closing.text")
        return super(ClosingText, self).create(vals)
