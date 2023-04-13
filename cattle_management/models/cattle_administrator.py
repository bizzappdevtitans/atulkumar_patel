from odoo import models, fields


class CattleAdministrator(models.Model):
    """Created this model for adding Administrator Detail #T00316"""

    _name = "cattle.administrator"
    _description = "Administrator Detail"

    name = fields.Char(string="Admin Name", required=True)
    administrator_id = fields.Char(string="Admin Id", readonly=True)
    email = fields.Char(string="Admin Email", required=True)
    password = fields.Char(required=True)
    permissions = fields.Selection(
        [
            ("read", "Read"),
            ("read_write", "Read and Write"),
            ("read_write_delete", "Read,write and Delete"),
        ],
        required=True,
        default="read_write",
    )
