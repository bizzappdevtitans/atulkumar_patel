from odoo import models, fields, api

class AccountMove(models.Model):
    '''Inherit account move model #T00316'''	

    _inherit = "account.move"
    _description = "sale inheritance account move"

    invoice_text = fields.Text(string="Invoice Description")
