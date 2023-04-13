from odoo import models, fields, api


class CattleNews(models.Model):
    """Created this model for adding News Detail #T00316"""

    _name = "cattle.news"
    _description = "News Detail"

    news = fields.Char(string="News")
    news_id = fields.Char(string="News Id", readonly=True)

    # created this model to generate sequence no
    @api.model
    def create(self, vals):
        vals["news_id"] = self.env["ir.sequence"].next_by_code("cattle.news")
        return super(CattleNews, self).create(vals)
