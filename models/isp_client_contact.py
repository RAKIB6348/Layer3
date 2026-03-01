from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class IspClientContact(models.Model):
    _name = 'isp.client.contact'
    _description = 'ISP Client Contact'

    client_id = fields.Many2one('isp.client', ondelete='cascade')
    transmission_id = fields.Many2one('isp.transmission.nttn', ondelete='cascade')
    work_order_id = fields.Many2one('isp.work.order', ondelete='cascade')
    contact_type = fields.Selection([
        ('owner', 'Owner'),
        ('billing', 'Billing'),
        ('marketing', 'Marketing'),
        ('technical', 'Technical'),
    ], string="Type", required=True)

    name = fields.Char(string="Name")
    designation = fields.Char(string="Designation")
    phone = fields.Char(string="Phone")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    active = fields.Boolean(default=True, invisible=True)

    @api.constrains('client_id', 'transmission_id', 'work_order_id')
    def _check_contact_parent(self):
        for rec in self:
            if not rec.client_id and not rec.transmission_id and not rec.work_order_id:
                raise ValidationError(_("Contact must be linked to a client, an NTTN transmission, or a work order."))
