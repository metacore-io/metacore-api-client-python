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


class TenantsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deletetenants_item(self, tenants_id, if_match, **kwargs):  # noqa: E501
        """Deletes a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletetenants_item(tenants_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenants_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletetenants_item_with_http_info(tenants_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.deletetenants_item_with_http_info(tenants_id, if_match, **kwargs)  # noqa: E501
            return data

    def deletetenants_item_with_http_info(self, tenants_id, if_match, **kwargs):  # noqa: E501
        """Deletes a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletetenants_item_with_http_info(tenants_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenants_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenants_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletetenants_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenants_id' is set
        if ('tenants_id' not in params or
                params['tenants_id'] is None):
            raise ValueError("Missing the required parameter `tenants_id` when calling `deletetenants_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `deletetenants_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenants_id' in params:
            path_params['tenantsId'] = params['tenants_id']  # noqa: E501

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
            '/tenants/{tenantsId}', 'DELETE',
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

    def gettenants(self, **kwargs):  # noqa: E501
        """Retrieves one or more tenants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gettenants(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gettenants_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.gettenants_with_http_info(**kwargs)  # noqa: E501
            return data

    def gettenants_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more tenants  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gettenants_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse20012
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
                    " to method gettenants" % key
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
            '/tenants', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def gettenants_item(self, tenants_id, **kwargs):  # noqa: E501
        """Retrieves a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gettenants_item(tenants_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenants_id: (required)
        :return: Tenants
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gettenants_item_with_http_info(tenants_id, **kwargs)  # noqa: E501
        else:
            (data) = self.gettenants_item_with_http_info(tenants_id, **kwargs)  # noqa: E501
            return data

    def gettenants_item_with_http_info(self, tenants_id, **kwargs):  # noqa: E501
        """Retrieves a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gettenants_item_with_http_info(tenants_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenants_id: (required)
        :return: Tenants
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenants_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gettenants_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenants_id' is set
        if ('tenants_id' not in params or
                params['tenants_id'] is None):
            raise ValueError("Missing the required parameter `tenants_id` when calling `gettenants_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenants_id' in params:
            path_params['tenantsId'] = params['tenants_id']  # noqa: E501

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
            '/tenants/{tenantsId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tenants',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patchtenants_item(self, body, if_match, tenants_id, **kwargs):  # noqa: E501
        """Updates a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchtenants_item(body, if_match, tenants_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tenants body: A tenants or list of tenants documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str tenants_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patchtenants_item_with_http_info(body, if_match, tenants_id, **kwargs)  # noqa: E501
        else:
            (data) = self.patchtenants_item_with_http_info(body, if_match, tenants_id, **kwargs)  # noqa: E501
            return data

    def patchtenants_item_with_http_info(self, body, if_match, tenants_id, **kwargs):  # noqa: E501
        """Updates a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchtenants_item_with_http_info(body, if_match, tenants_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tenants body: A tenants or list of tenants documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str tenants_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'tenants_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patchtenants_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patchtenants_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `patchtenants_item`")  # noqa: E501
        # verify the required parameter 'tenants_id' is set
        if ('tenants_id' not in params or
                params['tenants_id'] is None):
            raise ValueError("Missing the required parameter `tenants_id` when calling `patchtenants_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenants_id' in params:
            path_params['tenantsId'] = params['tenants_id']  # noqa: E501

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
            '/tenants/{tenantsId}', 'PATCH',
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

    def posttenants(self, body, **kwargs):  # noqa: E501
        """Stores one or more tenants.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.posttenants(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tenants body: A tenants or list of tenants documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.posttenants_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.posttenants_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def posttenants_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more tenants.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.posttenants_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tenants body: A tenants or list of tenants documents (required)
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
                    " to method posttenants" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `posttenants`")  # noqa: E501

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
            '/tenants', 'POST',
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

    def puttenants_item(self, body, if_match, tenants_id, **kwargs):  # noqa: E501
        """Replaces a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.puttenants_item(body, if_match, tenants_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tenants body: A tenants or list of tenants documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str tenants_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.puttenants_item_with_http_info(body, if_match, tenants_id, **kwargs)  # noqa: E501
        else:
            (data) = self.puttenants_item_with_http_info(body, if_match, tenants_id, **kwargs)  # noqa: E501
            return data

    def puttenants_item_with_http_info(self, body, if_match, tenants_id, **kwargs):  # noqa: E501
        """Replaces a tenants document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.puttenants_item_with_http_info(body, if_match, tenants_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tenants body: A tenants or list of tenants documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str tenants_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'tenants_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method puttenants_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `puttenants_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `puttenants_item`")  # noqa: E501
        # verify the required parameter 'tenants_id' is set
        if ('tenants_id' not in params or
                params['tenants_id'] is None):
            raise ValueError("Missing the required parameter `tenants_id` when calling `puttenants_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenants_id' in params:
            path_params['tenantsId'] = params['tenants_id']  # noqa: E501

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
            '/tenants/{tenantsId}', 'PUT',
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