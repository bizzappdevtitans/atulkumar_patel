from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryManagement(models.Model):
    _name = "library.management"
    _description = "Library management"

    name = fields.Char()
    address = fields.Text()
    contact = fields.Char()
    email = fields.Char()

    @api.constrains("contact")
    def _check_mobile_no(self):
        for record in self:
            if len(record.contact) > 15 or len(record.contact) < 6:

                raise ValidationError("Invalid mobile_number %s" % record.contact)
