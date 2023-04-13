from odoo import models, fields


class SaleOrderLine(models.Model):
    """inherit sale order model #T00316"""

    _inherit = "sale.order.line"
    _description = "sale inheritance"

    new_cattle_id = fields.Many2one("cattle.detail")
