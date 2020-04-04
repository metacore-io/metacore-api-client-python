# coding: utf-8

"""
    Metacore IoT Object Storage API

    Metacore Object Storage - IOT Core Services  # noqa: E501

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.regions_api import RegionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRegionsApi(unittest.TestCase):
    """RegionsApi unit test stubs"""

    def setUp(self):
        self.api = api.regions_api.RegionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deleteregions_item(self):
        """Test case for deleteregions_item

        Deletes a regions document  # noqa: E501
        """
        pass

    def test_getregions(self):
        """Test case for getregions

        Retrieves one or more regions  # noqa: E501
        """
        pass

    def test_getregions_item(self):
        """Test case for getregions_item

        Retrieves a regions document  # noqa: E501
        """
        pass

    def test_patchregions_item(self):
        """Test case for patchregions_item

        Updates a regions document  # noqa: E501
        """
        pass

    def test_postregions(self):
        """Test case for postregions

        Stores one or more regions.  # noqa: E501
        """
        pass

    def test_putregions_item(self):
        """Test case for putregions_item

        Replaces a regions document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()