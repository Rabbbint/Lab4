import unittest
from Project import convert_to_moscow_time
from zoneinfo import ZoneInfo
from datetime import datetime

class TestConvertToMoscowTime(unittest.TestCase):
    def test_convert_timestamp_to_moscow_time(self):
        timestamp = 1624621200  # 2021-06-24 12:00:00 UTC
        moscow_time = convert_to_moscow_time(timestamp)
        expected_time = datetime(2021, 6, 25, 14, 40, tzinfo=ZoneInfo('Europe/Moscow'))
        self.assertEqual(moscow_time, expected_time)

    def test_convert_negative_timestamp_to_moscow_time(self):
        timestamp = -3600  # 1970-01-01 00:00:00 UTC
        moscow_time = convert_to_moscow_time(timestamp)
        expected_time = datetime(1970, 1, 1, 2, 0, tzinfo=ZoneInfo('Europe/Moscow'))
        self.assertEqual(moscow_time, expected_time)




