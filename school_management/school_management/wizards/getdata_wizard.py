from odoo import models, fields, api


class GetStudentData(models.TransientModel):
    _name = "getdata.wizard"
    _description = "student wizard"

    students_id = fields.Many2one("student.detail", string="Student id")
