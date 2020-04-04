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
from api.oplog_api import OplogApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOplogApi(unittest.TestCase):
    """OplogApi unit test stubs"""

    def setUp(self):
        self.api = api.oplog_api.OplogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_oplog_item(self):
        """Test case for get_oplog_item

        Retrieves a Oplog document  # noqa: E501
        """
        pass

    def test_getoplog(self):
        """Test case for getoplog

        Retrieves one or more oplog  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
