from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    rp_margin = fields.Float(
        string='Marge',
        default=1.00,
    )
    
    is_textile_quotation = fields.Boolean(
        string='Devis Confection',
    )