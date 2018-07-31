"""
This library allows you to send emails through the Paubox Transactional Email
API application and get the email disposition of sent emails.

Paubox Mail
"""

class Mail(object):
    """Paubox API send request formatter."""
    def __init__(
            self,
            from_=None,
            subject=None,
            recipients=None,
            content=None,
            optional_headers=None):
        """
        :param from_: From email address.
        :type from: basestring
        :param subject: Email subject.
        :type subject: basestring
        :param recipients: Email recipients.
        :type recipients: list
        :param content: Body of the email.
        :type content: dict
        :params optional_headers: Additional optional headers for the email.
        :type optional_headers: dict
        """
        self._from_ = None
        self._subject = None
        self._recipients = []
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
        """Formats the Email to a Send Request for the Paubox Email API"""
        mail = {"data": {"message": {}}}
        mail["data"]["message"]["recipients"] = self.recipients
        mail["data"]["message"]["headers"] = {"subject": self.subject, "from":self.from_}
        mail["data"]["message"]["content"] = self.content

        if hasattr(self, 'bcc'):
            mail["data"]["message"]["bcc"] = self.bcc
        if hasattr(self, 'reply_to'):
            mail["data"]["message"]["headers"]["reply-to"] = self.reply_to
        if hasattr(self, 'attachments'):
            mail["data"]["message"]["attachments"] = self.attachments
        return mail
