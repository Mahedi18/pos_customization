from odoo import fields, models


class POSShortcuts(models.Model):
    _name = "pos.shortcuts"
    _description = "POS Shortcuts"

    name = fields.Char(string="Name")
    next_screen = fields.Char(string="Next Screen")
    customer_screen = fields.Char(string="Customer Screen")
    search_product = fields.Char(string="Search Product")
    select_quantity = fields.Char(string="Select Quantity in Numpad")
    select_discount = fields.Char(string="Select Discount in Numpad")
    select_price = fields.Char(string="Select Price in Numpad")
    add_customer = fields.Char(string="Add Customer")
    select_previous_orderline = fields.Char(string="Select Previous Orderline")
    select_next_orderline = fields.Char(string="Select Next Orderline")
    delete_order = fields.Char(
        string="Delete Quantity/Discount/Price of Orderline")
    other_invoice = fields.Char(string="Other Invoice")
    payment_method_ids = fields.One2many(
        "account.journal", "pos_shorcuts_id", string="Payment Method")
    select_deselect_customer = fields.Char(string="Select/Deselect Customer")
    print_receipt = fields.Char(string="Print Receipt")
    show_next_screen = fields.Char(string="Show Next Screen")
    back_screen = fields.Char(string="Next Screen")
    create_new_order = fields.Char(string="Create New Order")
    delete_current_order = fields.Char(string="Delete Current Order")
    ok_button_popup = fields.Char(string="Ok Button Popup")
    cancle_button_in_popup = fields.Char(string="Cancle Button in Popup")
    select_next_order = fields.Char(string="Select Next Order")
    select_previous_order = fields.Char(string="Select Previous Order")
    select_pos_user = fields.Char(string="Select POS User")
    refresh_connection = fields.Char(string="Refresh Connection")
    close_connection = fields.Char(string="Close POS Connection")
