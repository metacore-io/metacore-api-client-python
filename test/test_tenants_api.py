# coding: utf-8

"""
    Metacore IoT Object Storage API

    Metacore Object Storage - IOT Core Services  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import metacore_api_python_cli
from api.tenants_api import TenantsApi  # noqa: E501
from metacore_api_python_cli.rest import ApiException


class TestTenantsApi(unittest.TestCase):
    """TenantsApi unit test stubs"""

    def setUp(self):
        self.api = api.tenants_api.TenantsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deletetenants_item(self):
        """Test case for deletetenants_item

        Deletes a tenants document  # noqa: E501
        """
        pass

    def test_gettenants(self):
        """Test case for gettenants

        Retrieves one or more tenants  # noqa: E501
        """
        pass

    def test_gettenants_item(self):
        """Test case for gettenants_item

        Retrieves a tenants document  # noqa: E501
        """
        pass

    def test_patchtenants_item(self):
        """Test case for patchtenants_item

        Updates a tenants document  # noqa: E501
        """
        pass

    def test_posttenants(self):
        """Test case for posttenants

        Stores one or more tenants.  # noqa: E501
        """
        pass

    def test_puttenants_item(self):
        """Test case for puttenants_item

        Replaces a tenants document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
