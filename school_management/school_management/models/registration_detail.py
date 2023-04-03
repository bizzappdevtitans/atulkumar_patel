from odoo import models, fields, api

from odoo.exceptions import ValidationError


# created this class for registration of new student
class RegistrationDetail(models.Model):
    _name = "registration.detail"
    _description = "school"

    name = fields.Char(string="New Joiny Name")
    registration_seq = fields.Char(readonly=True)
    fathers_name = fields.Char(string="Father's Name")
    roll_no = fields.Integer(string="Roll No")
    age = fields.Integer(string=" Student Age")
    student_dob = fields.Date(string="Date of Birth")
    student_gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
    )
    mobile_number = fields.Char(string="mobile number", required=True)
    e_mail = fields.Char(string="email")
    student_stream = fields.Selection(
        [
            ("science", "Science Stream"),
            ("art", "Art stream"),
        ],
        string="Stream",
    )

    # this decorator is for setting valid mobile no
    @api.constrains("mobile_number")
    def _check_mobile_no(self):
        for record in self:
            if len(record.mobile_number) > 15 or len(record.mobile_number) < 6:

                raise ValidationError("Invalid mobile_number %s" % record.mobile_number)

    # this decorator generates sequence no
    @api.model
    def create(self, vals):
        vals["registration_seq"] = self.env["ir.sequence"].next_by_code(
            "registration.detail"
        )
        return super(RegistrationDetail, self).create(vals)
