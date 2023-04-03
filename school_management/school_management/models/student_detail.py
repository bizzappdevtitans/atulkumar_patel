from odoo import models, fields, api

from odoo.exceptions import ValidationError, UserError


class StudentDetail(models.Model):
    """created this class to get and set student detail"""

    _name = "student.detail"
    _description = "school"

    name = fields.Char(string="Name", required=True)
    roll_no = fields.Integer(string="Roll No")
    student_seq = fields.Char(readonly=True)
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

    mobile_number = fields.Char(string="mobile number", required=True)
    e_mail = fields.Char(string="Email")

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
        string="State",
    )

    course_id = fields.Many2many("course.detail", string="course")

    teacher = fields.Many2many("teachers.detail")

    transportation = fields.Many2one("transportation.detail")

    fee_detail = fields.One2many("fees.detail", "fees", string="fees")

    students_count = fields.Integer(compute="compute_count")

    def name_get(self):
        """created name_get method to concatnate two fields"""
        result = []

        for rec in self:

            result.append((rec.id, "%s - %s" % (rec.student_seq, rec.name)))

        return result

    @api.model
    def _name_search(
        self, name="", args=None, operator="ilike", limit=100, name_get_uid=None
    ):

        """name_search method to search records"""
        args = list(args or [])
        if name:
            args += [
                "|",
                "|",
                ("name", operator, name),
                ("e_mail", operator, name),
                ("mobile_number", operator, name),
            ]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)

    @api.constrains("mobile_number")
    def _check_mobile_no(self):
        """this method is to set valid mobile no"""
        for record in self:
            if len(record.mobile_number) > 15 or len(record.mobile_number) < 6:
                raise ValidationError("Invalid mobile_number %s" % record.mobile_number)

    # this decorator is for setting sequence no
    @api.model
    def create(self, vals):
        vals["student_seq"] = self.env["ir.sequence"].next_by_code("student.detail")
        return super(StudentDetail, self).create(vals)

        # write method to update the data

    def write(self, vals):

        return super(StudentDetail, self).write(vals)

    def unlink(self):
        """unlink method to delete the data"""
        for student in self:
            if student.state != "initial_state":
                raise UserError("you can delete state only in initial state")

        return super(StudentDetail, self).unlink()

    @api.model
    def default_get(self, fields):
        """default get method to set value"""
        res = super(StudentDetail, self).default_get(fields)
        print("\n\n\n\n\n\n\n\n fields: ", fields)
        print("\n\n\n\n\n\n\n\n res=: ", res)
        res["gender"] = "male"
        print("\n\n\n\n\n\n\n\n res=: ", res, "\n\n\n\n")
        return res
