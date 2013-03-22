from countdown import parse_time, decr_time
import unittest


class Test_Countdown(unittest.TestCase):

    def test_parse_time(self):
        ''' parse_time should return a tuple of (h, m, s) '''
        time = '30'
        self.assertEqual(parse_time(time), [0,0,30])
        time = '1h2m3'
        self.assertEqual(parse_time(time), [1,2,3])
        time = '20m20'
        self.assertEqual(parse_time(time), [0,20,20])
        time = '160'
        self.assertEqual(parse_time(time), [0,0,160])

    def test_decr_time(self):
        time = '1h2m'
        self.assertEqual(decr_time(time), [1,2,59])
        time = '1h'
        self.assertEqual(decr_time(time), [0,59,0])
