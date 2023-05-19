from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError


class CattleDetail(models.Model):
    """Created this model for adding Cattle Detail #T00316"""

    _name = "cattle.detail"
    _description = "Cattle Detail"
    _rec_name = "cattle_name"

    cattle_seq = fields.Char(string="Cattle Id", readonly=True)
    cattle_name = fields.Selection(
        [("cow", "Cow"), ("buffalo", "Buffalo")],
        default="cow",
        string="Cattle Name",
        required=True,
    )
    birth_date = fields.Date(string="Cattle Birth Date", required=True)
    cattle_age = fields.Integer(string="Cattle Age", compute="_compute_age")
    cattle_weight = fields.Float(string="Cattle Weight")
    price = fields.Float(required=True)
    cattle_breed = fields.Char(string="Cattle Breed", required=True)
    cattle_colour = fields.Char(string="Cattle Colour", required=True)
    sold = fields.Boolean(string="Sold", default=False)
    cattle_image = fields.Binary()
    product_id = fields.Many2one("product.product", string="Customer")
    partner_id = fields.Many2one("res.partner", string="Customer")
    user_id = fields.Many2one("res.users", string="Sales Person")
    state = fields.Selection(
        [("draft", "Draft"), ("product_created", "Product Created")],
        default="draft",
    )
    cattle_gender = fields.Selection(
        [
            ("female", "Female"),
        ],
        string="Cattle Gender",
        default="female",
    )

    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", " high"), ("3", "very high")],
        string="Status",
        default="1",
    )

    @api.depends("birth_date")
    def _compute_age(self):
        """This method will compute age based on DOB #T00316"""
        today = date.today()
        for record in self:
            if record.birth_date:
                delta = today - record.birth_date
                record.cattle_age = delta.days * 0.002738
            else:
                record.cattle_age = 0

    def name_get(self):
        """created name_get method to concatnate two fields #T00316"""
        result = []

        for rec in self:
            result.append((rec.id, "%s - %s" % (rec.cattle_seq, rec.cattle_name)))

        return result

    @api.model
    def create(self, vals):
        """created this method to generate sequence no #T00316"""
        vals["cattle_seq"] = self.env["ir.sequence"].next_by_code("cattle.detail")
        return super(CattleDetail, self).create(vals)

    def create_products(self):
        """created this method to create product in product.product #T00316"""
        for cattle in self:
            if cattle.sold:
                raise UserError("Selected cattle Already sold")
            elif cattle.state == "product_created":
                raise UserError("Product already created")
            product = self.env["product.product"].create(
                {
                    "name": cattle.cattle_name,
                    "type": "product",
                    "list_price": cattle.price,
                    "cattle_breed": cattle.cattle_breed,
                    "cattle_weight": cattle.cattle_weight,
                    "cattle_colour": cattle.cattle_colour,
                    "cattle_age": cattle.cattle_age,
                    "default_code": "CATTLE-%s" % cattle.id,
                    "description_sale": "Breed:%s\nGender:%s\nPrice:%s\nAge:%s\nColour:%s"
                    % (
                        cattle.cattle_breed,
                        cattle.cattle_gender,
                        cattle.price,
                        cattle.cattle_age,
                        cattle.cattle_colour,
                    ),
                }
            )
            self.write({"state": "product_created"})
            cattle.write({"product_id": product.id})
