from odoo import models, fields, api


class CattleMilk(models.Model):
    """ This model will show the cattle milk related detail #T00316"""
    _name = "cattle.milk"
    _description = "cattle milk management"
    _rec_name = "cattle_id"

    cattle_id = fields.Many2one("cattle.detail", required=True)
    start_milking_date = fields.Date("Start Milking Date", required=True)
    last_milking_date = fields.Date("Last Milking Date", required=True)
    milk_yield = fields.Float("Milk Yield(L)", required=True)
    average_milk_yield = fields.Float(
        string="Average Milk Yield(L/Day)", compute="_compute_average_milk_yield"
    )
    total_days = fields.Integer(string="Total Milking Days")

    @api.depends("cattle_id", "milk_yield", "start_milking_date", "last_milking_date")
    def _compute_average_milk_yield(self):
        """ This method will compute average milk of a cattle #T00316 """
        for record in self:
            if (
                record.start_milking_date
                and record.last_milking_date
                and record.milk_yield
            ):
                delta = record.last_milking_date - record.start_milking_date
                total_days = delta.days
                record.average_milk_yield = record.milk_yield / total_days
                record.total_days = total_days
            else:
                record.average_milk_yield = 0
