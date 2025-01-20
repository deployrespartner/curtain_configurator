from odoo import fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    rp_width = fields.Float(
        string='Largeur',
        default=1.00,
    )
    rp_height = fields.Float(
        string='Hauteur',
        default=1.00,
    )
    rp_nb_curtain_on_curtain_rod = fields.Float(
        string='Nb Rdx par tringle',
        default=1.00,
    )
    rp_nb_same_curtain_rod = fields.Float(
        string='Nb tringle identique',
        default=1.00,
    )