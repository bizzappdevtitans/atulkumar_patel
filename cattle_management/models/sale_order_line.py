from odoo import models, fields


class SaleOrderLine(models.Model):
    """inherit sale order model #T00316"""

    _inherit = "sale.order.line"
    _description = "sale cattle module"

    cattle_age = fields.Integer(string="Cattle Age in Year")
    cattle_weight = fields.Float(string="Cattle Weight")

    cattle_breed = fields.Char(string="Cattle Breed", required=True)
    cattle_colour = fields.Char(string="Cattle Colour", required=True)
    cattle_gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Cattle Gender",
        default="male",
    )
