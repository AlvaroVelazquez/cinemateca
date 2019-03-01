from odoo import models,fields, api

class sesion(models.Model):
    #Clasica
    _inherit = 'base.empresa'
    _name = 'cinemateca.sesion'
    precio = fields.Integer(string="precio", help="precio de la pelicula")
    asistencia = fields.Integer(string="asistencia", help="numero de espectadores")
    recaudacion = fields.Integer(string="recaudacion", help="recaudacion", compute="sumar")
    pelicula_id = fields.Many2one("cinemateca.pelicula", string="pelicula")
    salaCine_id = fields.Many2one("base.empresa", string="pelicula")


@api.depends('totalRecaudacion')
    def sumar(self):
        self.recaudacion = self.asistencia * self.precio


            

