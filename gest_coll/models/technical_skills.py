from odoo import api, fields, models


class tachnical_skills(models.Model):
    _name = "technical_skills.db"
    _description = "database"
    name = fields.Char(string='Name', required=True)
    level = fields.Selection([('beginner', 'Beginner'), ('medium', 'Medium'), ('expert', 'Expert')], string='Level',
                             required=True)
    description = fields.Text()
    collaborateur_id = fields.Many2one('collaborateurs.db')
