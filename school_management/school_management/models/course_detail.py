from odoo import models, fields, api


# created this model to get and set course detail
class CourseDetail(models.Model):
    _name = "course.detail"
    _description = "school course"

    name = fields.Char(readonly=True)

    course_name = fields.Char(string="Course Name")
    course_url = fields.Text(string="course url")

    description = fields.Text(string="description")
    fee = fields.Float(string="course fee")
    student_id = fields.Many2many("student.detail", string="Students")

    # this method is for generating sequence no
    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code("course.detail")
        return super(CourseDetail, self).create(vals)
