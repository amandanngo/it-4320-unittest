import unittest
import re

def valid_symbol(symbol):
    match = re.fullmatch(r'[A-Z]{1,7}', symbol)
    if match == None:
        return False
    else:
        return True
    
def valid_chart(chart):
    if chart == '1' or chart == '2':
        return True
    else:
        return False
    
def valid_time_series(time_series):
    match = re.fullmatch(r'[1-4]', time_series)
    if match == None:
        return False
    else:
        return True
    
def valid_date(date):
    match = re.fullmatch(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$', date)
    if match == None:
        return False
    else:
        return True

class TestInput(unittest.TestCase):
    def test_symbol(self):
        self.assertTrue(valid_symbol("AAPL"))
        self.assertFalse(valid_symbol("asdfghghjj"))

    def test_chart(self):
        self.assertTrue(valid_chart("1"))
        self.assertTrue(valid_chart("2"))
        self.assertFalse(valid_chart("3"))

    def test_time_series(self):
        self.assertTrue(valid_time_series("1"))
        self.assertTrue(valid_time_series("4"))
        self.assertFalse(valid_time_series("6"))

    def test_start_date(self):
        self.assertTrue(valid_date("2002-01-01"))
        self.assertTrue(valid_date("2025-05-31"))
        self.assertFalse(valid_date("213-023-123"))
        self.assertFalse(valid_date("2013-23-43"))

    def test_end_date(self):
        self.assertTrue(valid_date("2002-01-01"))
        self.assertTrue(valid_date("2025-05-31"))
        self.assertFalse(valid_date("213-023-123"))
        self.assertFalse(valid_date("2013-23-43"))

if "__name__" == '__main__':
    unittest.main()