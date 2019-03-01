from odoo import models,fields, api

class salaCine(models.Model):
    #Extension
    _inherit = 'base.empresa'
    pelicula_id = fields.Many2one("cinemateca.pelicula", string="pelicula")
    sesion_ids = fields.One2many("cinemateca.sesion", "salaCine_id", string="sesion")
    

