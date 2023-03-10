from odoo import models, fields, api
from datetime import datetime


class AttendanceDetail(models.Model):
    _name = "attendance.detail"
    _description = "school attendance detail"

    name = fields.Char(string="Class Name")

    student = fields.Many2one("student.detail", string="Student")
    class_id = fields.Many2one("class.detail", string="Class")
    roll_no = fields.Integer(string="Roll No")
    note = fields.Text(string="description")
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        string="Gender",
    )

    status = fields.Selection(
        [
            ("present", "Present"),
            ("absent", "Absent"),
        ],
        string="Status",
    )
    date_field = fields.Date(string="Date", default=datetime.today())
    mobile_number = fields.Char(String="Mobile number")
    e_mail = fields.Char(String="Email")

    # api.decorators
    @api.onchange("student")
    def onchange_student_id(self):
        print("\n\n\nonchange student field\n\n\n")
        for rec in self:
            if rec.student:
                if not rec.student.gender:
                    rec.gender = ""

            rec.gender = rec.student.gender


"""

  if self.student:
            if self.student.gender:
                self.gender = self.student.gender

            else:
                self.gender = ""
"""
