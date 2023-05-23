from odoo import http
from odoo.http import request


class TableController(models.Model):

    @http.route('/<table_id:string>', type="json", auth='user')
    def table_controller(self, table_id):
        print(">>>>>>>>>>", table_id)
        return request.render("")
