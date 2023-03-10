from odoo import models, fields, api


class TransportationDetail(models.Model):
    _name = "transportation.detail"
    _description = "school"
    _rec_name = "transportation_type"

    transportation_type = fields.Char(string="Transportation Name")
    vehicle_no = fields.Integer(string="Vehicle No")
    driver_name = fields.Char(string="Driver Name")

    transportation_fare = fields.Char(string="Transportation Fare")

    # inverse relation for school model
