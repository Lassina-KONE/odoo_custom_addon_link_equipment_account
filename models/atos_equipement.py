from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class AtosEquipement(models.Model):
    _inherit = 'atos_equipement'


    def marquer_comme_sortie(self):
        
        self.env['account.move'].create(
            {
                'partner_id': self.partner_id.id,
                'move_type': 'out_invoice',
                'journal_id': 1,
                'name': self.name
            }
        )
        _logger.info('Facture creee avec succes')
        print('Facture creee avec succes')
        return super().marquer_comme_sortie()