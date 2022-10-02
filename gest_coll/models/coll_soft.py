from odoo import api, fields, models
class projects(models.Model):
    _name = "coll_soft.db"
    _description = "database"
    coll_soft_id= fields.Many2one('soft_skills.db')
    coll_id=fields.Many2one('collaborateurs.db')
    level = fields.Selection([('beginner', 'Beginner'), ('medium', 'Medium'), ('expert', 'Expert')], string='Level',
                             required=True)