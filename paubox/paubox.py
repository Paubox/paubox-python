"""
This library allows you to send emails through the Paubox Transactional Email
API application and get the email disposition of sent emails.

Paubox Client
"""

import json
import os
import requests
from .helpers.errors import handle_error

class Response(object):
    """Response from Paubox Transactional Email API"""

    def __init__(self, response):
        self._status_code = response.status_code
        self._headers = response.headers
        self._text = response.text

    @property
    def status_code(self):
        """
        :return: Status code of Paubox API response
        """
        return self._status_code

    @property
    def headers(self):
        """
        :return: Headers of Paubox API response
        """
        return self._headers

    @property
    def text(self):
        """
        :return: Body of Paubox API response
        """
        return self._text

    @property
    def to_dict(self):
        """
        :return: Body of Paubox API response as a dict
        """
        if self.text:
            return json.loads(self.text.decode('utf-8'))
        return None

class PauboxApiClient(object):
    """
    Client to send requests to the Paubox Transactional Email API
    """
    def __init__(
            self,
            api_key=os.environ.get('PAUBOX_API_KEY'),
            host=os.environ.get('PAUBOX_HOST')):
        """
        Construct API client to the Paubox Transactional Email API
        :param api_key: Paubox API key.
        :type api_key: basestring
        :params host: Paubox endpoint base URL for API calls
        :type host: basestring
        """
        self.api_key = api_key
        self.host = host

    def send(self, mail):
        """
        Send messages through the Paubox API
        """
        headers = {
            'Content-Type':'application/json',
            'Authorization': "Token token=" + self.api_key
        }
        url = self.host + '/messages'
        try:
            response = requests.post(url, json=mail, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            error = handle_error(error)
            raise error
        return Response(response)

    def get(self, tracking_code):
        """
        Get the disposition of messages through the Paubox API
        """
        params = {'sourceTrackingId': tracking_code}
        headers = {
            'Content-Type':'application/json',
            'Authorization': "Token token=" + self.api_key
        }
        url = self.host + '/message_receipt'
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            error = handle_error(error)
            raise error
        return Response(response)
