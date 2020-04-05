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
from api.devices_api import DevicesApi  # noqa: E501
from metacore_api_python_cli.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deletedevices_item(self):
        """Test case for deletedevices_item

        Deletes a devices document  # noqa: E501
        """
        pass

    def test_getdevices(self):
        """Test case for getdevices

        Retrieves one or more devices  # noqa: E501
        """
        pass

    def test_getdevices_item(self):
        """Test case for getdevices_item

        Retrieves a devices document  # noqa: E501
        """
        pass

    def test_patchdevices_item(self):
        """Test case for patchdevices_item

        Updates a devices document  # noqa: E501
        """
        pass

    def test_postdevices(self):
        """Test case for postdevices

        Stores one or more devices.  # noqa: E501
        """
        pass

    def test_putdevices_item(self):
        """Test case for putdevices_item

        Replaces a devices document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
