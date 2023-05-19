from odoo import models, fields, api
from datetime import datetime


class CattlePayment(models.Model):
    """Created this model for adding Payment Detail #T00316"""

    _name = "cattle.payment"
    _description = "Payment Detail"
    _rec_name = "buyer_id"

    payment_id = fields.Char(string="Payment Id", readonly=True)
    date = fields.Date(string="Payment Date", default=datetime.today())
    buyer_id = fields.Many2one("cattle.buyer", required=True)
    seller_id = fields.Many2one("cattle.seller", string="Seller")
    cattle_ids = fields.Many2many("cattle.detail", string="Cattle")
    amount = fields.Float(compute="_amount_total", string="SubTotal")
    status = fields.Selection(
        [
            ("draft", "Draft"),
            ("pending", "Pending"),
            ("confirm", "Confirm"),
        ],
        default="draft",
        string="State",
    )

    def _amount_total(self):
        """
        Compute the total amounts of the cattle #T00316
        """
        total = 0.0
        for count in self.cattle_ids:
            total += count.cattle_price
        self.amount = total

    # created this model to generate sequence no #T00316

    @api.model
    def create(self, vals):
        vals["payment_id"] = self.env["ir.sequence"].next_by_code("cattle.payment")
        return super(CattlePayment, self).create(vals)
