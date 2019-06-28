# -*- coding: utf-8 -*-, api


# stdlib
import logging


# external libraries
import requests


# odoo core
from odoo import api, fields, models


# project libraries
from .misc import fetch_image_from_url


_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(default='N.A.', required=True)

    @api.multi
    def generate_name(self):
        person_info = requests.get('https://randomuser.me/api/')

        if person_info.status_code == 200:

            for partner in self:
                partner.name = '{} {}'.format(
                    person_info.json()['results'][0]['name']['first'].capitalize(),
                    person_info.json()['results'][0]['name']['last'].capitalize()
                )
                partner.email = person_info.json()['results'][0]['email']
                partner.image = fetch_image_from_url(person_info.json()['results'][0]['picture']['large'])
                partner.city = person_info.json()['results'][0]['location']['city'].capitalize()
                partner.street = person_info.json()['results'][0]['location']['street']
                partner.zip = str(person_info.json()['results'][0]['location']['postcode'])
                partner.phone = person_info.json()['results'][0]['phone']
                partner.mobile = person_info.json()['results'][0]['cell']

        else:
            _logger.error('Cannot fetch person_info from https://randomuser.me/api')
