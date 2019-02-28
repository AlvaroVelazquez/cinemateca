from odoo import models,fields, api

class actor(models.Model):
    _inherit = 'base.entidad'
    _name = 'cinemateca.actor'
    name = fields.Char(string="name", required=True, help="Nombre del actor")
    rol = fields.Char(string="rol", help="Nombre del rol")
    cache = fields.Integer(string="cache")
    pelicula_id = fields.Many2one("cinemateca.pelicula", string="pelicula")


   
    
    