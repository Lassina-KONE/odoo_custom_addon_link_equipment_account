from odoo import fields, models

class AtosEquipementMarque(models.Model):
	_name = 'atos_equipement_marque'
	_description = 'Marques des Equipements du Stock Atos'
	
	name = fields.Char('Nom de la marque',required=True)
	equipement_ids = fields.One2many("atos_equipement","marque_id")
