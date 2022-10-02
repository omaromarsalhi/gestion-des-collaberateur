from odoo import api, fields, models
class collaborateurs(models.Model):
    _name = "collaborateurs.db"
    _description = "database"
    name = fields.Char(string='Name',required=True)
    email = fields.Char(string='Email',required=True)
    gender = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string='Sexe',required=True)
    photo = fields.Binary(string='Photo')
    date_of_birth = fields.Date(string='Date de naissance',required=True)
    contact_number= fields.Integer(string='Contact number',required=True)
    post=fields.Char(string='Post',required=True)
    status=fields.Char(string='Status',required=True)
    city=fields.Char(string='City',required=True)
    adress=fields.Char(string='Adress',required=True)
    date_of_joining=fields.Date(string='Date of joining',required=True)
    education=fields.Char(string='Education',required=True)
    specialization=fields.Char(string='Specialization',required=True)
    superviser=fields.Char(string='supervasor',required=True)
    #soft_skills_ids = fields.One2many(comodel_name='soft_skills.db',inverse_name='collaborateur_id', string="Soft skills")
    technical_skills_ids = fields.One2many(comodel_name='technical_skills.db',inverse_name='collaborateur_id', string="Technical skills")
    experience_ids = fields.One2many(comodel_name='experience.db',inverse_name='collaborateur_id', string="Experience ")
    project_ids = fields.One2many(comodel_name='projects.db',inverse_name='collaborateur_id', string="projects ")
    coll_soft_ids = fields.One2many(comodel_name='coll_soft.db',inverse_name='coll_id', string="coll_soft ")
