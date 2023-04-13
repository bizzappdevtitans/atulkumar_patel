from odoo import models, fields


class PurchaseOrder(models.Model):
    """inherit sale order model #T00316"""

    _inherit = "purchase.order"
    _description = "sale inheritance"

    buyer_id = fields.Many2one("cattle.buyer")
    cattle_ids = fields.Many2many("cattle.detail", string="Cattle")

    def action_confirm(self):
        res = super(PurchaseOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                order.cattle_ids |= line.cattle_id
        return res
