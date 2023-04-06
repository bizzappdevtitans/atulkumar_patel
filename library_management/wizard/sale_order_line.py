from odoo import models, fields, api

class SaleOrderLine(models.Model):
    ''' inherit sale order model #T00316'''

    _inherit = "sale.order.line"
    _description = "sale inheritance"

 