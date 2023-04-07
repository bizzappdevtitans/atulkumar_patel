from odoo import models, fields


class SaleOrder(models.Model):
    """inherit sale order model #T00316"""

    _inherit = "sale.order"
    _description = "sale inheritance"

    # T00316 this field is for account move invoice
    invoice_description = fields.Text(string="Invoice Description")

    # T00316 this field is for stock picking
    delivery_description = fields.Text(string="Delivery Description")

    # T00316 this field is for sale order line one2many field
    sale_data = fields.Float(string="Sale Data")

    # T00316 this field is for mrp production
    mrp_text = fields.Char(string="Manufacturing Text")

    # T00316 this field is for project_project model
    project_text = fields.Text(string="Project Text")

    # T00316 this field is for project task model
    task_text = fields.Text(string="Task Text")

    introduction_id = fields.Many2one("introduction.text")
    closing_id = fields.Many2one("closing.text")

    def _prepare_invoice(self):
        """this method will generate a regular invoice #T00316"""
        res = super(SaleOrder, self)._prepare_invoice()
        res["invoice_text"] = self.invoice_description
        return res
