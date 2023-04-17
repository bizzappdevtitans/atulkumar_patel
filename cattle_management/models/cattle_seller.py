from odoo import models, fields, api
from odoo.exceptions import ValidationError
# from odoo.exceptions import UserError


class CattleSeller(models.Model):
    """Created this model for adding Seller Detail #T00316"""

    _name = "cattle.seller"
    _description = "Seller Detail"

    name = fields.Char(string="Seller Name", required=True)
    seller_id = fields.Char(string="Seller Id", readonly=True)
    contact = fields.Char(string="Seller Contact", required=True)
    email = fields.Char(string="Seller Email", required=True)
    address = fields.Text(string="Seller Address")
    cattle_ids = fields.One2many("cattle.detail", "seller_id", string="Cattle")
    total_cattle = fields.Integer(compute="_count_cattle")
    get_cattle = fields.Char(compute="get_cattle")
    # created this model to generate sequence no

    @api.depends("cattle_ids")
    def _count_cattle(self):
        """Created count cattle compute method to get count of
        total cattle related to this seller #T00316"""
        for cattle in self:
            cattle.total_cattle = len(cattle.cattle_ids)

    def get_cattle(self):
        """This method will show cattle detail if there is one cattle then
        it will show form view and if more than one cattle then it
        will show tree view #T00316"""
        if self.total_cattle == 1:
            cattle_form = self.env.ref("cattle_management.cattle_view_form")

            return {
                "name": "cattle",
                "res_model": "cattle.detail",
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "views": [(cattle_form.id, "form")],
                "domain": [("seller_id", "=", self.id)],
            }

        return {
            "name": "cattle",
            "res_model": "cattle.detail",
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "domain": [("seller_id", "=", self.id)],
        }

    @api.model
    def create(self, vals):
        vals["seller_id"] = self.env["ir.sequence"].next_by_code("cattle.seller")
        return super(CattleSeller, self).create(vals)

    @api.constrains("contact")
    def _check_mobile_no(self):
        """this method is to set valid mobile no"""
        for record in self:
            if len(record.contact) > 15 or len(record.contact) < 10:
                raise ValidationError("Invalid mobile_number %s" % record.contact)

