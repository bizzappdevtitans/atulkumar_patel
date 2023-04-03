from odoo import models, fields, api


# created employee detail model to get and set school employee detail
class EmployeeDetail(models.Model):
    _name = "employee.detail"
    _description = "school"

    name = fields.Char(string="Name")
    emp_id = fields.Integer(string="Empployee Id")
    employee_seq = fields.Char(readonly=True)
    employee_dob = fields.Date(string="Date of Birth")
    employee_gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
    )
    mobile_number = fields.Char(string="mobile number", required=True)
    e_mail = fields.Char(string="email")
    employee_type = fields.Char(string="Employee Type")

    # this method is for generating sequence no
    @api.model
    def create(self, vals):
        vals["employee_seq"] = self.env["ir.sequence"].next_by_code("employee.detail")
        return super(EmployeeDetail, self).create(vals)
