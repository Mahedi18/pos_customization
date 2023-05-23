from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    pos_shorcuts_id = fields.Many2one("pos.shortcuts")
    key_code_journals = fields.Char(string="Key Code Journals")
