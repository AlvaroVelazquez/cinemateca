from odoo import models,fields, api

class sesion(models.Model):
    #Clasica
    _inherit = 'base.empresa'
    _name = 'cinemateca.sesion'
    precio = fields.Integer(string="precio", help="precio de la pelicula")
    asistencia = fields.Integer(string="asistencia", help="numero de espectadores")
    pelicula_ids = fields.Many2one("cinemateca.pelicula", string="pelicula")
    salaCine_ids = fields.Many2one("cinemateca.salaCine", string="pelicula")


   
            

