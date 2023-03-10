from odoo import models, fields, api


class ReadersDetail(models.Model):
    _name = "readers.detail"
    _description = "readers management system"

    name = fields.Char(string="Reader Name")
