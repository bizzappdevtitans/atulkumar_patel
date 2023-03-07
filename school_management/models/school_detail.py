from odoo import models, fields, api


class SchoolDetail(models.Model):
    _name = "school.detail"
    _description = "school"

    name = fields.Char(string="Name", required=True)
    principle = fields.Char(string="Principle Name")
    address = fields.Text(string='School Address')
    contact = fields.Char(string='Contact NO')
    email = fields.Char(string='Email')
    image = fields.Binary(string='cover')
    active = fields.Boolean(string="Active?")
    refers_to = fields.Reference(
        [('student.detail', 'name'), ('teachers.detail', 'name')],
        string='Refers to')
