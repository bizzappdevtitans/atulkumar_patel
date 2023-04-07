from odoo import models, fields


class SaleOrderLine(models.Model):
    """inherit sale order model #T00316"""

    _inherit = "sale.order.line"
    _description = "sale inheritance"

    sale_data = fields.Float(string="Sale Data")
    sale_product_id = fields.Many2one("product.product")

    def _timesheet_create_project_prepare_values(self):
        """this method will pass value from sale order to project.project model #T00316"""
        vals = super(SaleOrderLine, self)._timesheet_create_project_prepare_values()
        vals["project_description"] = self.order_id.project_text
        return vals

    def _timesheet_create_task_prepare_values(self, project):
        """this method will pass value from sale order to project.task model #T00316"""
        vals = super(SaleOrderLine, self)._timesheet_create_task_prepare_values(project)
        vals["task_description"] = self.order_id.task_text
        return vals
