from odoo import models, fields


class StockPicking(models.Model):
    """inherit stock picking model #T00316"""

    _inherit = "stock.picking"
    _description = "sale inheritance stock picking"

    shipment_text = fields.Text(string="Shipment Text")
