from odoo import models, fields, api


class EmployeeDetail(models.Model):
    _name = "employee.detail"
    _description = "school"

    name = fields.Char(string="Name")
    emp_id = fields.Integer(string="Empployee Id")

    employee_dob = fields.Date(string="Date of Birth")
    employee_gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
    )
    mobile_number = fields.Char(String="mobile number")
    e_mail = fields.Char(String="email")
    employee_type = fields.Char(string="Employee Type")

    # inverse field

    # employee_inverse_field = fields.Many2one("school.detail", string="Inverse_school")
