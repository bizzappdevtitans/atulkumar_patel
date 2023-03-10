from odoo import models, fields, api


class BooksDetail(models.Model):
    _name = "books.detail"
    _description = "books management system"

    name = fields.Char(string="Book Name")


