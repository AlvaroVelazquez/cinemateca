from odoo import models,fields, api

class sesion(models.Model):
    #Clasica
    _inherit = 'base.empresa'
    _name = 'cinemateca.sesion'
    precio = fields.Integer(string="precio", help="precio de la pelicula")
    asistencia = fields.Integer(string="asistencia", help="numero de espectadores")
    #coche_ids = fields.One2many("res.partner", "taller_id", string="coches")
    #mecanico_ids = fields.One2many("base.entidad", "taller_id", string="mecanicos")


   
            

