# Paubox Package
This package and Paubox Transactional Email HTTP API are currently in alpha development.

This is the official Python package for the Paubox Transactional Email HTTP API. The Paubox Transactional Email API allows your application to send secure, HIPAA-compliant email via Paubox and track deliveries and opens.

It extends the [Requests Library](https://github.com/requests/requests) for seamless integration in your existing Python application.

## Installation

### Getting Paubox API Credentials
You will need to have a Paubox account. Please contact [Paubox Customer Success](https://paubox.zendesk.com/hc/en-us) for details on gaining access to the Transactional Email API alpha testing program.

### Setup Environment Variables

```
$ echo "export PAUBOX_API_KEY='YOUR_API_KEY'" > .env
$ echo "export PAUBOX_HOST='http://api.paubox.net/v1/YOUR_ENDPOINT_NAME'" > .env
$ echo ".env" >> .gitignore
$ source .env
```

### Install Package

```
$ pip install paubox
```

## Usage

### Sending Messages with the Paubox Mail Helper

Sending via Paubox is easy. This is the minimum content needed to send an email.
```python
import paubox
from paubox.helpers.mail import *

paubox_client = paubox.PauboxApiClient()
recipients = ['recipient@example.com']
from_ = 'sender@yourdomain.com'
subject = 'Testing!'
content = { "text/plain": "Hello World!" }
mail = Mail(from_, subject, recipients, content)
response = paubox_client.send(mail.get())
print(response.status_code)
print(response.headers)
print(response.text)
```

### Sending Messages without the Mail Helper Class
```python
import paubox

paubox_client = paubox.PauboxApiClient()
mail = {
  "data": {
    "message": {
      "recipients": [
        "reicpient@example.com"
      ],
      "headers": {
        "subject": "Testing!",
        "from": "sender@yourdomain.com"
      },
      "content": {
        "text/plain": "Hello World!",
      }
    }
  }
}
response = paubox_client.send(mail)
print(response.status_code)
print(response.headers)
print(response.text)
```

### Checking Email Dispositions
```python
import paubox

paubox_client = paubox.PauboxApiClient()
response = paubox_client.get("SOURCE_TRACKING_ID")
print(response.status_code)
print(response.headers)
print(response.text)
```


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/Paubox/paubox-python.


## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Copyright
Copyright &copy; 2018, Paubox Inc.
