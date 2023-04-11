from odoo import models, fields


class MrpProduction(models.Model):
    """Inherit Manufacturing Orders #T00316"""

    _inherit = "mrp.production"
    _description = "Production Order"

    mrp_description = fields.Char(string="Manufacturing Description")
