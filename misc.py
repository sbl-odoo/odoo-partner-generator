# -*- coding: utf-8 -*-


# stdlib
import logging
import base64


# external libraries
import requests


_logger = logging.getLogger(__name__)


def fetch_image_from_url(url):
    """
    Gets an image from a URL and converts it to an PIL base-64 encoded image usable in an Odoo Binary field.
    :param url: The URL to fetch.
    :return: A base64 encoded string.
    """
    data = ''

    try:
        data = base64.b64encode(requests.get(url.strip()).content).replace(b'\n', b'')

    except Exception as e:
        _logger.warning('There was a problem requesting the image from URL %s' % url)
        logging.exception(e)

    return data
