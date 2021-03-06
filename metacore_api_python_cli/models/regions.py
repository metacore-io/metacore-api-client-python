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


class Regions(object):
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
        'id': 'RegionsId',
        'description': 'str',
        'location': 'RegionsLocation',
        'name': 'str',
        'organization_id': 'OrganizationsId'
    }

    attribute_map = {
        'id': '_id',
        'description': 'description',
        'location': 'location',
        'name': 'name',
        'organization_id': 'organizationId'
    }

    def __init__(self, id=None, description=None, location=None, name=None, organization_id=None):  # noqa: E501
        """Regions - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._description = None
        self._location = None
        self._name = None
        self._organization_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.description = description
        if location is not None:
            self.location = location
        self.name = name
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def id(self):
        """Gets the id of this Regions.  # noqa: E501


        :return: The id of this Regions.  # noqa: E501
        :rtype: RegionsId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Regions.


        :param id: The id of this Regions.  # noqa: E501
        :type: RegionsId
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this Regions.  # noqa: E501


        :return: The description of this Regions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Regions.


        :param description: The description of this Regions.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def location(self):
        """Gets the location of this Regions.  # noqa: E501


        :return: The location of this Regions.  # noqa: E501
        :rtype: RegionsLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Regions.


        :param location: The location of this Regions.  # noqa: E501
        :type: RegionsLocation
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this Regions.  # noqa: E501


        :return: The name of this Regions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Regions.


        :param name: The name of this Regions.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this Regions.  # noqa: E501


        :return: The organization_id of this Regions.  # noqa: E501
        :rtype: OrganizationsId
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Regions.


        :param organization_id: The organization_id of this Regions.  # noqa: E501
        :type: OrganizationsId
        """

        self._organization_id = organization_id

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
        if issubclass(Regions, dict):
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
        if not isinstance(other, Regions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
