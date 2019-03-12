import logging
import requests

DEFAULT_SOCKET_TIMEOUT = 10


class SmartConn:
    def __init__(self, logger, https, host, port, timeout=DEFAULT_SOCKET_TIMEOUT):
        logging.basicConfig()
        self._logger = logger or logging.getLogger('amp')
        self._https, self._host, self._port = https, host, port
        self._socket_timeout = timeout
        protocol = 'https' if https else 'http'
        self._base_url = '{}://{}'.format(protocol, host)
        self._request_session = requests.Session()

    def _build_url(self, path):
        return '{}/{}:{}'.format(self._base_url, path, self._port)

    def request(self, method, path, data=None, headers=None):
        return self._request_session.request(method, self._build_url(path), data=data, headers=headers,
                                             timeout=self._socket_timeout)
