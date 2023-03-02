from odoo import models, fields, api


class SchoolDetail(models.Model):
    _name = "school.detail"
    _description = "school"

    name = fields.Char(string="Name", required=True)
    principle = fields.Char(string="Principle Name")
    address = fields.Text(string='School Address')
    contact = fields.Char(string='Contact NO')
