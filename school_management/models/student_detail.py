from odoo import models, fields, api

from odoo.exceptions import ValidationError


class StudentDetail(models.Model):
    _name = "student.detail"
    _description = "school"

    name = fields.Char(string="Name", required=True)
    roll_no = fields.Integer(string="Roll No")

    fathers_name = fields.Char(string="Father's Name")
    student_dob = fields.Date(string="Date of Birth")
    student_class = fields.Char(string="Class")
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        string="Gender",
    )

    # gender = fields.Selection(selection_add=[("transgender", "Transgender")])
    mobile_number = fields.Char(String="mobile number", required=True)
    e_mail = fields.Char(String="Email")

    student_stream = fields.Selection(
        [
            ("science", "Science Stream"),
            ("art", "Art stream"),
        ],
        string="Stream",
    )

    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", " high"), ("3", "very high")],
        string="Status",
        default="1",
    )

    state = fields.Selection(
        [
            ("initial_state", "Initial state"),
            ("inprogress", "Inprogress"),
            ("done", "Done"),
            ("cancel", "Cancel"),
        ],
        default="initial_state",
        string="Status",
    )
    course_id = fields.Many2many("course.detail", string="course")
    teacher = fields.Many2many("teachers.detail")

    transportation = fields.Many2one("transportation.detail")

    fee_detail = fields.One2many("fees.detail", "fees", string="fees")

    students_count = fields.Integer(compute="compute_count")

    @api.constrains("mobile_number")
    def _check_mobile_no(self):
        for record in self:
            if len(record.mobile_number) > 15 or len(record.mobile_number) < 6:
                raise ValidationError("Invalid mobile_number %s" % record.mobile_number)
