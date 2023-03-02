from odoo import models, fields, api

from odoo.exceptions import ValidationError


class RgistrationDetail(models.Model):
    _name = "registration.detail"
    _description = "school"

    name = fields.Char(string="New Joiny Name")
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
    mobile_number = fields.Char(String="mobile number")
    e_mail = fields.Char(String="email")
    student_stream = fields.Selection(
        [
            ("science", "Science Stream"),
            ("art", "Art stream"),
        ],
        string="Stream",
    )

    # inverse relation for school model

    # registration_inverse_field = fields.Many2one(
    #     "school.detail", string="Inverse_school"
    # )

    @api.constrains("mobile_number")
    def _check_mobile_no(self):
        for record in self:
            if len(record.mobile_number) > 15 or len(record.mobile_number) < 6:

                raise ValidationError("Invalid mobile_number %s" % record.mobile_number)
