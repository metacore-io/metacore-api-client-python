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


class Organizations(object):
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
        'id': 'OrganizationsId',
        'address': 'str',
        'brand_name': 'str',
        'city': 'str',
        'country': 'str',
        'description': 'str',
        'guid': 'int',
        'is_active': 'bool',
        'loraserver_organization_id': 'int',
        'name': 'str',
        'organization_id': 'OrganizationsId',
        'phone_number': 'str',
        'tax_number': 'int',
        'tax_office': 'str'
    }

    attribute_map = {
        'id': '_id',
        'address': 'address',
        'brand_name': 'brandName',
        'city': 'city',
        'country': 'country',
        'description': 'description',
        'guid': 'guid',
        'is_active': 'isActive',
        'loraserver_organization_id': 'loraserver_organization_id',
        'name': 'name',
        'organization_id': 'organizationId',
        'phone_number': 'phoneNumber',
        'tax_number': 'taxNumber',
        'tax_office': 'taxOffice'
    }

    def __init__(self, id=None, address=None, brand_name=None, city=None, country=None, description=None, guid=1001, is_active=True, loraserver_organization_id=None, name=None, organization_id=None, phone_number=None, tax_number=None, tax_office=None):  # noqa: E501
        """Organizations - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._address = None
        self._brand_name = None
        self._city = None
        self._country = None
        self._description = None
        self._guid = None
        self._is_active = None
        self._loraserver_organization_id = None
        self._name = None
        self._organization_id = None
        self._phone_number = None
        self._tax_number = None
        self._tax_office = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if brand_name is not None:
            self.brand_name = brand_name
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if description is not None:
            self.description = description
        if guid is not None:
            self.guid = guid
        if is_active is not None:
            self.is_active = is_active
        if loraserver_organization_id is not None:
            self.loraserver_organization_id = loraserver_organization_id
        self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        if phone_number is not None:
            self.phone_number = phone_number
        if tax_number is not None:
            self.tax_number = tax_number
        if tax_office is not None:
            self.tax_office = tax_office

    @property
    def id(self):
        """Gets the id of this Organizations.  # noqa: E501


        :return: The id of this Organizations.  # noqa: E501
        :rtype: OrganizationsId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organizations.


        :param id: The id of this Organizations.  # noqa: E501
        :type: OrganizationsId
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this Organizations.  # noqa: E501


        :return: The address of this Organizations.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Organizations.


        :param address: The address of this Organizations.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def brand_name(self):
        """Gets the brand_name of this Organizations.  # noqa: E501


        :return: The brand_name of this Organizations.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this Organizations.


        :param brand_name: The brand_name of this Organizations.  # noqa: E501
        :type: str
        """

        self._brand_name = brand_name

    @property
    def city(self):
        """Gets the city of this Organizations.  # noqa: E501


        :return: The city of this Organizations.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Organizations.


        :param city: The city of this Organizations.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Organizations.  # noqa: E501


        :return: The country of this Organizations.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Organizations.


        :param country: The country of this Organizations.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def description(self):
        """Gets the description of this Organizations.  # noqa: E501


        :return: The description of this Organizations.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Organizations.


        :param description: The description of this Organizations.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def guid(self):
        """Gets the guid of this Organizations.  # noqa: E501


        :return: The guid of this Organizations.  # noqa: E501
        :rtype: int
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Organizations.


        :param guid: The guid of this Organizations.  # noqa: E501
        :type: int
        """

        self._guid = guid

    @property
    def is_active(self):
        """Gets the is_active of this Organizations.  # noqa: E501


        :return: The is_active of this Organizations.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Organizations.


        :param is_active: The is_active of this Organizations.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def loraserver_organization_id(self):
        """Gets the loraserver_organization_id of this Organizations.  # noqa: E501


        :return: The loraserver_organization_id of this Organizations.  # noqa: E501
        :rtype: int
        """
        return self._loraserver_organization_id

    @loraserver_organization_id.setter
    def loraserver_organization_id(self, loraserver_organization_id):
        """Sets the loraserver_organization_id of this Organizations.


        :param loraserver_organization_id: The loraserver_organization_id of this Organizations.  # noqa: E501
        :type: int
        """

        self._loraserver_organization_id = loraserver_organization_id

    @property
    def name(self):
        """Gets the name of this Organizations.  # noqa: E501


        :return: The name of this Organizations.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organizations.


        :param name: The name of this Organizations.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this Organizations.  # noqa: E501


        :return: The organization_id of this Organizations.  # noqa: E501
        :rtype: OrganizationsId
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Organizations.


        :param organization_id: The organization_id of this Organizations.  # noqa: E501
        :type: OrganizationsId
        """

        self._organization_id = organization_id

    @property
    def phone_number(self):
        """Gets the phone_number of this Organizations.  # noqa: E501


        :return: The phone_number of this Organizations.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Organizations.


        :param phone_number: The phone_number of this Organizations.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def tax_number(self):
        """Gets the tax_number of this Organizations.  # noqa: E501


        :return: The tax_number of this Organizations.  # noqa: E501
        :rtype: int
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this Organizations.


        :param tax_number: The tax_number of this Organizations.  # noqa: E501
        :type: int
        """

        self._tax_number = tax_number

    @property
    def tax_office(self):
        """Gets the tax_office of this Organizations.  # noqa: E501


        :return: The tax_office of this Organizations.  # noqa: E501
        :rtype: str
        """
        return self._tax_office

    @tax_office.setter
    def tax_office(self, tax_office):
        """Sets the tax_office of this Organizations.


        :param tax_office: The tax_office of this Organizations.  # noqa: E501
        :type: str
        """

        self._tax_office = tax_office

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
        if issubclass(Organizations, dict):
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
        if not isinstance(other, Organizations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other