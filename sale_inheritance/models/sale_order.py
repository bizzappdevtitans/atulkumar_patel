from odoo import models, fields, api

class SaleOrder(models.Model):
    ''' inherit sale order model #T00316'''
    
    _inherit = "sale.order"
    _description = "sale inheritance"
    
    invoice_description = fields.Text(string="Invoice Description")
    #this field is for account move invoice

    delivery_description = fields.Text(string="Delivery Description")
    #this field is for stock picking 

    sale_data = fields.Float(string="Sale Data")
    #this field is for sale order line one2many field

    mrp_text = fields.Char(string="Manufacturing Text")
    #this field is for mrp production


    project_text = fields.Text(string="Project Text")
    #this field is for project_project model

   

    task_text = fields.Text(string="Task Text")
    #this field is for project task model

    introduction_id = fields.Many2one("introduction.text")
    closing_id = fields.Many2one("closing.text")

    

    def _prepare_invoice(self):
        '''this method will generate a regular invoice #T00316'''
        res = super(SaleOrder, self)._prepare_invoice()
        res["invoice_text"] = self.invoice_description
        return res

   




