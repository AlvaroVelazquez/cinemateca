from odoo import models,fields, api

class director(models.Model):
    #Clasica
    _inherit = 'base.entidad'
    _name = 'cinemateca.director'
    name = fields.Char(string="name", required=True, help="Nombre del director")
    apellidos = fields.Char(string="apellidos", required=True, help="Apellidos del director")
    pelicula_ids = fields.One2many("cinemateca.pelicula", "director_id", string="sesion")