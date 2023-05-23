
import qrcode

import base64
from io import BytesIO

from odoo import api, fields, models


class RestaurantTable(models.Model):
    _inherit = 'restaurant.table'

    qr_code = fields.Binary("QR Code", attachment=True,
                            compute="_depends_on_table_name",
                            store=True)
    qr_code_name = fields.Char("QR Name")

    @api.depends('name')
    def _depends_on_table_name(self):
        url = "http://localhost:8069/web"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        data = url + '/' + self.name if self.name else ''
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        temp = BytesIO()
        img.save(temp, format="PNG")
        qr_image = base64.b64encode(temp.getvalue())
        self.qr_code = qr_image
