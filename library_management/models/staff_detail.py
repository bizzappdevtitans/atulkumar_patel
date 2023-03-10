from odoo import models, fields, api


class StaffDetail(models.Model):
    _name = "staff.detail"
    _description = "staff management system"

    name = fields.Char(string="Staff Name")
