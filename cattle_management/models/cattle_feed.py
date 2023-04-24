from odoo import models, fields, api


class CattleFeed(models.Model):
    """ This model will show the cattle feed related detail #T00316"""
    _name = "cattle.feed"
    _description = "cattle feed management"
    _rec_name = "cattle_id"

    cattle_id = fields.Many2one("cattle.detail", required=True)
    feed_type = fields.Char("Feed Type", required=True)
    start_feeding_date = fields.Date("Start Feeding Date", required=True)
    last_feeding_date = fields.Date("Last Feeding Date", required=True)
    feed_quantity = fields.Float("Feed Quantity(Kg/Day)", required=True)
    total_feeding_days = fields.Integer(string="Total Feeding Days")
    total_feed_consumed = fields.Float(
        string="Total Feed Consumed(Kg)", compute="_compute_total_feed_consumed"
    )

    @api.depends("feed_quantity", "start_feeding_date", "last_feeding_date")
    def _compute_total_feed_consumed(self):
        """This method will compute total feed consumed by perticular cattle #T00316"""
        for record in self:
            if (
                record.last_feeding_date
                and record.start_feeding_date
                and record.feed_quantity
            ):
                delta = record.last_feeding_date - record.start_feeding_date
                total_days = delta.days
                total_feed = record.feed_quantity * total_days
                record.total_feeding_days = total_days
                record.total_feed_consumed = total_feed
            else:
                record.total_feed_consumed = 0
