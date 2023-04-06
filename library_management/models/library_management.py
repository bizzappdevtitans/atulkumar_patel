from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryManagement(models.Model):
    """created library management model to get library related information #T00316"""

    _name = "library.management"
    _description = "Library management"

    name = fields.Char()
    library_seq = fields.Char(readonly=True)
    address = fields.Text()
    contact = fields.Char()
    email = fields.Char()

    @api.constrains("contact")
    def _check_mobile_no(self):
        '''created constrains for mobile number to get valid mobile number #T00316'''
        for record in self:
            if len(record.contact) > 15 or len(record.contact) < 6:

                raise ValidationError("Invalid mobile_number %s" % record.contact)

    @api.model
    def create(self, vals):
        '''created sequence model for Library management main menu #T00316'''
        vals["library_seq"] = self.env["ir.sequence"].next_by_code("library.management")
        return super(LibraryManagement, self).create(vals)
