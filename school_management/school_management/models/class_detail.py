from odoo import models, fields, api


# created this model to get and set class detail
class ClassDetail(models.Model):
    _name = "class.detail"
    _description = "class detail"

    name = fields.Char(string="Class Name", required=True)
    class_seq = fields.Char(readonly=True)
    code = fields.Char(string="Code")
    teachers_id = fields.Many2one("teachers.detail", string="Teacher")

    course_id = fields.Many2one("course.detail", string="course")
    student_id = fields.Many2many("student.detail", string="Students")

    # this model is for generating sequence no
    @api.model
    def create(self, vals):
        vals["class_seq"] = self.env["ir.sequence"].next_by_code(
            "class.detail"
        )
        return super(ClassDetail, self).create(vals)
