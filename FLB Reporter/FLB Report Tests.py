import unittest

class TestReportTools(unittest.TestCase):

    def test_find_logs(self):
        from main.py import get_files_from_dir
        self.assertGreater(len(get_files_from_dir('Logs')),0)


