from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_code = fields.Char(string="Customer Code")
    age = fields.Integer(string="Age")
    city = fields.Char(string="City")