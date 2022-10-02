from odoo import api, fields, models
class soft_skills(models.Model):
    _name = "soft_skills.db"
    _description = "database"
    name=fields.Char(string='Name',required=True)

    #collaborateur_id= fields.Many2one('collaborateurs.db')


