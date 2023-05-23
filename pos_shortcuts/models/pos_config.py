from odoo import fields, models


class POSConfig(models.Model):
    _inherit = "pos.config"

    choose_shortcuts = fields.Boolean(string="Choose Shortcuts")

    iface_choose_shortcuts_id = fields.Many2one(
        "pos.shortcuts", string="Choose Shortcuts")
