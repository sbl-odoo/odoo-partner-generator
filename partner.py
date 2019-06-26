# -*- coding: utf-8 -*-


import logging


import requests


from odoo import fields, models, api


from .misc import fetch_image_from_url


_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _name = 'coopplanning.partner'
    _description = 'Partner'

    name = fields.Char(default='N.A.', required=True)
    language = fields.Char()
    # image = fields.Binary(string="Image")
    avatar = fields.Binary(string="Avatar")

    @api.multi
    def generate_name(self):
        person_info = requests.get('https://randomuser.me/api/')

        if person_info.status_code == 200:
            self.name = '{} {}'.format(
                person_info.json()['results'][0]['name']['first'].capitalize(),
                person_info.json()['results'][0]['name']['last'].capitalize()
            )

            self.avatar = fetch_image_from_url(person_info.json()['results'][0]['picture']['medium'])

        else:
            _logger.error('Cannot fetch person_info from https://randomuser.me/api')
