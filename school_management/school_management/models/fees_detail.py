from odoo import models, fields, api


from odoo.exceptions import ValidationError


# created fees detail model to get and set student fees detail
class FeesDetail(models.Model):
    _name = "fees.detail"
    _description = "school"

    name = fields.Char(string="Name")
    fee_seq = fields.Char(readonly=True)
    tution_fee = fields.Float(string="Tution fee", required=True)
    book_uniform_cost = fields.Float(string="Book & Uniform fee", required=True)
    activity_fee = fields.Float(string="Activity Fee", required=True)
    total_fee = fields.Float(string="Total fee", store=True, compute="_calculate_fee")

    roll_no = fields.Integer(string="Roll No")
    student_class = fields.Char(string="Class")
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
    student_fees_detail = fields.Char(string="student fees detail")
    fees = fields.Many2one("student.detail")

    # created this decorator to get valid fee
    @api.constrains("tution_fee")
    def _check_something(self):
        for record in self:
            if record.tution_fee < 0:
                raise ValidationError("Fee Amount cannot be negative")

    # created this decorator to calculate total fee of student
    @api.depends("tution_fee", "book_uniform_cost", "activity_fee")
    def _calculate_fee(self):
        for record in self:
            if record.tution_fee and record.book_uniform_cost and record.activity_fee:
                record.total_fee = (
                    record.tution_fee + record.book_uniform_cost + record.activity_fee
                )

    # this decorator  is to set valid mobile no
    @api.constrains("mobile_number")
    def _check_mobile_no(self):
        for record in self:
            if len(record.mobile_number) > 15 or len(record.mobile_number) < 6:

                raise ValidationError("Invalid mobile_number %s" % record.mobile_number)

    # this decorator is for generating sequence no
    @api.model
    def create(self, vals):
        vals["fee_seq"] = self.env["ir.sequence"].next_by_code("fees.detail")
        return super(FeesDetail, self).create(vals)
