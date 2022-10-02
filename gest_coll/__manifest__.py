{
    'name': 'gestion des collaborateurs',
    'version': '1.0.0',
    'sequence': -100,
    'application': True,
    'installable': True,
    'auto_install': False,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/collaborateurs.xml',
        'views/soft_skills.xml',
         'views/experience.xml',
        'views/tachnical_skills.xml',
        'views/period.xml',
        'views/projects.xml',
        'views/coll_soft.xml',

    ]
}
