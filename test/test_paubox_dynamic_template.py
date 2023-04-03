import unittest

from paubox import paubox
from paubox.helpers.DynamicTemplate import PauboxAPI
import os

USERNAME = '<USERNAME>'
API_KEY = '<APIKEY>'
TEMPLATE_PATH = os.getcwd() + '\\Template.hbs'
TEMPLATE_NAME = 'Tempate Name'
TEMPLATE_ID = '667'
Delete_TEMPLATE_ID = '672'


class TestPauboxAPI(unittest.TestCase):

    def setUp(self):
        self.api = PauboxAPI(USERNAME, API_KEY)

    def test_get_dynamic_templates(self):
        response = self.api.get_dynamic_templates()
        self.assertEqual(response.status_code, 200)

    def test_get_dynamic_template(self):
        response = self.api.get_dynamic_template(TEMPLATE_ID)                
        self.assertEqual(response.status_code, 200)

    def test_create_dynamic_template(self):
        response = self.api.create_dynamic_template(TEMPLATE_PATH, TEMPLATE_NAME)
        self.assertEqual(response.status_code, 201)

    def test_update_dynamic_template(self):
        response = self.api.update_dynamic_template(TEMPLATE_ID, TEMPLATE_PATH, TEMPLATE_NAME)        
        self.assertEqual(response.status_code, 200)

    def test_delete_dynamic_template(self):
        response = self.api.delete_dynamic_template(Delete_TEMPLATE_ID)
        self.assertEqual(response.status_code, 200)


SUITE = unittest.TestLoader().loadTestsFromTestCase(TestPauboxAPI)
unittest.TextTestRunner(verbosity=2).run(SUITE)
