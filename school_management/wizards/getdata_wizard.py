from odoo import models, fields, api


class GetStudentData(models.TransientModel):
    _name = "getdata.wizard"

    students_id = fields.Many2one("student.detail", string="Student")
