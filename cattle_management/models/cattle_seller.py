from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CattleSeller(models.Model):
    """Created this model for adding Seller Detail #T00316"""

    _name = "cattle.seller"
    _description = "Seller Detail"

    name = fields.Char(string="Seller Name", required=True)
    seller_id = fields.Char(string="Seller Id", readonly=True)
    contact = fields.Char(string="Seller Contact", required=True)
    email = fields.Char(string="Seller Email", required=True)
    address = fields.Text(string="Seller Address")
    cattle_ids = fields.One2many("cattle.detail", "seller_id", string="Cattle")
    sale_order_ids = fields.One2many(
        "sale.order",
        "seller_id",
        string="Sale Orders",
        domain=[("state", "=", "sale")],
    )

    def create_sale_order(self):
        sale_order = self.env["sale.order"]
        for seller in self:
            for cattle in seller.cattle_ids:
                sale_order.create(
                    {
                        "partner_id": seller.id,
                        "partner_invoice_id": seller.id,
                        "partner_shipping_id": seller.id,
                        "order_line": [
                            (
                                0,
                                0,
                                {
                                    "product_id": cattle.cattle_id.id,
                                    "name": cattle.cattle_name,
                                    "price_unit": cattle.cattle_price,
                                    "product_uom_qty": 1,
                                },
                            )
                        ],
                    }
                )

    # created this model to generate sequence no
    @api.model
    def create(self, vals):
        vals["seller_id"] = self.env["ir.sequence"].next_by_code("cattle.seller")
        return super(CattleSeller, self).create(vals)

    @api.constrains("contact")
    def _check_mobile_no(self):
        """this method is to set valid mobile no"""
        for record in self:
            if len(record.contact) > 15 or len(record.contact) < 10:
                raise ValidationError("Invalid mobile_number %s" % record.contact)
