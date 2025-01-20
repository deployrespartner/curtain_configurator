from odoo import fields, models

class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    rp_amplitude = fields.Float(
        string='Amplitude',
        default=1.00,
    )
    rp_curtain_width = fields.Float(
        string='Prix par lé',
        default=1.00,
    )
    rp_extra_height = fields.Float(
        string='Hauteur Suppl.',
        default=1.00,
    )