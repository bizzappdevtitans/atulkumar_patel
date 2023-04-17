from odoo import models, fields


class CattleSaleOrderLine(models.Model):
    """created cattle sale order model #T00316"""

    _name = "cattle.sale.order.line"
    _description = "sale cattle module"
    _rec_name = "cattle_id"

    order_id = fields.Many2one("cattle.sale.order", string="Sale Order")
    cattle_id = fields.Many2one("cattle.detail", string="Cattle", required=True)
    price = fields.Float(
        string="Price", related="cattle_id.price", readonly=True
    )
