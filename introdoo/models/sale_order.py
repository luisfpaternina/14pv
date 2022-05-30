# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import base64
import logging

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def print_report_introdoo(self):
        return self.env.ref('introdoo.report_template_sale_order_introdoo').report_action(self)
