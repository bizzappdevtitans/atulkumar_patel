from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TeachersDetail(models.Model):
    _name = "teachers.detail"
    _description = "school"
    teacher_id = fields.Integer(string="Teacher_id")
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    teacher_dob = fields.Date(string="Date of Birth")
    teacher_gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
    )
    mobile_number = fields.Char(String="mobile number")
    e_mail = fields.Char(String="email")
    student_id = fields.Many2one("student.detail")
    course_id = fields.Many2many("course.detail", string="course id")
    teacher_stream = fields.Char(string="Teachers Stream")
    students_count = fields.Char(compute="compute_count")
    student = fields.Char(compute="get_students")

    # inverse fields
    @api.constrains("age")
    def _check_age(self):
        print("\n\n\n ageageage \n\n\n")
        for record in self:
            if record.age < 0:
                raise ValidationError("Invalid age %s" % record.age)

    # @api.constrains("mobile_number")
    # def _check_mobile_no(self):
    #     for record in self:
    #         if len(record.mobile_number) > 15 or len(record.mobile_number) < 6:

    #             raise ValidationError("Invalid mobile_number %s" % record.mobile_number)

    def compute_count(self):
        for record in self:
            record.students_count = self.env["student.detail"].search_count(
                [("teacher", "=", self.ids)]
            )

    def get_students(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Student",
            "view_mode": "tree",
            "res_model": "student.detail",
            "domain": [("teacher", "=", self.id)],
            "context": "{'create': False}",
        }
