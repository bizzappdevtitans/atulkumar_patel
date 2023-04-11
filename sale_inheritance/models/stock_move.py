from odoo import models, fields


class StockMove(models.Model):
    """inherit stock move model #T00316"""

    _inherit = "stock.move"
    _description = "sale inheritance stock move"

    # this field is for stock picking
    delivery_description = fields.Text(string="Delivery Description")

    # this field is for mrp production
    mrp_text = fields.Char(string="Manufacturing Text")

    def _prepare_procurement_values(self):
        """this method will move value from sale order to stock rule #T00316"""

        val = super(StockMove, self)._prepare_procurement_values()
        val["mrp_text"] = self.group_id.sale_id.mrp_text
        return val

    def _get_new_picking_values(self):
        """created this method to move value from sale order to stock picking #T00316"""

        res = super(StockMove, self)._get_new_picking_values()
        # passed value from sale order field to stock picking field
        res["shipment_text"] = self.group_id.sale_id.delivery_description
        return res
