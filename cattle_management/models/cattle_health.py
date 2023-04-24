from odoo import models, fields, api


class CattleHealth(models.Model):
    """This model will show the cattle health related detail #T00316"""

    _name = "cattle.health"
    _description = "cattle health"
    _rec_name = "cattle_id"

    cattle_id = fields.Many2one("cattle.detail", required=True)
    health_issue = fields.Selection(
        [
            ("foot_rot", "Foot rot"),
            ("fever", "Fever"),
            ("brucellosis", "Brucellosis"),
            ("schmallenberg_virus", "Schmallenberg Virus"),
            ("mouth_disease", "Mouth disease"),
            ("bovine_viral_diarrhoea", "Bovine Viral Diarrhoea"),
            ("no_issue", "No Issue"),
        ],
        default="no_issue",
        string=" Health Issue",
        required=True,
    )
    diagnosis_date = fields.Date(string="Diagnosis Date", required=True)
    recovery_date = fields.Date(string="Recovery Date")
    veterinarian = fields.Many2one("cattle.doctor", string="Veterinarian")
    total_health_issues = fields.Integer(
        "Total Health Issues", compute="_compute_total_health_issues"
    )

    @api.depends("cattle_id", "health_issue")
    def _compute_total_health_issues(self):
        """This method will compute total health issue of a perticular cattle #T00316"""
        for record in self:
            if record.health_issue == "no_issue":
                record.total_health_issues = 0
            else:
                total_issues = self.search_count(
                    [("cattle_id", "=", record.cattle_id.id)]
                )
                record.total_health_issues = total_issues
