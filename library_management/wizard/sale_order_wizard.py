from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrderWizard(models.TransientModel):
    """ created sale order wizard model this will create a sale order in library management module #T00316"""

    _name = "sale.order.wizard"
    _description = "student wizard"

    partner_id = fields.Many2one("res.partner", string="Customer",required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    order_id = fields.Many2one('sale.order', string='Sale Order', required=True, ondelete='cascade')
    sale_line_ids = fields.One2many("sale.order.line","order_id", string="Sale Line")
    qty = fields.Float(string="Quantity",default= '1.0')
    date_order = fields.Datetime(string='Order Date',index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now, help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.")

    def create_sale_orders(self):
        # T00316 This method will create sale order
        sale_order = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            'sale_line_ids': [(0,0,{
                'product_id':self.product_id.id,
                'product_uom_qty':self.qty,
                })]
            })

    def create_sale_order(self):
        # T00316 This method is for creating and viewing sale order
        sale_order = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            'sale_line_ids': [(0,0,{
                'product_id':self.product_id.id,
                'product_uom_qty':self.qty,
                })]
            })
        if sale_order:
            return{
            'name':'Sale Order Created',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sale.order',
            'type':'ir.actions.act_window',
            'res_id':sale_order.id,
            }
        else:
            raise UserError('Failed to create sale order')

    def action_cancel(self):
        # T00316 This method will cancel wizard
        cancel_warning = self._show_cancel_wizard()
        if cancel_warning:
            return {
                'name': _('Cancel Sales Order'),
                'view_mode': 'form',
                'res_model': 'sale.order.cancel',
                'view_id': self.env.ref('sale.sale_order_cancel_view_form').id,
                'type': 'ir.actions.act_window',
                'context': {'default_order_id': self.id},
                'target': 'new'
            }
        return self._action_cancel()

    
    def action_cancel(self):
        return self.order_id.with_context({'disable_cancel_warning': True}).action_cancel()