from odoo import models, fields


class CattleSaleOrder(models.Model):
    """created cattle sale order model #T00316"""

    _name = "cattle.sale.order"
    _description = "sale cattle module"

    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    order_line = fields.One2many(
        "cattle.sale.order.line", "order_id", string="Order Lines"
    )
    state = fields.Selection(
        [("draft", "Draft"), ("confirmed", "Confirmed"), ("invoiced", "Invoiced")],
        string="State",
        default="draft",
    )
    cattle_id = fields.Many2one("cattle.detail", string="Cattle", required=True)

    invoice_id = fields.Many2one("account.move", string="Invoice", readonly=True)

    def create_sale_order(self):
        for record in self.order_line:
            if record.cattle_id.sold:
                raise ValueError("Selected cattle Already sold")
        order_vals = {
            "partner_id": self.partner_id.id,
            "order_line": [
                (
                    0,
                    0,
                    {
                        "product_id": record.id,
                        "name": record.cattle_id.cattle_name,
                        "cattle_age": record.cattle_id.cattle_age,
                        "cattle_weight": record.cattle_id.cattle_weight,
                        "cattle_breed": record.cattle_id.cattle_breed,
                        "cattle_colour": record.cattle_id.cattle_colour,
                        "cattle_gender": record.cattle_id.cattle_gender,
                        "price_unit": record.cattle_id.price,
                    },
                )
                for record in self.order_line
            ],
        }
        sale_order = self.env["sale.order"].create(order_vals)
        sale_order.action_confirm()
        self.write({"state": "confirmed"})
        return {
            "name": "Sale Order",
            "view_mode": "form",
            "res_model": "sale.order",
            "res_id": sale_order.id,
            "type": "ir.actions.act_window",
            "target": "current",
        }

    def action_purchase_cattle(self):
        for cattle in self.order_line:
            purchase_order = self.env["purchase.order"].create(
                {
                    "partner_id": self.partner_id.id,
                    "order_line": [
                        (
                            0,
                            0,
                            {
                                "product_id": cattle.cattle_id.id,
                                "product_qty": 1,
                                "price_unit": cattle.cattle_id.price,
                                "name": cattle.cattle_id.cattle_name,
                            },
                        )
                    ],
                }
            )
            purchase_order.button_confirm()
            picking = self.env["stock.picking"].search(
                [{"origin", "=", purchase_order.name}], limit=1
            )
            if picking:
                picking.action_assign()
                picking.action_done()

    # def create_invoice(self):
    #     invoice_lines = [
    #         (
    #             0,
    #             0,
    #             {
    #                 "product_id": line.cattle_id.id,
    #                 "name": line.cattle_id.cattle_name,
    #                 "quantity": 1,
    #                 "price_unit": line.cattle_id.price,
    #                 "account_id": self.partner_id.property_account_receivable_id.id,
    #             },
    #         )
    #         for line in self.order_line
    #     ]
    #     invoice_vals = {
    #         "partner_id": self.partner_id.id,
    #         "invoice_line_ids": invoice_lines,
    #     }
    #     invoice = self.env["account.move"].create(invoice_vals)
    #     self.write({"state": "invoiced", "invoice_id": invoice.id})
    #     return {
    #         "name": "Invoice",
    #         "view_mode": "form",
    #         "res_model": "account.move",
    #         "res_id": invoice.id,
    #         "type": "ir.actions.act_window",
    #         "target": "current",
    #     }

    # def delivery_order(self):
    #     for record in self.order_line:
    #         delivery = self.env["stock.picking"].create(
    #             {
    #                 "move_ids_without_package": [
    #                     (
    #                         0,
    #                         0,
    #                         {
    #                             "product_id": record.cattle_id.id,
    #                             "product_uom_qty": 1,
    #                             "picking_type_id": 1,
    #                         },
    #                     )
    #                 ],
    #             }
    #         )

    #         return delivery
