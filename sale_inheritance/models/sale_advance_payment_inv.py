from odoo import models, fields, api

class SaleAdvancePaymentInv(models.TransientModel):
    ''' Inherit Sales Advance Payment Invoice model #T00316'''

    _inherit = "sale.advance.payment.inv"
    _description = "Sales Advance Payment Invoice"

    invoice_text = fields.Text(string="Invoice Description")
    invoice_description = fields.Text(string="Invoice Text")

    def _prepare_invoice_values(self, order, name, amount, so_line):
        '''created this method to pass value from sale order to acount move using downpayment invoice #T00316'''
        res = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(order, name, amount, so_line)
        res.update({'invoice_text': order.invoice_description})

	    #T00316 pass value from sale order field to account move field using update method
        return res

