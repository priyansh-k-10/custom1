from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_code = fields.Char(string="Customer Code")

    loyalty_points = fields.Integer(string="Loyalty Points")

    loyalty_status = fields.Char(
        string="Loyalty Status",
        compute="_compute_loyalty_status"
    )

    @api.depends('loyalty_points')
    def _compute_loyalty_status(self):
        for rec in self:
            if rec.loyalty_points >= 100:
                rec.loyalty_status = "Gold"
            else:
                rec.loyalty_status = "Silver"