"""
    Tradovate API

    Tradovate API provides an access to the complete set of robust Tradovate functionality.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.prices_api import PricesApi  # noqa: E501


class TestPricesApi(unittest.TestCase):
    """PricesApi unit test stubs"""

    def setUp(self):
        self.api = PricesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_speed(self):
        """Test case for change_speed

        """
        pass

    def test_check_replay_session(self):
        """Test case for check_replay_session

        """
        pass

    def test_initialize_clock(self):
        """Test case for initialize_clock

        """
        pass


if __name__ == '__main__':
    unittest.main()
