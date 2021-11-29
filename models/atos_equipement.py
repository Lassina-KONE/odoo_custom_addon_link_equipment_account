from odoo import api, fields, models
from odoo.exceptions import ValidationError

class AtosEquipement(models.Model):
	_name = 'atos_equipement'
	_description = 'Equipement du Stock Atos'
	_order = 'state asc'
	
	name = fields.Char('Nom equipement',required=True)
	serial_number = fields.Char('Numero de serie',required=True)
	part_number = fields.Char('Numero de partition',required=True)
	description = fields.Text("Description")
	marque_id = fields.Many2one("atos_equipement_marque",string="Marque")
	compatiment_id = fields.Many2one("atos_compatiment",string="Compatiment")
	actif = fields.Boolean("Statut",default="True")
	raison_de_sortie = fields.Text("Raison de sortie")
	state = fields.Selection(
		[
			('in','En stock'),
			('out','Sortie')
		],
		default="in",
		string="Etat"
	)  
	date_in = fields.Datetime("Date d'entree",default= lambda self: fields.Datetime.now(), required=True)
	date_out = fields.Datetime("Date de sortie")

	_sql_constraints = [
		('unique_serial_number', 'unique(serial_number)', 'Ce numero de serie existe deja !')
	]

	@api.onchange("actif")
	def _change_date_out(self):
		if not self.actif:
			self.state = "out"
			self.date_out = fields.Datetime.now()
		else:
			self.state = "in"
			self.date_out = ''

	def marquer_comme_sortie(self):
		for record in self:
			record.actif = False
			record.state = "out"
			record.date_out = fields.Datetime.now()
		return True

	@api.constrains('date_out')
	def _check_date_out(self):
		for record in self:
			if not record.actif:
				if record.date_out < record.date_in:
					raise ValidationError("La date de sortie ne peut pas etre inferieur a la date d'entree.")

	
