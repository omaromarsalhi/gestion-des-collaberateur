from odoo import api, fields, models
class projects(models.Model):
    _name = "projects.db"
    _description = "database"
    name = fields.Char(string='Name',required=True)
    topic=fields.Char(string='Topic',required=True)
    description = fields.Text()
    collaborateur_id = fields.Many2one('collaborateurs.db')
    periods_ids = fields.One2many(comodel_name='period.db', inverse_name='projects_id', string="period")

