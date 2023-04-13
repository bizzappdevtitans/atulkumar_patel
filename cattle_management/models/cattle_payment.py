from odoo import models, fields, api
from datetime import datetime


class CattlePayment(models.Model):
    """Created this model for adding Payment Detail #T00316"""

    _name = "cattle.payment"
    _description = "Payment Detail"

    payment_id = fields.Char(string="Payment Id", readonly=True)
    name = fields.Char(required=True)
    amount = fields.Float(required=True)
    # register_id = fields.Integer(string="Register Id", required=True)
    date = fields.Date(string="Payment Date", default=datetime.today())
    # transaction_no = fields.Char(string="Transation No", required=True)
    buyer_id = fields.Many2one("cattle.buyer")
    seller_id = fields.Many2one("cattle.seller", string="Seller")
    cattle_id = fields.Many2one("cattle.detail", string="Cattle")
    sale_order_id = fields.Many2one("sale.order", string="Sale order")
    purchase_order_id = fields.Many2one("purchase.order", string="Purchase Order")
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("pending", "Pending"),
            ("confirm", "Confirm"),
        ],
        default="draft",
        string="State",
    )

    # created this model to generate sequence no
    @api.model
    def create(self, vals):
        vals["payment_id"] = self.env["ir.sequence"].next_by_code("cattle.payment")
        return super(CattlePayment, self).create(vals)
