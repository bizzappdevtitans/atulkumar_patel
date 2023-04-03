from odoo import models, fields, api

class ProjectTask(models.Model):
	''' inherit project task model #T00316'''
	_inherit = "project.task"
	_description = "sale inheritance project task"

	task_description = fields.Text(string="Task Description")