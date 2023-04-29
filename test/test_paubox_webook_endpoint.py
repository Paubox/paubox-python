import unittest

from paubox import paubox
from paubox.helpers.WebhookEndpoint import WebhookEndpoint
import os

USERNAME = '<USERNAME>'
API_KEY = '<APIKEY>'

target_url = "https://example.com"
events = ["api_mail_log_delivered"]
active = True
signing_key = "TestSignKey"
api_key = "TestAPIKey"
Endpoint_ID = '667'
Delete_Endpoint_ID = '672'


class TestPauboxAPIWebhook(unittest.TestCase):

    def setUp(self):
        self.api = WebhookEndpoint(USERNAME, API_KEY)

    def test_get_webhook_endpoint(self):
        response = self.api.get_dynamic_templates()
        self.assertEqual(response.status_code, 200)

    def test_get_webhook_endpoint(self):
        response = self.api.get_dynamic_template(Endpoint_ID)                
        self.assertEqual(response.status_code, 200)

    def test_create_webhook_endpoint(self):
        response = self.api.create_dynamic_template(target_url, events, active, signing_key, api_key)
        self.assertEqual(response.status_code, 201)

    def test_update_webhook_endpoint(self):
        response = self.api.update_dynamic_template(Endpoint_ID, target_url, events, active, signing_key, api_key)        
        self.assertEqual(response.status_code, 200)

    def test_delete_webhook_endpoint(self):
        response = self.api.delete_dynamic_template(Delete_Endpoint_ID)
        self.assertEqual(response.status_code, 200)


SUITE = unittest.TestLoader().loadTestsFromTestCase(TestPauboxAPIWebhook)
unittest.TextTestRunner(verbosity=2).run(SUITE)
