from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class RegistrationDetail(models.Model):
    """Created this model for adding Registration Detail #T00316"""

    _name = "registration.detail"
    _description = "Registration Detail"

    name = fields.Char(string="Register Name", required=True)
    register_id = fields.Char(string="Register Id", readonly=True)
    contact = fields.Char(string="Register Contact", required=True)
    date = fields.Date(string="Registration Date", default=datetime.today())
    email = fields.Char(string="Register Email", required=True)
    address = fields.Text(string="Register Address")
    is_seller = fields.Boolean(default=False)
    is_buyer = fields.Boolean(default=False)

    # created this model to generate sequence no
    @api.model
    def create(self, vals):
        vals["register_id"] = self.env["ir.sequence"].next_by_code(
            "registration.detail"
        )
        return super(RegistrationDetail, self).create(vals)

    @api.constrains("contact")
    def _check_mobile_no(self):
        """this method is to set valid mobile no"""
        for record in self:
            if len(record.contact) > 15 or len(record.contact) < 10:
                raise ValidationError("Invalid mobile_number %s" % record.contact)
