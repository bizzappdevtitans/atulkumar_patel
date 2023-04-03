from odoo import models, fields, api
from odoo.exceptions import ValidationError


# created this class to get and set teacher detail
class TeachersDetail(models.Model):
    _name = "teachers.detail"

    _description = "school"

    teacher_id = fields.Char(string="Teacher_id")
    teacher_seq = fields.Char(readonly=True)
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
    mobile_number = fields.Char(string="mobile number", required=True)
    e_mail = fields.Char(string="email")
    student_id = fields.Many2one("student.detail", string="Student id", default=lambda self: self.env.user,)
    student_ids = fields.Many2many("student.detail", string="Student ids")
    course_id = fields.Many2many("course.detail", string="course id")
    teacher_stream = fields.Char(string="Teachers Stream")
    students_count = fields.Integer(compute="compute_count")
    student = fields.Char(compute="get_students")

    # this computed method counts how many student have been assign to a teacher
    def compute_count(self):
        for record in self:
            record.students_count = self.env["student.detail"].search_count(
                [("teacher", "=", self.ids)]
            )

    # this method is for getting student detail
    def get_students(self):
        if self.students_count == 1:
            student = self.env.ref(
                "school_management_menu_root.student_detail_view_form"
            )

            return {
                "res_model": "student.detail",
                "type": "ir.actions.act_window",
                "name": "Students",
                "view_mode": "form",
                "views": [(student.id, "form")],
                "domain": [("id", "=", self.id)],
            }

        return {
            "type": "ir.actions.act_window",
            "name": "Students",
            "res_model": "student.detail",
            "view_mode": "tree,form",
            "domain": [("id", "=", self.id)],
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

    # this decorator is for setting valid age
    @api.constrains("age")
    def _check_age(self):
        print("\n\n\n ageageage \n\n\n")
        for record in self:
            if record.age < 0:
                raise ValidationError("Invalid age %s" % record.age)

    # this decorator is for setting valid mobile no
    @api.constrains("mobile_number")
    def _check_mobile_no(self):
        for record in self:
            if len(record.mobile_number) > 15 or len(record.mobile_number) < 6:

                raise ValidationError("Invalid mobile_number %s" % record.mobile_number)

    # this model is for generating sequence no
    @api.model
    def create(self, vals):
        vals["teacher_seq"] = self.env["ir.sequence"].next_by_code("teachers.detail")
        return super(TeachersDetail, self).create(vals)



