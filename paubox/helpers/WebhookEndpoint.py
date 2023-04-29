import json
import requests


class WebhookEndpoint:
    def __init__(self, username, api_key):
        self.base_url = f'https://api.paubox.net/v1/{username}'
        self.headers = {
            'Authorization': f'Token token={api_key}'
        }

    def create_webhook_endpoint(self, target_url, events, active, signing_key, api_key):
        url = f'{self.base_url}/webhook_endpoints'
        payload = json.dumps({
            "target_url": target_url,
            "events": events,
            "active": active,
            "signing_key": signing_key,
            "api_key": api_key
        })    
        response = requests.post(url, headers=self.headers, data=payload)
        return response

    def update_webhook_endpoint(self, endpoint_id, target_url, events, active, signing_key, api_key):
        url = f'{self.base_url}/webhook_endpoints/{endpoint_id}'
        payload = json.dumps({
            "target_url": target_url,
            "events": events,
            "active": active,
            "signing_key": signing_key,
            "api_key": api_key
        }) 
        response = requests.patch(url, headers=self.headers, data=payload)
        return response
    
    def delete_webhook_endpoint(self, endpoint_id):
        url = f'{self.base_url}/webhook_endpoints/{endpoint_id}'
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/json'
        response = requests.delete(url, headers=headers)
        return response

    def get_webhook_endpoints(self):
        url = f'{self.base_url}/webhook_endpoints'
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/json'
        response = requests.get(url, headers=headers)
        return response
    
    def get_webhook_endpoint(self, endpoint_id):
        url = f'{self.base_url}/webhook_endpoints/{endpoint_id}'
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/json'
        response = requests.get(url, headers=headers)
        return response
