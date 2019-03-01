from odoo import models,fields, api

class sesion(models.Model):
    #Clasica
    _inherit = 'base.empresa'
    _name = 'cinemateca.sesion'
    precio = fields.Integer(string="precio", help="precio de la pelicula")
    asistencia = fields.Integer(string="asistencia", help="numero de espectadores", compute="guardar")
    pelicula_id = fields.Many2one("cinemateca.pelicula", string="pelicula")
    salaCine_id = fields.Many2one("base.empresa", string="pelicula")


   @api.depends('guardarValores')
    def guardar(self):
        x = self.precio * self.asistencia

            

