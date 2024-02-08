from odoo import models, fields

class EstateAccountEntry(models.Model):
    _name = 'estate_account.entry'
    _description = 'Estate Account Entry'

    name = fields.Char(string='Description', required=True)
    amount = fields.Float(string='Amount', required=True)
    property_id = fields.Many2one('estate.property', string='Related Property')
    date = fields.Date(string='Entry Date', default=fields.Date.context_today)
