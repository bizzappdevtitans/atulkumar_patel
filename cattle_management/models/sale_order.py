from odoo import models, fields


class SaleOrder(models.Model):
    """inherit sale order model #T00316"""

    _inherit = "sale.order"
    _description = "sale inheritance"

    cattle_ids = fields.Many2many("cattle.detail", string="Cattle")
    seller_id = fields.Many2one("cattle.seller", string="Seller")

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                order.cattle_ids |= line.cattle_id
        return res
