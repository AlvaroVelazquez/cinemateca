from odoo import models,fields, api

class pelicula(models.Model):
    _name = 'cinemateca.pelicula'
    title = fields.Char(string="name", required=True, help="Nombre de la  pelicula")
    recaudacion = fields.integer(string="recaudacion", help="recaudacion")
    salaCine_ids = fields.One2many("base.empresa", "peliculas_id", string="sala")
    director_ids = fields.One2many("base.entidad", "peliculas_id", string="director")
    actor_ids = fields.One2many("base.entidad", "pelicula_id", string="actor")
    sesion_ids = fields.One2many("base.empresa", "pelicula_id", string="sesion")