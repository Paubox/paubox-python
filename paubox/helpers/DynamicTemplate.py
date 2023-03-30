import requests


class DynamicTemplate:
    def __init__(self, username, api_key):
        self.base_url = f'https://api.paubox.net/v1/{username}'
        self.headers = {
            'Authorization': f'Token token={api_key}'
        }

    def create_dynamic_template(self, template_path, template_name):
        url = f'{self.base_url}/dynamic_templates'
        with open(template_path, 'rb') as template_file:
            files = {
                'data[body]': template_file,
                'data[name]': (None, template_name),
            }
            response = requests.post(url, headers=self.headers, files=files)
        return response

    def update_dynamic_template(self, template_id, template_path, template_name):
        url = f'{self.base_url}/dynamic_templates/{template_id}'
        with open(template_path, 'rb') as template_file:
            files = {
                'data[body]': template_file,
                'data[name]': (None, template_name),
            }
            response = requests.patch(url, headers=self.headers, files=files)
        return response
    
    def delete_dynamic_template(self, template_id):
        url = f'{self.base_url}/dynamic_templates/{template_id}'
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/json'
        response = requests.delete(url, headers=headers)
        return response

    def get_dynamic_templates(self):
        url = f'{self.base_url}/dynamic_templates'
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/json'
        response = requests.get(url, headers=headers)
        return response
    
    def get_dynamic_template(self, template_id):
        url = f'{self.base_url}/dynamic_templates/{template_id}'
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/json'
        response = requests.get(url, headers=headers)
        return response
