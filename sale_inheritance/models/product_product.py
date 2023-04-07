from odoo import models, fields, api


class ProductProduct(models.Model):
    """Inherit account move model #T00316"""

    _inherit = "product.product"
    _description = "sale inheritance account move"

    product_ids = fields.One2many(
        "purchase.order.line",
        "product_id",
        string="Last Five Products For purchase order",
        compute="_compute_purchase_order",
    )
    sale_product_ids = fields.One2many(
        "sale.order.line",
        "sale_product_id",
        string="Last Five Products For sale order",
        compute="_compute_sale_order",
    )

    @api.depends("product_ids")
    def _compute_purchase_order(self):
        """ this method is for computing product_ids #T00316"""
        for product in self:
            product.product_ids = self.env["purchase.order.line"].search(
                [("product_id", "=", product.id)],
                order="id DESC",
                limit=5,
            )

    @api.depends("sale_product_ids")
    def _compute_sale_order(self):
        """ this method is for computing sale_product_ids #T00316"""
        for product in self:
            product.sale_product_ids = self.env["sale.order.line"].search(
                [("product_id", "=", product.id)], order="id DESC", limit=5
            )
