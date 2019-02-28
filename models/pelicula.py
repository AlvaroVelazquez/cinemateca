from odoo import models,fields, api

class pelicula(models.Model):
    _name = 'cinemateca.peliculas'
    title = fields.Char(string="name", required=True, help="Nombre de la  pelicula")
    recaudacion = fields.integer(string="recaudacion", help="recaudacion")
    salaCines_ids = fields.One2many("base.empresa", "peliculas_id", string="sala")