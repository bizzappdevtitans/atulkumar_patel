from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CattleBuyer(models.Model):
    """Created this model for adding Buyer Detail #T00316"""

    _name = "cattle.buyer"
    _description = "Buyer Detail"

    name = fields.Char(string="Buyer Name", required=True)
    buyer_id = fields.Char(string="Buyer Id", readonly=True)
    contact = fields.Char(string="Buyer Contact", required=True)
    email = fields.Char(string="Buyer Email", required=True)
    address = fields.Text(string="Buyer Address")

    payment_ids = fields.One2many("cattle.payment", "buyer_id")

    # created this model to generate sequence no
    @api.model
    def create(self, vals):
        vals["buyer_id"] = self.env["ir.sequence"].next_by_code("cattle.buyer")
        return super(CattleBuyer, self).create(vals)

    @api.constrains("contact")
    def _check_mobile_no(self):
        """this method is to set valid mobile no"""
        for record in self:
            if len(record.contact) > 15 or len(record.contact) < 10:
                raise ValidationError("Invalid mobile_number %s" % record.contact)
