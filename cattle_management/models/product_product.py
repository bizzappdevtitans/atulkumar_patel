from odoo import models, fields


class ProductProduct(models.Model):
    """Inherited Product.Product model #T00316"""

    _inherit = "product.product"
    _description = "product module"

    cattle_breed = fields.Char(string="Cattle Breed")
    cattle_colour = fields.Char(string="Cattle Colour")
    cattle_weight = fields.Float(string="Cattle Weight")
    cattle_age = fields.Integer(string="Cattle Age")
