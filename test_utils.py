import unittest
import datetime
from utils import convert_to_moscow_time

class TestUtils(unittest.TestCase):
    def test_convert_to_moscow_time(self):
        file_list = [
            {"Last Modification Time": datetime.datetime(2023, 4, 1, 12, 0, 0)},
            {"Last Modification Time": datetime.datetime(2023, 4, 1, 15, 0, 0)}
        ]

        converted_list = convert_to_moscow_time(file_list)

        self.assertEqual(converted_list[0]["Last Modification Time"], datetime.datetime(2023, 4, 1, 15, 0, 0))
        self.assertEqual(converted_list[1]["Last Modification Time"], datetime.datetime(2023, 4, 1, 18, 0, 0))

if __name__ == '__main__':
    unittest.main()
