from odoo import models, fields, api

class SaleOrder(models.Model):
    ''' inherit sale order model #T00316'''
    
    _inherit = "sale.order"
    _description = "sale inheritance"
    
    sale_line_ids = fields.One2many("sale.order.line","order_id", string="Sale Line")