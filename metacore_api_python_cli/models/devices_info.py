# coding: utf-8

"""
    Metacore IoT Object Storage API

    Metacore Object Storage - IOT Core Services  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class DevicesInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'battery_operated': 'bool',
        'hw_version': 'str',
        'lora_mac': 'str',
        'manufacturer': 'str',
        'serial_no': 'str',
        'status': 'str',
        'sw_version': 'str'
    }

    attribute_map = {
        'battery_operated': 'battery_operated',
        'hw_version': 'hw_version',
        'lora_mac': 'lora_mac',
        'manufacturer': 'manufacturer',
        'serial_no': 'serial_no',
        'status': 'status',
        'sw_version': 'sw_version'
    }

    def __init__(self, battery_operated=False, hw_version=None, lora_mac=None, manufacturer=None, serial_no=None, status=None, sw_version=None):  # noqa: E501
        """DevicesInfo - a model defined in Swagger"""  # noqa: E501
        self._battery_operated = None
        self._hw_version = None
        self._lora_mac = None
        self._manufacturer = None
        self._serial_no = None
        self._status = None
        self._sw_version = None
        self.discriminator = None
        if battery_operated is not None:
            self.battery_operated = battery_operated
        if hw_version is not None:
            self.hw_version = hw_version
        if lora_mac is not None:
            self.lora_mac = lora_mac
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if serial_no is not None:
            self.serial_no = serial_no
        if status is not None:
            self.status = status
        if sw_version is not None:
            self.sw_version = sw_version

    @property
    def battery_operated(self):
        """Gets the battery_operated of this DevicesInfo.  # noqa: E501


        :return: The battery_operated of this DevicesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._battery_operated

    @battery_operated.setter
    def battery_operated(self, battery_operated):
        """Sets the battery_operated of this DevicesInfo.


        :param battery_operated: The battery_operated of this DevicesInfo.  # noqa: E501
        :type: bool
        """

        self._battery_operated = battery_operated

    @property
    def hw_version(self):
        """Gets the hw_version of this DevicesInfo.  # noqa: E501


        :return: The hw_version of this DevicesInfo.  # noqa: E501
        :rtype: str
        """
        return self._hw_version

    @hw_version.setter
    def hw_version(self, hw_version):
        """Sets the hw_version of this DevicesInfo.


        :param hw_version: The hw_version of this DevicesInfo.  # noqa: E501
        :type: str
        """

        self._hw_version = hw_version

    @property
    def lora_mac(self):
        """Gets the lora_mac of this DevicesInfo.  # noqa: E501


        :return: The lora_mac of this DevicesInfo.  # noqa: E501
        :rtype: str
        """
        return self._lora_mac

    @lora_mac.setter
    def lora_mac(self, lora_mac):
        """Sets the lora_mac of this DevicesInfo.


        :param lora_mac: The lora_mac of this DevicesInfo.  # noqa: E501
        :type: str
        """

        self._lora_mac = lora_mac

    @property
    def manufacturer(self):
        """Gets the manufacturer of this DevicesInfo.  # noqa: E501


        :return: The manufacturer of this DevicesInfo.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this DevicesInfo.


        :param manufacturer: The manufacturer of this DevicesInfo.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def serial_no(self):
        """Gets the serial_no of this DevicesInfo.  # noqa: E501


        :return: The serial_no of this DevicesInfo.  # noqa: E501
        :rtype: str
        """
        return self._serial_no

    @serial_no.setter
    def serial_no(self, serial_no):
        """Sets the serial_no of this DevicesInfo.


        :param serial_no: The serial_no of this DevicesInfo.  # noqa: E501
        :type: str
        """

        self._serial_no = serial_no

    @property
    def status(self):
        """Gets the status of this DevicesInfo.  # noqa: E501


        :return: The status of this DevicesInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DevicesInfo.


        :param status: The status of this DevicesInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sw_version(self):
        """Gets the sw_version of this DevicesInfo.  # noqa: E501


        :return: The sw_version of this DevicesInfo.  # noqa: E501
        :rtype: str
        """
        return self._sw_version

    @sw_version.setter
    def sw_version(self, sw_version):
        """Sets the sw_version of this DevicesInfo.


        :param sw_version: The sw_version of this DevicesInfo.  # noqa: E501
        :type: str
        """

        self._sw_version = sw_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DevicesInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DevicesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
