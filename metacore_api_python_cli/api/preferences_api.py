# coding: utf-8

"""
    Metacore IoT Object Storage API

    Metacore Object Storage - IOT Core Services  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from metacore_api_python_cli.api_client import ApiClient


class PreferencesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deletepreferences_item(self, preferences_id, if_match, **kwargs):  # noqa: E501
        """Deletes a preferences document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepreferences_item(preferences_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str preferences_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletepreferences_item_with_http_info(preferences_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.deletepreferences_item_with_http_info(preferences_id, if_match, **kwargs)  # noqa: E501
            return data

    def deletepreferences_item_with_http_info(self, preferences_id, if_match, **kwargs):  # noqa: E501
        """Deletes a preferences document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepreferences_item_with_http_info(preferences_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str preferences_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['preferences_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletepreferences_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'preferences_id' is set
        if ('preferences_id' not in params or
                params['preferences_id'] is None):
            raise ValueError("Missing the required parameter `preferences_id` when calling `deletepreferences_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `deletepreferences_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'preferences_id' in params:
            path_params['preferencesId'] = params['preferences_id']  # noqa: E501

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
            '/preferences/{preferencesId}', 'DELETE',
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

    def getpreferences(self, **kwargs):  # noqa: E501
        """Retrieves one or more preferences  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpreferences(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getpreferences_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.getpreferences_with_http_info(**kwargs)  # noqa: E501
            return data

    def getpreferences_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more preferences  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpreferences_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2008
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
                    " to method getpreferences" % key
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
            '/preferences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getpreferences_item(self, preferences_id, **kwargs):  # noqa: E501
        """Retrieves a preferences document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpreferences_item(preferences_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str preferences_id: (required)
        :return: Preferences
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getpreferences_item_with_http_info(preferences_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getpreferences_item_with_http_info(preferences_id, **kwargs)  # noqa: E501
            return data

    def getpreferences_item_with_http_info(self, preferences_id, **kwargs):  # noqa: E501
        """Retrieves a preferences document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpreferences_item_with_http_info(preferences_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str preferences_id: (required)
        :return: Preferences
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['preferences_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getpreferences_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'preferences_id' is set
        if ('preferences_id' not in params or
                params['preferences_id'] is None):
            raise ValueError("Missing the required parameter `preferences_id` when calling `getpreferences_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'preferences_id' in params:
            path_params['preferencesId'] = params['preferences_id']  # noqa: E501

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
            '/preferences/{preferencesId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Preferences',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patchpreferences_item(self, body, if_match, preferences_id, **kwargs):  # noqa: E501
        """Updates a preferences document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchpreferences_item(body, if_match, preferences_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Preferences body: A preferences or list of preferences documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str preferences_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patchpreferences_item_with_http_info(body, if_match, preferences_id, **kwargs)  # noqa: E501
        else:
            (data) = self.patchpreferences_item_with_http_info(body, if_match, preferences_id, **kwargs)  # noqa: E501
            return data

    def patchpreferences_item_with_http_info(self, body, if_match, preferences_id, **kwargs):  # noqa: E501
        """Updates a preferences document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchpreferences_item_with_http_info(body, if_match, preferences_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Preferences body: A preferences or list of preferences documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str preferences_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'preferences_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patchpreferences_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patchpreferences_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `patchpreferences_item`")  # noqa: E501
        # verify the required parameter 'preferences_id' is set
        if ('preferences_id' not in params or
                params['preferences_id'] is None):
            raise ValueError("Missing the required parameter `preferences_id` when calling `patchpreferences_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'preferences_id' in params:
            path_params['preferencesId'] = params['preferences_id']  # noqa: E501

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
            '/preferences/{preferencesId}', 'PATCH',
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

    def postpreferences(self, body, **kwargs):  # noqa: E501
        """Stores one or more preferences.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postpreferences(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Preferences body: A preferences or list of preferences documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postpreferences_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.postpreferences_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def postpreferences_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more preferences.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postpreferences_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Preferences body: A preferences or list of preferences documents (required)
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
                    " to method postpreferences" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postpreferences`")  # noqa: E501

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
            '/preferences', 'POST',
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

    def putpreferences_item(self, body, if_match, preferences_id, **kwargs):  # noqa: E501
        """Replaces a preferences document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putpreferences_item(body, if_match, preferences_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Preferences body: A preferences or list of preferences documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str preferences_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.putpreferences_item_with_http_info(body, if_match, preferences_id, **kwargs)  # noqa: E501
        else:
            (data) = self.putpreferences_item_with_http_info(body, if_match, preferences_id, **kwargs)  # noqa: E501
            return data

    def putpreferences_item_with_http_info(self, body, if_match, preferences_id, **kwargs):  # noqa: E501
        """Replaces a preferences document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putpreferences_item_with_http_info(body, if_match, preferences_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Preferences body: A preferences or list of preferences documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str preferences_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'preferences_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putpreferences_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `putpreferences_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `putpreferences_item`")  # noqa: E501
        # verify the required parameter 'preferences_id' is set
        if ('preferences_id' not in params or
                params['preferences_id'] is None):
            raise ValueError("Missing the required parameter `preferences_id` when calling `putpreferences_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'preferences_id' in params:
            path_params['preferencesId'] = params['preferences_id']  # noqa: E501

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
            '/preferences/{preferencesId}', 'PUT',
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