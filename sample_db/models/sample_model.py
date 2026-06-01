from odoo import models, fields


class SampleModel(models.Model):
    _name = 'sample.model'
    _description = 'Sample Model'

    name = fields.Char(string="Name", required=True)
    location = fields.Char(string="Location")
    email = fields.Char(string="Email")
    active = fields.Boolean(string="Active", default=True)