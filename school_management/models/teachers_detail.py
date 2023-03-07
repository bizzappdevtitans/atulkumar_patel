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
    mobile_number = fields.Char(String="mobile number", required=True)
    e_mail = fields.Char(String="email")
    student_id = fields.Many2one("student.detail")
    student_ids = fields.Many2many("student.detail")
    course_id = fields.Many2many("course.detail", string="course id")
    teacher_stream = fields.Char(string="Teachers Stream")
    students_count = fields.Integer(compute="compute_count")
    student = fields.Char(compute="get_students")

    def compute_count(self):
        for record in self:
            record.students_count = self.env["student.detail"].search_count(
                [("teacher", "=", self.ids)]
            )

    def get_students(self):
        for rec in self:
            if rec.students_count == 1:

                return {
                    "res_model": "student.detail",
                    "type": "ir.actions.act_window",
                    "name": "form",
                    "domain": [("id", "=", self.ids)],
                    "view_mode": "tree,form",
                }

            return {
                "type": "ir.actions.act_window",
                "name": "Students",
                "view_mode": "tree",
                "res_model": "student.detail",
                "domain": [("id", "in", self.id)],
                "context": "{'create': True}",
            }

    # student = self.mapped("id")
    # action = self.env["ir.actions.actions"]._for_xml_id(
    #     "school_management.student_detail_view_form"
    # )
    # if self.students_count > 1:
    #     action["domain"] = [("id", "in", self.id)]
    # elif len(self.students_count) == 1:
    #     form_view = [
    #         (self.env.ref("school_management.student_detail_view_form").id, "form")
    #     ]
    #     action["views"] = form_view
    #     action["res_id"] = self.id
    # else:
    #     action = {"type": "ir.actions.act_window_close"}
    # context = {}
    # if len(self) == 1:
    #     context.update(
    #         {
    #             "default_name": self.name,
    #         }
    #     )
    # action["context"] = context
    # return action

    # inverse fields
    @api.constrains("age")
    def _check_age(self):
        print("\n\n\n ageageage \n\n\n")
        for record in self:
            if record.age < 0:
                raise ValidationError("Invalid age %s" % record.age)

    @api.constrains("mobile_number")
    def _check_mobile_no(self):
        for record in self:
            if len(record.mobile_number) > 15 or len(record.mobile_number) < 6:

                raise ValidationError("Invalid mobile_number %s" % record.mobile_number)
