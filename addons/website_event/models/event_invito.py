from odoo import fields, models


class InvitedCompany(models.Model):
    _name = 'evento.invited.company'
    _description = 'Aziende Invitate'

    name = fields.Char(string='Nome Azienda', required=True)
    email = fields.Char(string='Email', required=True)
    status = fields.Selection([
        ('pending', 'In attesa'),
        ('accepted', 'Accettato'),
        ('declined', 'Rifiutato'),
    ], string='Stato Invito', default='pending')
    event_id = fields.Many2one('evento.event', string='Evento', required=True)
