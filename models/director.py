from odoo import models,fields, api

class director(models.Model):
    #Extension
    _inherit = 'base.entidad'
    _name = 'cinemateca.director'
    apellidos = fields.Char(string="apellidos", required=True, help="Apellidos del mecanico")
    #taller_id = fields.Many2one("taller1.taller", string="taller")
