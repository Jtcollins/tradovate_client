"""
    Tradovate API

    Tradovate API provides an access to the complete set of robust Tradovate functionality.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.authentication_api import AuthenticationApi  # noqa: E501


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_access_token_request(self):
        """Test case for access_token_request

        """
        pass

    def test_me(self):
        """Test case for me

        """
        pass

    def test_o_auth_token(self):
        """Test case for o_auth_token

        """
        pass

    def test_renew_access_token(self):
        """Test case for renew_access_token

        """
        pass


if __name__ == '__main__':
    unittest.main()
