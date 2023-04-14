from odoo import models, fields


class SaleOrder(models.Model):
    """inherit sale order model #T00316"""

    _inherit = "sale.order"
    _description = "sale cattle module"

    address = fields.Char(string="seller Address")
    seller_name = fields.Char(string="Seller Name")
