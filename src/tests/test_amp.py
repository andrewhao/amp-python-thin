import unittest
import amp


class TestAmp(unittest.TestCase):
    def test_no_key(self):
        with self.assertRaises(amp.AmpError) as ex:
            amp.Amp("", "amp_agents")
        self.assertEqual("'key' can't not be empty", str(ex.exception))

    def test_no_amp_agents(self):
        with self.assertRaises(amp.AmpError) as ex:
            amp.Amp("key", "")
        self.assertEqual("'amp_agents' can't be empty", str(ex.exception))

    def test_bad_amp_agent(self):
        with self.assertRaises(amp.AmpError) as ex:
            amp.Amp.parse_agent("bad_amp_agent")
        self.assertEqual('bad amp agent bad_amp_agent', str(ex.exception))

    def test_bad_protocol(self):
        with self.assertRaises(amp.AmpError) as ex:
            amp.Amp.parse_agent("ftp://ftp_server")
        self.assertEqual("method in ftp://ftp_server must be 'http' or 'https'", str(ex.exception))

    def test_good_agents(self):
        http, host, port = amp.Amp.parse_agent("http://localhost:8080")
        self.assertFalse(http)
        self.assertEqual("localhost", host)
        self.assertEqual(8080, port)
        http, host, port = amp.Amp.parse_agent("http://localhost")
        self.assertFalse(http)
        self.assertEqual("localhost", host)
        self.assertEqual(8100, port)
        http, host, port = amp.Amp.parse_agent("https://localhost:8080")
        self.assertTrue(http)
        self.assertEqual("localhost", host)
        self.assertEqual(8080, port)
        http, host, port = amp.Amp.parse_agent("https://localhost")
        self.assertTrue(http)
        self.assertEqual("localhost", host)
        self.assertEqual(8100, port)


if __name__ == '__main__':
    unittest.main()
