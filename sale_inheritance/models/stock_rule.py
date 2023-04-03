from odoo import models, fields, api

class StockRule(models.Model):
	'''Inherit stock rule class which is persent inside mrp '''
	_inherit = 'stock.rule'
	_description = "sale inheritance stock rule"

	def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom):
		'''this method will pass value from sale order to manufacturing order #T00316'''

		vals = super(StockRule, self)._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom)
		vals["mrp_description"] = values.get('mrp_text')                                                                     
		print("\n\n print vals",vals,"\n\n")
		return vals


 