from odoo import models, fields
from odoo.exceptions import UserError


class SaleOrderWizard(models.TransientModel):
    """Created sale order wizard model this will create a sale order in
    library management module #T00316"""

    _name = "sale.order.wizard"
    _description = "sale order wizard"

    partner_id = fields.Many2one("res.partner", string="Customer", required=True)

    order_line = fields.Many2many(
        "sale.order.line", "order_id", string="Sale Line", required=True
    )

    def create_and_view_sale_order(self):
        """T00316 This method is for creating and viewing sale order """
        sale_order = self.env["sale.order"].create(
            {"partner_id": self.partner_id.id, "order_line": self.order_line}
        )
        if sale_order:
            return {
                "name": "Sale Order Created",
                "view_type": "form",
                "view_mode": "form",
                "res_model": "sale.order",
                "type": "ir.actions.act_window",
                "res_id": sale_order.id,
            }
        else:
            raise UserError("Failed to create sale order")

    def create_sale_order(self):
        """T00316 This method will create sale order"""
        self.env["sale.order"].create(
            {"partner_id": self.partner_id.id, "order_line": self.order_line}
        )
        if self._context.get("open_sale_order", False):
            return self.create_and_view_sale_order()
