import os

class Mail(object):
  def __init__(
      self,
      from_=None,
      subject=None,
      recipients=None,
      content=None,
      optional_headers={}):

    self._from_ = None
    self._subject = None
    self._recipients = None
    self._content = None
    self._bcc = None
    self._reply_to = None
    self._attachments = []

    if from_:
      self.from_ = from_
    if subject:
      self.subject = subject
    if recipients:
      self.recipients = recipients
    if content:
      self.content = content

    if optional_headers:
      if optional_headers.has_key('bcc'):
        self.bcc = optional_headers['bcc']
      if optional_headers.has_key('reply_to'):
        self.reply_to = optional_headers['reply_to']
      if optional_headers.has_key('attachments'):
        self.attachments = optional_headers['attachments']

  def get(self):
    mail = { "data": { "message": {} } }
    mail["data"]["message"]["recipients"] = self.recipients
    mail["data"]["message"]["headers"] = {"subject": self.subject, "from":self.from_ }
    mail["data"]["message"]["content"] = self.content

    if hasattr(self, 'bcc'):
      mail["data"]["message"]["bcc"] = self.bcc
    if hasattr(self, 'reply_to'):
      mail["data"]["message"]["headers"]["reply-to"] = self.reply_to
    if hasattr(self, 'attachments'):
      mail["data"]["message"]["attachments"] = self.attachments
    return mail




