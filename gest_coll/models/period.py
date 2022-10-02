from odoo import api, fields, models
class period(models.Model):

    _name = "period.db"
    _description = "database"
    begin_date = fields.Date(string='Begin date')
    end_date=fields.Date(string='End date')
    role=fields.Char(string='Role')
    projects_id=fields.Many2one('projects.db')