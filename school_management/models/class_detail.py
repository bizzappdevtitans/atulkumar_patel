from odoo import models, fields, api


class ClassDetail(models.Model):
    _name = "class.detail"
    _description = "class detail"

    name = fields.Char(string="Class Name", required=True)
    code = fields.Char(string="Code")
    teachers_id = fields.Many2one("teachers.detail", string="Teacher")

    course_id = fields.Many2one("course.detail", string="course")
    student_id = fields.Many2many("student.detail", string="Students")
