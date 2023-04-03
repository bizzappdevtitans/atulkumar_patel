from odoo import models, fields, api

class ProjectProject(models.Model):
	''' inherit project.project model #T00316'''
	_inherit = "project.project"
	_description = "sale inheritance project_project"

	project_description = fields.Text(string="Project Description")