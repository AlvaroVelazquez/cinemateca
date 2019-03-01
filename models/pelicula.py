from odoo import models,fields, api

class pelicula(models.Model):
    _name = 'cinemateca.pelicula'
    title = fields.Char(string="name", required=True, help="Nombre de la  pelicula")
    genero = fields.Selection([
        ('Accion', 'Accion'),
        ('Aventura', 'Aventura'), 
        ('Misterio', 'Misterio')], string='Genero')
    salaCine_ids = fields.One2many("base.empresa", "pelicula_id", string="sala")
    director_id = fields.Many2one("cinemateca.director", string="director")
    actor_ids = fields.One2many("base.entidad", "pelicula_id", string="actor")
    sesion_ids = fields.One2many("cinemateca.sesion", "pelicula_id", string="sesion")



