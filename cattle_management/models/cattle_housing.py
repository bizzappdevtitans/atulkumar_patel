from odoo import models, fields, api
from datetime import date


class CattleHousing(models.Model):
    """ This model will show the cattle housing related detail #T00316"""
    _name = "cattle.housing"
    _description = "cattle housing management"
    _rec_name = "cattle_id"

    cattle_id = fields.Many2one("cattle.detail", required=True)
    housing_area = fields.Char("Housing Area", required=True)
    start_date = fields.Date("Start Date", required=True)
    end_date = fields.Date("End Date")
    duration = fields.Integer(string="Duration(Days)", compute="_compute_duration")

    @api.depends("start_date", "end_date")
    def _compute_duration(self):
        """This method will compute duration of a cattle in housing area #T00316"""
        for record in self:
            if record.start_date and record.end_date:
                delta = record.end_date - record.start_date
                record.duration = delta.days
            elif record.start_date:
                delta = date.today() - record.start_date
                record.duration = delta.days
            else:
                record.duration = 0
