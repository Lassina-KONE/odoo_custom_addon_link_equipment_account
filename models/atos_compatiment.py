from odoo import fields, models

class AtosCompatiment(models.Model):
	_name = 'atos_compatiment'
	_description = 'Compatiments dans le depot du Stock Atos'
	
	name = fields.Char('Libelle',required=True)
	designation = fields.Char(required=True)
	equipement_ids = fields.One2many("atos_equipement","compatiment_id")
