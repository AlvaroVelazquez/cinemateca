from odoo import models,fields, api

class actor(models.Model):
    #Extension
    _inherit = 'base.entidad'
    name = fields.Char(string="name", required=True, help="Nombre del actor")
    rol = fields.Char(string="rol", help="Nombre del rol")
    cache = fields.Integer(string="cache")
    pelicula_id = fields.Many2one("cinemateca.pelicula", string="pelicula")


   
    
    