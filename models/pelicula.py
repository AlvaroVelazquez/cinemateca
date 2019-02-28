from odoo import models,fields, api

class pelicula(models.Model):
    _name = 'cinemateca.pelicula'
    title = fields.Char(string="name", required=True, help="Nombre de la  pelicula")
    recaudacion = fields.Integer(string="recaudacion", help="recaudacion")
    salaCine_ids = fields.One2many("cinemateca.salaCine", "peliculas_id", string="sala")
    director_ids = fields.One2many("cinemateca.director", "peliculas_id", string="director")
    actor_ids = fields.One2many("cinemateca.actor", "pelicula_id", string="actor")
    sesion_ids = fields.One2many("cinemateca.sesion", "pelicula_id", string="sesion")