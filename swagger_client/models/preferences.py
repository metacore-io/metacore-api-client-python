# coding: utf-8

"""
    Metacore IoT Object Storage API

    Metacore Object Storage - IOT Core Services  # noqa: E501

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Preferences(object):
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
        'dashboards': 'list[PreferencesDashboards]',
        'organization_id': 'OrganizationsId',
        'user_id': 'UsersId'
    }

    attribute_map = {
        'id': '_id',
        'dashboards': 'dashboards',
        'organization_id': 'organizationId',
        'user_id': 'userId'
    }

    def __init__(self, id=None, dashboards=None, organization_id=None, user_id=None):  # noqa: E501
        """Preferences - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._dashboards = None
        self._organization_id = None
        self._user_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if dashboards is not None:
            self.dashboards = dashboards
        if organization_id is not None:
            self.organization_id = organization_id
        self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this Preferences.  # noqa: E501


        :return: The id of this Preferences.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Preferences.


        :param id: The id of this Preferences.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def dashboards(self):
        """Gets the dashboards of this Preferences.  # noqa: E501


        :return: The dashboards of this Preferences.  # noqa: E501
        :rtype: list[PreferencesDashboards]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Sets the dashboards of this Preferences.


        :param dashboards: The dashboards of this Preferences.  # noqa: E501
        :type: list[PreferencesDashboards]
        """

        self._dashboards = dashboards

    @property
    def organization_id(self):
        """Gets the organization_id of this Preferences.  # noqa: E501


        :return: The organization_id of this Preferences.  # noqa: E501
        :rtype: OrganizationsId
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Preferences.


        :param organization_id: The organization_id of this Preferences.  # noqa: E501
        :type: OrganizationsId
        """

        self._organization_id = organization_id

    @property
    def user_id(self):
        """Gets the user_id of this Preferences.  # noqa: E501


        :return: The user_id of this Preferences.  # noqa: E501
        :rtype: UsersId
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Preferences.


        :param user_id: The user_id of this Preferences.  # noqa: E501
        :type: UsersId
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if issubclass(Preferences, dict):
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
        if not isinstance(other, Preferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
