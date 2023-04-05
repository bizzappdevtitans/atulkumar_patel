from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    '''Inherit account move model #T00316'''    

    _inherit = "purchase.order.line"
    _description = "sale inheritance account move"

    product_id = fields.Many2one("product.product")

   