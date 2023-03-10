from odoo import models, fields, api


class LibraryManagement(models.Model):
    _name = "library.management"
    _description = "Library management system"

    name = fields.Char(string="Library Name")



