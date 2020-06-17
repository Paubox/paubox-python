"""
This library allows you to send emails through the Paubox Transactional Email
API application and get the email disposition of sent emails.

Paubox Mail
"""

import base64
from six import string_types


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
        self._cc = []
        self._reply_to = None
        self._attachments = []
        self._forceSecureNotification = None
        self._allowNonTLS = False      
        if from_:
            self.from_ = from_
        if subject:
            self.subject = subject
        if recipients:
            self.recipients = recipients
        if content:
            if 'text/html' in content:
                _html_text = content.get('text/html')
                if(_html_text != None and _html_text != ""):
                    encoded_html = base64.b64encode(_html_text)
                    content['text/html'] = encoded_html

            self.content = content

        if optional_headers:
            if 'bcc' in optional_headers:
                self.bcc = optional_headers['bcc']
            if 'cc' in optional_headers:
                self.cc = optional_headers['cc'] 
            if 'reply_to' in optional_headers:
                self.reply_to = optional_headers['reply_to']
            if 'attachments' in optional_headers:
                self.attachments = optional_headers['attachments']
            if 'forceSecureNotification' in optional_headers:
                self.forceSecureNotification = optional_headers['forceSecureNotification']
            if 'allowNonTLS' in optional_headers:
                self.allowNonTLS = optional_headers['allowNonTLS']

    def get(self):
        """Formats the Email to a Send Request for the Paubox Email API"""
        mail = {"data": {"message": {}}}
        mail["data"]["message"]["recipients"] = self.recipients
        mail["data"]["message"]["headers"] = {
            "subject": self.subject, "from": self.from_}
        mail["data"]["message"]["content"] = self.content

        if hasattr(self, 'bcc'):
            mail["data"]["message"]["bcc"] = self.bcc
        if hasattr(self, 'cc'):
            mail["data"]["message"]["cc"] = self.cc
        if hasattr(self, 'reply_to'):
            mail["data"]["message"]["headers"]["reply-to"] = self.reply_to
        if hasattr(self, 'attachments'):
            mail["data"]["message"]["attachments"] = self.attachments
        if hasattr(self, 'forceSecureNotification'):
            self.forceSecureNotification = self._return_valid_forcesecurenotification_value()
            if(self.forceSecureNotification != None):
                mail["data"]["message"]["forceSecureNotification"] = self.forceSecureNotification
        if hasattr(self, 'allowNonTLS'):
            mail["data"]["message"]["allowNonTLS"] = self.allowNonTLS
        else:
            mail["data"]["message"]["allowNonTLS"] = False                    
        return mail

    def _return_valid_forcesecurenotification_value(self):
        """ Returns valid ForceSecureNotification value """

        _forceSecureNotification = self.forceSecureNotification
        if isinstance(_forceSecureNotification, string_types):
            if(_forceSecureNotification == None or _forceSecureNotification == ""):
                return None
            else:
                _forceSecureNotificationValue = _forceSecureNotification.strip().lower()
                if _forceSecureNotificationValue == 'true':
                    return True
                elif _forceSecureNotificationValue == 'false':
                    return False
                else:
                    return None
        else:
            return None
