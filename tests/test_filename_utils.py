# test script for filename_utils
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from filename_utils import sanitize_filename

class TestSanitizeFilename(unittest.TestCase):
    def test_sanitize_common_characters(self):
        self.assertEqual(sanitize_filename("example file*name?.txt"), "example-file-name-.txt")

    def test_sanitize_non_ascii(self):
        self.assertEqual(sanitize_filename("naïve café.txt"), "na-ve-caf-.txt")

    def test_no_change_needed(self):
        self.assertEqual(sanitize_filename("regular_filename.txt"), "regular_filename.txt")

if __name__ == '__main__':
    unittest.main()
