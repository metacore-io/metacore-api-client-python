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


class PreferencesDashboards(object):
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
        'name': 'str',
        'uid': 'str',
        'widgets': 'list[PreferencesWidgets]'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'widgets': 'widgets'
    }

    def __init__(self, name=None, uid=None, widgets=None):  # noqa: E501
        """PreferencesDashboards - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._uid = None
        self._widgets = None
        self.discriminator = None
        self.name = name
        self.uid = uid
        if widgets is not None:
            self.widgets = widgets

    @property
    def name(self):
        """Gets the name of this PreferencesDashboards.  # noqa: E501


        :return: The name of this PreferencesDashboards.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PreferencesDashboards.


        :param name: The name of this PreferencesDashboards.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this PreferencesDashboards.  # noqa: E501


        :return: The uid of this PreferencesDashboards.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this PreferencesDashboards.


        :param uid: The uid of this PreferencesDashboards.  # noqa: E501
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def widgets(self):
        """Gets the widgets of this PreferencesDashboards.  # noqa: E501


        :return: The widgets of this PreferencesDashboards.  # noqa: E501
        :rtype: list[PreferencesWidgets]
        """
        return self._widgets

    @widgets.setter
    def widgets(self, widgets):
        """Sets the widgets of this PreferencesDashboards.


        :param widgets: The widgets of this PreferencesDashboards.  # noqa: E501
        :type: list[PreferencesWidgets]
        """

        self._widgets = widgets

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
        if issubclass(PreferencesDashboards, dict):
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
        if not isinstance(other, PreferencesDashboards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
