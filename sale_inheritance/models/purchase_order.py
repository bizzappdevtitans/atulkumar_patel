from odoo import models


class PurchaseOrder(models.Model):
    """Inherit account move model #T00316"""

    _inherit = "purchase.order"
    _description = "sale inheritance account move"

    def _prepare_purchase_order_line(
        self, product_id, product_qty, product_uom, company_id, supplier, po
    ):

        """ this mehod is for passing purchase order data to product.product model #T00316"""
        res = super(PurchaseOrder, self)._prepare_purchase_order_line(
            product_id, product_qty, product_uom, company_id, supplier, po
        )
        res["product_id"] = product_id
        return res
