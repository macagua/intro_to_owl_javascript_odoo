from odoo import api, fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    sale_order_revenue = fields.Float(
        compute="_compute_sale_order_revenue",
        store=True
    )

    @api.depends("sale_order_ids")
    def _compute_sale_order_revenue(self):
        for partner in self:
            partner.sale_order_revenue = sum(partner.sale_order_ids.mapped("amount_total"))
