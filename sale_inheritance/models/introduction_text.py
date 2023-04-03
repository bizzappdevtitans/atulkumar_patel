from odoo import models, fields, api
from odoo.exceptions import ValidationError

class IntroductionText(models.Model):
    '''created introdution model #T00316'''	

    _name = "introduction.text"
    _description = "introduction text class"

    name = fields.Char(string="Name",required="1")
    intro_seq = fields.Char(readonly=True)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        default="male",
    )
    age = fields.Integer(string="Age")
    contact = fields.Char(string="Contact")
    address = fields.Text(string="Address")
    introduction_text = fields.Text(string="Introduction Text")

    @api.constrains("contact")
    def _check_mobile_no(self):
        """created constrains for mobile no to get valid mobile no #T00316"""
        for record in self:
            if len(record.contact) > 15 or len(record.contact) < 10:

                raise ValidationError("Invalid contact no %s" % record.contact)

    @api.model
    def create(self, vals):
        """created sequence for introduction model  #T00316"""
        vals["intro_seq"] = self.env["ir.sequence"].next_by_code("introduction.text")
        return super(IntroductionText, self).create(vals)
