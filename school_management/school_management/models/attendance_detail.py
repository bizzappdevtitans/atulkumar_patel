from odoo import models, fields, api
from datetime import datetime


# created school attendance detail model
class AttendanceDetail(models.Model):

    _name = "attendance.detail"
    _description = "school attendance detail"

    name = fields.Char(string="Class Name")
    attendance_seq = fields.Char(readonly=True)
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
    mobile_number = fields.Char(string="Mobile number")
    e_mail = fields.Char(string="Email")

    # created onchange api.decorator to select gender
    @api.onchange("student")
    def onchange_student_id(self):
        for rec in self:
            if rec.student:
                if not rec.student.gender:
                    rec.gender = ""

            rec.gender = rec.student.gender

    # created this model to generate sequence no
    @api.model
    def create(self, vals):
        vals["attendance_seq"] = self.env["ir.sequence"].next_by_code(
            "attendance.detail"
        )
        return super(AttendanceDetail, self).create(vals)

    @api.onchange("gender")
    def onchange_gender(self):
        '''created browse method to browse recordset of gender = male #T00316'''
        lines = self.env["student.detail"].search([("gender", "=", "male")])
        data = self.env["attendance.detail"].browse(lines)
        print("\n\n\n\n\n", data)


"""

  if self.student:
            if self.student.gender:
                self.gender = self.student.gender

            else:
                self.gender = ""
"""
