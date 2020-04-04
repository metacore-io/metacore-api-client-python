# coding: utf-8

"""
    Metacore IoT Object Storage API

    Metacore Object Storage - IOT Core Services  # noqa: E501

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deleteusers_item(self, users_id, if_match, **kwargs):  # noqa: E501
        """Deletes a users document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deleteusers_item(users_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str users_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deleteusers_item_with_http_info(users_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.deleteusers_item_with_http_info(users_id, if_match, **kwargs)  # noqa: E501
            return data

    def deleteusers_item_with_http_info(self, users_id, if_match, **kwargs):  # noqa: E501
        """Deletes a users document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deleteusers_item_with_http_info(users_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str users_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['users_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deleteusers_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'users_id' is set
        if ('users_id' not in params or
                params['users_id'] is None):
            raise ValueError("Missing the required parameter `users_id` when calling `deleteusers_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `deleteusers_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'users_id' in params:
            path_params['usersId'] = params['users_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users/{usersId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getusers(self, **kwargs):  # noqa: E501
        """Retrieves one or more users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getusers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getusers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.getusers_with_http_info(**kwargs)  # noqa: E501
            return data

    def getusers_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getusers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['where', 'sort', 'page', 'max_results']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getusers" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'max_results' in params:
            query_params.append(('max_results', params['max_results']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getusers_item(self, users_id, **kwargs):  # noqa: E501
        """Retrieves a users document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getusers_item(users_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str users_id: (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getusers_item_with_http_info(users_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getusers_item_with_http_info(users_id, **kwargs)  # noqa: E501
            return data

    def getusers_item_with_http_info(self, users_id, **kwargs):  # noqa: E501
        """Retrieves a users document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getusers_item_with_http_info(users_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str users_id: (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['users_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getusers_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'users_id' is set
        if ('users_id' not in params or
                params['users_id'] is None):
            raise ValueError("Missing the required parameter `users_id` when calling `getusers_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'users_id' in params:
            path_params['usersId'] = params['users_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users/{usersId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Users',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patchusers_item(self, body, if_match, users_id, **kwargs):  # noqa: E501
        """Updates a users document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchusers_item(body, if_match, users_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Users body: A users or list of users documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str users_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patchusers_item_with_http_info(body, if_match, users_id, **kwargs)  # noqa: E501
        else:
            (data) = self.patchusers_item_with_http_info(body, if_match, users_id, **kwargs)  # noqa: E501
            return data

    def patchusers_item_with_http_info(self, body, if_match, users_id, **kwargs):  # noqa: E501
        """Updates a users document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchusers_item_with_http_info(body, if_match, users_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Users body: A users or list of users documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str users_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'users_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patchusers_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patchusers_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `patchusers_item`")  # noqa: E501
        # verify the required parameter 'users_id' is set
        if ('users_id' not in params or
                params['users_id'] is None):
            raise ValueError("Missing the required parameter `users_id` when calling `patchusers_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'users_id' in params:
            path_params['usersId'] = params['users_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users/{usersId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def postusers(self, body, **kwargs):  # noqa: E501
        """Stores one or more users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postusers(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Users body: A users or list of users documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postusers_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.postusers_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def postusers_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postusers_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Users body: A users or list of users documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postusers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postusers`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def putusers_item(self, body, if_match, users_id, **kwargs):  # noqa: E501
        """Replaces a users document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putusers_item(body, if_match, users_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Users body: A users or list of users documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str users_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.putusers_item_with_http_info(body, if_match, users_id, **kwargs)  # noqa: E501
        else:
            (data) = self.putusers_item_with_http_info(body, if_match, users_id, **kwargs)  # noqa: E501
            return data

    def putusers_item_with_http_info(self, body, if_match, users_id, **kwargs):  # noqa: E501
        """Replaces a users document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putusers_item_with_http_info(body, if_match, users_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Users body: A users or list of users documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str users_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'users_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putusers_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `putusers_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `putusers_item`")  # noqa: E501
        # verify the required parameter 'users_id' is set
        if ('users_id' not in params or
                params['users_id'] is None):
            raise ValueError("Missing the required parameter `users_id` when calling `putusers_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'users_id' in params:
            path_params['usersId'] = params['users_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users/{usersId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)