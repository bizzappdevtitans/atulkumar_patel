from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CattleAdministrator(models.Model):
    """Created this model for adding Cattle Admin #T00316"""

    _name = "cattle.administrator"
    _description = "Cattle Admin"

    admin_seq = fields.Char(string="Admin id", readonly=True)
    name = fields.Char(string="Name", required=True)
    address = fields.Text(string="Address")
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        default="male",
    )

    mobile_number = fields.Char(string="mobile number", required=True)
    e_mail = fields.Char(string="Email")

    @api.constrains("mobile_number")
    def _check_mobile_no(self):
        """this method is to set valid mobile no"""
        for record in self:
            if len(record.mobile_number) > 15 or len(record.mobile_number) < 10:
                raise ValidationError("Invalid mobile_number %s" % record.mobile_number)

    @api.model
    def create(self, vals):
        """created this method to generate sequence no #T00316"""
        vals["admin_seq"] = self.env["ir.sequence"].next_by_code("cattle.administrator")
        return super(CattleAdministrator, self).create(vals)
