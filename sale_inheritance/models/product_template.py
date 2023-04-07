from odoo import models, fields


class product_template(models.Model):
    _inherit = "product.template"

    purchase_line_ids = fields.One2many("purchase.order.line", "product_template_id")
