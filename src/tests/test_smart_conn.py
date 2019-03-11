import subprocess
import sys
import time
import unittest
from subprocess import Popen

from src.si import amp,smart_conn

python = '/usr/local/bin/python3'


class TestSmartConn(unittest.TestCase):
    _process = None  # type: Popen

    @classmethod
    def setUpClass(cls):
        cls._process = subprocess.Popen([python, "server.py"])
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls._process.terminate()
        if sys.version_info[0] == 3:
            cls._process.wait(1)
        else:
            cls._process.wait()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_wrong_agent(self):
        with self.assertRaises(amp.AmpError) as ex:
            with smart_conn.SmartConn(None, False, "localhost", 9000):
                pass
        self.assertEqual("Can't connect to localhost:9000", str(ex.exception))
        with self.assertRaises(amp.AmpError) as ex:
            with smart_conn.SmartConn(None, False, "not_local_host", 8000):
                pass
        self.assertEqual("Can't connect to not_local_host:8000", str(ex.exception))

    def test_requests(self):
        with smart_conn.SmartConn(None, False, "localhost", 8000) as conn:
            response = conn.request("GET", "good")
            self.assertEqual("A good request", response)
            with self.assertRaises(amp.AmpError) as ex:
                conn.request("GET", "bad")
            self.assertEqual("GET localhost:8000/bad failed with status 400: A bad request", str(ex.exception))


if __name__ == '__main__':
    unittest.main()
