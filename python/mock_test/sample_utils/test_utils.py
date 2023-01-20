#!/usr/bin/env python3

"""Sample for Python unittest"""

import os
import unittest
from unittest import mock
import utils
import errno

class TestUtils(unittest.TestCase):

    @mock.patch("os.makedirs")
    def test_mkdir_p(self, mock_mkdir_p):
        utils.mkdir_p("/tmp/mock-mock-mock")

        mock_mkdir_p.assert_called_with("/tmp/mock-mock-mock")

    @mock.patch("os.path")
    @mock.patch("os.makedirs")
    def test_raise_oserror(self, mock_mkdir_p, mock_os_path):
        mock_mkdir_p.side_effect = (OSError())
        self.assertRaises(OSError, utils.mkdir_p, "/tmp/mock-mock-mock")


if __name__ == "__main__":
    unittest.main()
