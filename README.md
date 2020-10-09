<img src="https://avatars.githubusercontent.com/u/22528478?s=200&v=4" alt="Paubox" width="150px">

# Paubox Python Package

This is the official Python package for the Paubox Email API. 

The Paubox Email API allows your application to send secure, HIPAA compliant email via Paubox and track deliveries and opens.

# Table of Contents
* [Installation](#installation)
*  [Usage](#usage)
*  [Contributing](#contributing)
*  [License](#license)

<a name="#installation"></a>
## Installation

### Getting Paubox API Credentials
You will need to have a Paubox account. You can [sign up here](https://www.paubox.com/join/see-pricing?unit=messages).

Once you have an account, follow the instructions on the Rest API dashboard to verify domain ownership and generate API credentials.

### Configuring API Credentials

Include your API credentials in a config file (e.g. config.cfg)

```
PAUBOX_HOST: 'https://api.paubox.net/v1/YOUR_ENDPOINT_NAME'
PAUBOX_API_KEY: 'YOUR_API_KEY'
```

Please install config package using pip to load API credentials from config.cfg file:

```
$ pip install config
```

### Install Package
```
$ pip install paubox-python
```

### Dependencies
[Requests](https://github.com/requests/requests)

<a name="#usage"></a>
## Usage

### Sending Messages with the Paubox Mail Helper

Sending via Paubox is easy. This is the minimum content needed to send an email.
```python
import paubox
from paubox.helpers.mail import Mail

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient(paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
recipients = ["recipient@example.com"]
from_ = "sender@yourdomain.com"
subject = "Testing!"
content = {"text/plain": "Hello World!"}
mail = Mail(from_, subject, recipients, content)
response = paubox_client.send(mail.get())
print(response.status_code)
print(response.headers)
print(response.text)
```

### Sending Messages without the Mail Helper Class
```python
import paubox

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient( paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
mail = {
    "data": {
        "message": {
            "recipients": [
                "recipient@example.com"
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

### Allowing non-TLS message delivery

If you want to send non-PHI mail that does not need to be HIPAA-compliant, you can allow the message delivery to take place even if a TLS connection is unavailable.

This means the message will not be converted into a secure portal message when a nonTLS connection is encountered. For this, just pass allowNonTLS as True, as shown below:

#### Using Mail Class Helper
```python
import paubox
from paubox.helpers.mail import Mail

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient( paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
recipients = ["recipient@example.com"]
from_ = "sender@yourdomain.com"
subject = "Testing!"
content = {
    "text/plain": "Hello World!"    
}
optional_headers = {    
    'reply_to': 'replies@yourdomain.com',    
    'allowNonTLS': True
}
mail = Mail(from_, subject, recipients, content, optional_headers)
response = paubox_client.send(mail.get())
print(response.status_code)
print(response.headers)
print(response.text)
```

#### Without the Mail Class Helper
```python
import paubox

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient( paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
mail = {
    "data": {
        "message": {
            "recipients": [
                "recipient@example.com"
            ],            
            'allowNonTLS': True,
            "headers": {
                "subject": "Testing!",
                "from": "Sender <sender@yourdomain.com>",
                "reply-to": "Reply-to <replies@yourdomain.com>"
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

### Forcing Secure Notifications

Paubox Secure Notifications allow an extra layer of security, especially when coupled with an organization's requirement for message recipients to use 2-factor authentication to read messages (this setting is available to org administrators in the Paubox Admin Panel).

Instead of receiving an email with the message contents, the recipient will receive a notification email that they have a new message in Paubox.

#### Using Mail Class Helper
```python
import paubox
from paubox.helpers.mail import Mail

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient( paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
recipients = ["recipient@example.com"]
from_ = "sender@yourdomain.com"
subject = "Testing!"
content = {
    "text/plain": "Hello World!"    
}
optional_headers = {    
    'reply_to': 'replies@yourdomain.com',    
    'forceSecureNotification': 'true'
}
mail = Mail(from_, subject, recipients, content, optional_headers)
response = paubox_client.send(mail.get())
print(response.status_code)
print(response.headers)
print(response.text)
```

#### Without the Mail Class Helper
```python
import paubox

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient( paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
mail = {
    "data": {
        "message": {
            "recipients": [
                "recipient@example.com"
            ],                        
            'forceSecureNotification': 'true',
            "headers": {
                "subject": "Testing!",
                "from": "Sender <sender@yourdomain.com>",
                "reply-to": "Reply-to <replies@yourdomain.com>"
            },
            "content": {
                "text/plain": "Hello World!"             
            }            
        }
    }
}
response = paubox_client.send(mail)
print(response.status_code)
print(response.headers)
print(response.text)
```

### Sending Messages with all available headers

#### Using Mail Class Helper
```python
import paubox
import base64
from paubox.helpers.mail import Mail

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient( paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
recipients = ["recipient@example.com"]
from_ = "sender@yourdomain.com"
subject = "Testing!"
attachment_content = base64.b64encode("Hello World!")
content = {
    "text/plain": "Hello World!",
    "text/html": "<html><body><h1>Hello World!</h1></body></html>"
}
optional_headers = {
    "attachments": [{
        "fileName": "the_file.txt",
        "contentType": "text/plain",
        "content": attachment_content
    }],
    'reply_to': 'replies@yourdomain.com',
    'bcc': 'recipient2@example.com',
    'cc':['recipientcc@example.com'],
    'forceSecureNotification': 'true',
    'allowNonTLS': True
}
mail = Mail(from_, subject, recipients, content, optional_headers)
response = paubox_client.send(mail.get())
print(response.status_code)
print(response.headers)
print(response.text)
```

#### Without the Mail Class Helper
```python
import paubox
import base64

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient( paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
attachment_content = base64.b64encode("Hello World!")
mail = {
    "data": {
        "message": {
            "recipients": [
                "recipient@example.com"
            ],
            "bcc": ["recipient2@example.com"],
            'cc':['recipientcc@example.com'],
            'forceSecureNotification':'true',
            'allowNonTLS': True,
            "headers": {
                "subject": "Testing!",
                "from": "Sender <sender@yourdomain.com>",
                "reply-to": "Reply-to <replies@yourdomain.com>"
            },
            "content": {
                "text/plain": "Hello World!",
                "text/html": "<html><body><h1>Hello World!</h1></body></html>"
            },
            "attachments": [{
                    "fileName": "the_file.txt",
                    "contentType": "text/plain",
                    "content": attachment_content
            }]
        }
    }
}
response = paubox_client.send(mail)
print(response.status_code)
print(response.headers)
print(response.text)
```


### Checking Email Dispositions
The SOURCE_TRACKING_ID of a message is returned in the response.text of your send request. Use response.to_dict to access the response text as a dictionary.
```python
import paubox

from config import Config
config_file = file("config.cfg")
paubox_config = Config(config_file)

paubox_client = paubox.PauboxApiClient( paubox_config.PAUBOX_API_KEY, paubox_config.PAUBOX_HOST)
disposition_response = paubox_client.get("SOURCE_TRACKING_ID")
print(disposition_response.status_code)
print(disposition_response.headers)
print(disposition_response.text)
```

<a name="#contributing"></a>
## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/Paubox/paubox-python.

<a name="#license"></a>
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
Copyright &copy; 2021, Paubox, Inc.
