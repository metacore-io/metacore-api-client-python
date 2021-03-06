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


class Hardwares(object):
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
        'id': 'str',
        'capabilities': 'list[str]',
        'claimed': 'bool',
        'claimed_at': 'datetime',
        'claimed_by': 'UsersId',
        'claimed_until': 'datetime',
        'color_code': 'str',
        'description': 'str',
        'desired': 'int',
        'device_id': 'DevicesId',
        'gpio_pin': 'int',
        'name': 'str',
        'organization_id': 'OrganizationsId',
        'output_id': 'int',
        'reported': 'int'
    }

    attribute_map = {
        'id': '_id',
        'capabilities': 'capabilities',
        'claimed': 'claimed',
        'claimed_at': 'claimed_at',
        'claimed_by': 'claimed_by',
        'claimed_until': 'claimed_until',
        'color_code': 'color_code',
        'description': 'description',
        'desired': 'desired',
        'device_id': 'deviceId',
        'gpio_pin': 'gpio_pin',
        'name': 'name',
        'organization_id': 'organizationId',
        'output_id': 'output_id',
        'reported': 'reported'
    }

    def __init__(self, id=None, capabilities=None, claimed=False, claimed_at=None, claimed_by=None, claimed_until=None, color_code=None, description='', desired=0, device_id=None, gpio_pin=None, name=None, organization_id=None, output_id=0, reported=None):  # noqa: E501
        """Hardwares - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._capabilities = None
        self._claimed = None
        self._claimed_at = None
        self._claimed_by = None
        self._claimed_until = None
        self._color_code = None
        self._description = None
        self._desired = None
        self._device_id = None
        self._gpio_pin = None
        self._name = None
        self._organization_id = None
        self._output_id = None
        self._reported = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if capabilities is not None:
            self.capabilities = capabilities
        if claimed is not None:
            self.claimed = claimed
        if claimed_at is not None:
            self.claimed_at = claimed_at
        if claimed_by is not None:
            self.claimed_by = claimed_by
        if claimed_until is not None:
            self.claimed_until = claimed_until
        if color_code is not None:
            self.color_code = color_code
        if description is not None:
            self.description = description
        if desired is not None:
            self.desired = desired
        self.device_id = device_id
        self.gpio_pin = gpio_pin
        self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        if output_id is not None:
            self.output_id = output_id
        if reported is not None:
            self.reported = reported

    @property
    def id(self):
        """Gets the id of this Hardwares.  # noqa: E501


        :return: The id of this Hardwares.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Hardwares.


        :param id: The id of this Hardwares.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def capabilities(self):
        """Gets the capabilities of this Hardwares.  # noqa: E501


        :return: The capabilities of this Hardwares.  # noqa: E501
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this Hardwares.


        :param capabilities: The capabilities of this Hardwares.  # noqa: E501
        :type: list[str]
        """

        self._capabilities = capabilities

    @property
    def claimed(self):
        """Gets the claimed of this Hardwares.  # noqa: E501


        :return: The claimed of this Hardwares.  # noqa: E501
        :rtype: bool
        """
        return self._claimed

    @claimed.setter
    def claimed(self, claimed):
        """Sets the claimed of this Hardwares.


        :param claimed: The claimed of this Hardwares.  # noqa: E501
        :type: bool
        """

        self._claimed = claimed

    @property
    def claimed_at(self):
        """Gets the claimed_at of this Hardwares.  # noqa: E501


        :return: The claimed_at of this Hardwares.  # noqa: E501
        :rtype: datetime
        """
        return self._claimed_at

    @claimed_at.setter
    def claimed_at(self, claimed_at):
        """Sets the claimed_at of this Hardwares.


        :param claimed_at: The claimed_at of this Hardwares.  # noqa: E501
        :type: datetime
        """

        self._claimed_at = claimed_at

    @property
    def claimed_by(self):
        """Gets the claimed_by of this Hardwares.  # noqa: E501


        :return: The claimed_by of this Hardwares.  # noqa: E501
        :rtype: UsersId
        """
        return self._claimed_by

    @claimed_by.setter
    def claimed_by(self, claimed_by):
        """Sets the claimed_by of this Hardwares.


        :param claimed_by: The claimed_by of this Hardwares.  # noqa: E501
        :type: UsersId
        """

        self._claimed_by = claimed_by

    @property
    def claimed_until(self):
        """Gets the claimed_until of this Hardwares.  # noqa: E501


        :return: The claimed_until of this Hardwares.  # noqa: E501
        :rtype: datetime
        """
        return self._claimed_until

    @claimed_until.setter
    def claimed_until(self, claimed_until):
        """Sets the claimed_until of this Hardwares.


        :param claimed_until: The claimed_until of this Hardwares.  # noqa: E501
        :type: datetime
        """

        self._claimed_until = claimed_until

    @property
    def color_code(self):
        """Gets the color_code of this Hardwares.  # noqa: E501


        :return: The color_code of this Hardwares.  # noqa: E501
        :rtype: str
        """
        return self._color_code

    @color_code.setter
    def color_code(self, color_code):
        """Sets the color_code of this Hardwares.


        :param color_code: The color_code of this Hardwares.  # noqa: E501
        :type: str
        """

        self._color_code = color_code

    @property
    def description(self):
        """Gets the description of this Hardwares.  # noqa: E501


        :return: The description of this Hardwares.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Hardwares.


        :param description: The description of this Hardwares.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def desired(self):
        """Gets the desired of this Hardwares.  # noqa: E501


        :return: The desired of this Hardwares.  # noqa: E501
        :rtype: int
        """
        return self._desired

    @desired.setter
    def desired(self, desired):
        """Sets the desired of this Hardwares.


        :param desired: The desired of this Hardwares.  # noqa: E501
        :type: int
        """

        self._desired = desired

    @property
    def device_id(self):
        """Gets the device_id of this Hardwares.  # noqa: E501


        :return: The device_id of this Hardwares.  # noqa: E501
        :rtype: DevicesId
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Hardwares.


        :param device_id: The device_id of this Hardwares.  # noqa: E501
        :type: DevicesId
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def gpio_pin(self):
        """Gets the gpio_pin of this Hardwares.  # noqa: E501


        :return: The gpio_pin of this Hardwares.  # noqa: E501
        :rtype: int
        """
        return self._gpio_pin

    @gpio_pin.setter
    def gpio_pin(self, gpio_pin):
        """Sets the gpio_pin of this Hardwares.


        :param gpio_pin: The gpio_pin of this Hardwares.  # noqa: E501
        :type: int
        """
        if gpio_pin is None:
            raise ValueError("Invalid value for `gpio_pin`, must not be `None`")  # noqa: E501

        self._gpio_pin = gpio_pin

    @property
    def name(self):
        """Gets the name of this Hardwares.  # noqa: E501


        :return: The name of this Hardwares.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Hardwares.


        :param name: The name of this Hardwares.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this Hardwares.  # noqa: E501


        :return: The organization_id of this Hardwares.  # noqa: E501
        :rtype: OrganizationsId
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Hardwares.


        :param organization_id: The organization_id of this Hardwares.  # noqa: E501
        :type: OrganizationsId
        """

        self._organization_id = organization_id

    @property
    def output_id(self):
        """Gets the output_id of this Hardwares.  # noqa: E501


        :return: The output_id of this Hardwares.  # noqa: E501
        :rtype: int
        """
        return self._output_id

    @output_id.setter
    def output_id(self, output_id):
        """Sets the output_id of this Hardwares.


        :param output_id: The output_id of this Hardwares.  # noqa: E501
        :type: int
        """

        self._output_id = output_id

    @property
    def reported(self):
        """Gets the reported of this Hardwares.  # noqa: E501


        :return: The reported of this Hardwares.  # noqa: E501
        :rtype: int
        """
        return self._reported

    @reported.setter
    def reported(self, reported):
        """Sets the reported of this Hardwares.


        :param reported: The reported of this Hardwares.  # noqa: E501
        :type: int
        """

        self._reported = reported

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
        if issubclass(Hardwares, dict):
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
        if not isinstance(other, Hardwares):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
