# PyAPNs2

[![PyPI version](https://img.shields.io/pypi/v/apns23.svg)](https://pypi.python.org/pypi/apns23)
[![PyPI version](https://img.shields.io/pypi/pyversions/apns23.svg)](https://pypi.python.org/pypi/apns23)

Python library for interacting with the Apple Push Notification service (APNs) via HTTP/2 protocol
Fork created to support iOS13 messaging with Python 2.7/3.6 support

## Installation

Download the source from Github.

## Sample usage

```python
from apns23.client import APNsClient
from apns23.payload import Payload

token_hex = 'b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b87'
payload = Payload(alert="Hello World!", sound="default", badge=1)
topic = 'com.example.App'
client = APNsClient('key.pem', use_sandbox=False, use_alternative_port=False)
client.send_notification(token_hex, payload, topic)

# To send multiple notifications in a batch
Notification = collections.namedtuple('Notification', ['token', 'payload'])
notifications = [Notification(payload=payload, token=token_hex)]
client.send_notification_batch(notifications=notifications, topic=topic)

# To use token based authentication
from apns23.credentials import TokenCredentials

auth_key_path = 'path/to/auth_key'
auth_key_id = 'app_auth_key_id'
team_id = 'app_team_id'
token_credentials = TokensCredentials(auth_key_path=auth_key_path, auth_key_id=auth_key_id, team_id=team_id)
client = APNsClient(credentials=token_credentials, use_sandbox=False)
client.send_notification_batch(notifications=notifications, topic=topic)
```

## Further Info

[iOS Reference Library: Local and Push Notification Programming Guide][a1]

## Contributing

To develop PyAPNs23, check out the code and install dependencies. It's recommended to use a virtualenv to isolate dependencies:
```shell
# Clone the source code.
git clone https://github.com/VinayGValsaraj/PyAPNs23.git
cd PyAPNs23
# Create a virtualenv and install dependencies.
virtualenv venv
. venv/bin/activate
pip install -e .[tests]
```

To run the tests:
```shell
pytest
```

You can use `tox` for running tests with all supported Python versions:
```shell
pyenv install 2.7.9; pyenv install 3.6.9
pyenv local 2.7.9 3.6.9
pip install tox
tox
```

To run the linter:
```shell
pip install pylint
pylint --reports=n apns23 test
```

## License

PyAPNs23 is distributed under the terms of the MIT license.

See [LICENSE](LICENSE) file for the complete license details.

[a1]:https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/
