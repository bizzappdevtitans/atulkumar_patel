from odoo import models, fields, api


class CattleDetail(models.Model):
    """Created this model for adding Cattle Detail #T00316"""

    _name = "cattle.detail"
    _description = "Cattle Detail"

    cattle_id = fields.Char(string="Cattle Id", readonly=True)
    cattle_name = fields.Char(string="Cattle Name", required=True)
    cattle_age = fields.Integer(string="Cattle Age in Year")
    cattle_weight = fields.Float(string="Cattle Weight")
    cattle_price = fields.Float(required=True)
    cattle_breed = fields.Char(string="Cattle Breed", required=True)
    cattle_colour = fields.Char(string="Cattle Colour", required=True)
    cattle_image = fields.Image(string="Cattle Image")
    seller_id = fields.Many2one("cattle.seller", string="Seller")
    # product_id = fields.Many2one("product.product", string="Product", required=True)
    sale_order_line_ids = fields.One2many(
        "sale.order.line", "new_cattle_id", string="Sale Order Line"
    )
    purchase_order_line_ids = fields.One2many(
        "purchase.order.line", "new_cattle_id", string="Purchase Order Line"
    )
    cattle_gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Cattle Gender",
        default="male",
    )

    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", " high"), ("3", "very high")],
        string="Status",
        default="1",
    )

    @api.model
    def create(self, vals):
        """created this model to generate sequence no #T00316"""
        vals["cattle_id"] = self.env["ir.sequence"].next_by_code("cattle.detail")
        return super(CattleDetail, self).create(vals)

    # @api.onchange("product_id")
    # def onchange_product_id(self):
    #     self.cattle_name = self.product_id.cattle_name
