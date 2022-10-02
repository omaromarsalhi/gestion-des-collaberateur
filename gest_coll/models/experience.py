from odoo import api, fields, models
class experience(models.Model):
    _name = "experience.db"
    _description = "database"
    name = fields.Char(string='Society name',required=True)
    begin_date=fields.Date(string='Begin date',required=True)
    end_date=fields.Date(string='End date',required=True)
    description = fields.Text()
    collaborateur_id = fields.Many2one('collaborateurs.db')

