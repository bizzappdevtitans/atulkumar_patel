from odoo import models, fields, api


# created this class to get and set school detail
class SchoolDetail(models.Model):
    _name = "school.detail"
    _description = "school"

    name = fields.Char(string="Name", required=True)
    school_seq = fields.Char(readonly=True)
    principle = fields.Char(string="Principle Name")
    address = fields.Text(string="School Address")
    contact = fields.Char(string="Contact NO")
    email = fields.Char(string="Email")
    image = fields.Binary(string="cover")
    active = fields.Boolean(string="Active?")

    # this decorator is for generating sequence no
    @api.model
    def create(self, vals):
        vals["school_seq"] = self.env["ir.sequence"].next_by_code("school.detail")
        return super(SchoolDetail, self).create(vals)
