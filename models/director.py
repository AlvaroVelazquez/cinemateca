from odoo import models,fields, api

class director(models.Model):
    _inherit = 'base.entidad'
    _name = 'cinemateca.director'
    name = fields.Char(string="name", required=True, help="Nombre del director")
    apellidos = fields.Char(string="apellidos", required=True, help="Apellidos del director")
    pelicula_id = fields.Many2one("cinemateca.pelicula", string="pelicula")
