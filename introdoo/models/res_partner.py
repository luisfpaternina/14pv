from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import base64
import logging

class ResPartner(models.Model):
    _inherit = 'res.partner'
