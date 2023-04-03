from odoo import models, fields, api


# created this class to get and set transportaion detail
class TransportationDetail(models.Model):
    _name = "transportation.detail"
    _description = "school"
    _rec_name = "transportation_type"

    transportation_type = fields.Char(string="Transportation Name")
    trans_seq = fields.Char(readonly=True)
    vehicle_no = fields.Integer(string="Vehicle No")
    driver_name = fields.Char(string="Driver Name")

    transportation_fare = fields.Char(string="Transportation Fare")

# this model is for generating sequence no
    @api.model
    def create(self, vals):
        vals["trans_seq"] = self.env["ir.sequence"].next_by_code(
            "transportation.detail"
        )
        return super(TransportationDetail, self).create(vals)
