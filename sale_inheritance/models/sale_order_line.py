from odoo import models, fields, api

class SaleOrderLine(models.Model):
    ''' inherit sale order model #T00316'''

    _inherit = "sale.order.line"
    _description = "sale inheritance"

    sale_data = fields.Float(string="Sale Data")
    sale_product_id = fields.Many2one("product.product")


    def _timesheet_create_project_prepare_values(self):
        vals = super(SaleOrderLine, self)._timesheet_create_project_prepare_values()
        print("\n\n\n",vals,"\n\n\n")
        vals["project_description"] = self.order_id.project_text
        print("\n\n project vals:",vals,"\n\n")
        return vals
       


    def _timesheet_create_task_prepare_values(self, project):
        vals = super(SaleOrderLine, self)._timesheet_create_task_prepare_values(project)
        print(vals)
        vals["task_description"] = self.order_id.task_text
        print("\n\n task vals:",vals,"\n\n")
        return vals

    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        print("\n\n", res,"\n\n after")
        return res