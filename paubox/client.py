import json
import requests
import os
import pdb
from paubox.helper.errors import *

class PauboxApiClient():
  def __init__(
      self,
      api_key=os.environ.get('PAUBOX_API_KEY'),
      host=os.environ.get('PAUBOX_HOST')):
    self.api_key = api_key
    self.host = host

  def send(self, mail):
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
    return response

  def get(self, tracking_code):
    params = { 'sourceTrackingId': tracking_code }
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

class Response(object):
  def __init__(self,response):
    self._status_code = response.status_code
    self._headers = response.headers
    self._text = response.text

  @property
  def status_code(self):
    return self._status_code

  @property
  def headers(self):
    return self._headers

  @property
  def text(self):
    return self._text

  @property
  def to_dict(self):
    if self.text:
      return json.loads(self.text.decode('utf-8'))
    else:
      return None
