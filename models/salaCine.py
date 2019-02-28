from odoo import models,fields, api

class salaCine(models.Model):
    #Clasica
    _inherit = 'base.empresa'
    _name = 'cinemateca.salaCine'
    sesion_ids = fields.One2many("base.empresa", "salaCine_id", string="sesion")
    

