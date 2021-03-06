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


class HardwaresApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deletehardwares_item(self, hardwares_id, if_match, **kwargs):  # noqa: E501
        """Deletes a hardwares document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletehardwares_item(hardwares_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hardwares_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletehardwares_item_with_http_info(hardwares_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.deletehardwares_item_with_http_info(hardwares_id, if_match, **kwargs)  # noqa: E501
            return data

    def deletehardwares_item_with_http_info(self, hardwares_id, if_match, **kwargs):  # noqa: E501
        """Deletes a hardwares document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletehardwares_item_with_http_info(hardwares_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hardwares_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardwares_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletehardwares_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardwares_id' is set
        if ('hardwares_id' not in params or
                params['hardwares_id'] is None):
            raise ValueError("Missing the required parameter `hardwares_id` when calling `deletehardwares_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `deletehardwares_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardwares_id' in params:
            path_params['hardwaresId'] = params['hardwares_id']  # noqa: E501

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
            '/hardwares/{hardwaresId}', 'DELETE',
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

    def gethardwares(self, **kwargs):  # noqa: E501
        """Retrieves one or more hardwares  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gethardwares(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gethardwares_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.gethardwares_with_http_info(**kwargs)  # noqa: E501
            return data

    def gethardwares_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more hardwares  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gethardwares_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2002
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
                    " to method gethardwares" % key
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
            '/hardwares', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def gethardwares_item(self, hardwares_id, **kwargs):  # noqa: E501
        """Retrieves a hardwares document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gethardwares_item(hardwares_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hardwares_id: (required)
        :return: Hardwares
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gethardwares_item_with_http_info(hardwares_id, **kwargs)  # noqa: E501
        else:
            (data) = self.gethardwares_item_with_http_info(hardwares_id, **kwargs)  # noqa: E501
            return data

    def gethardwares_item_with_http_info(self, hardwares_id, **kwargs):  # noqa: E501
        """Retrieves a hardwares document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gethardwares_item_with_http_info(hardwares_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str hardwares_id: (required)
        :return: Hardwares
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardwares_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gethardwares_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'hardwares_id' is set
        if ('hardwares_id' not in params or
                params['hardwares_id'] is None):
            raise ValueError("Missing the required parameter `hardwares_id` when calling `gethardwares_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardwares_id' in params:
            path_params['hardwaresId'] = params['hardwares_id']  # noqa: E501

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
            '/hardwares/{hardwaresId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Hardwares',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patchhardwares_item(self, body, if_match, hardwares_id, **kwargs):  # noqa: E501
        """Updates a hardwares document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchhardwares_item(body, if_match, hardwares_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Hardwares body: A hardwares or list of hardwares documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str hardwares_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patchhardwares_item_with_http_info(body, if_match, hardwares_id, **kwargs)  # noqa: E501
        else:
            (data) = self.patchhardwares_item_with_http_info(body, if_match, hardwares_id, **kwargs)  # noqa: E501
            return data

    def patchhardwares_item_with_http_info(self, body, if_match, hardwares_id, **kwargs):  # noqa: E501
        """Updates a hardwares document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchhardwares_item_with_http_info(body, if_match, hardwares_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Hardwares body: A hardwares or list of hardwares documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str hardwares_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'hardwares_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patchhardwares_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patchhardwares_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `patchhardwares_item`")  # noqa: E501
        # verify the required parameter 'hardwares_id' is set
        if ('hardwares_id' not in params or
                params['hardwares_id'] is None):
            raise ValueError("Missing the required parameter `hardwares_id` when calling `patchhardwares_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardwares_id' in params:
            path_params['hardwaresId'] = params['hardwares_id']  # noqa: E501

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
            '/hardwares/{hardwaresId}', 'PATCH',
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

    def posthardwares(self, body, **kwargs):  # noqa: E501
        """Stores one or more hardwares.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.posthardwares(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Hardwares body: A hardwares or list of hardwares documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.posthardwares_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.posthardwares_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def posthardwares_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more hardwares.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.posthardwares_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Hardwares body: A hardwares or list of hardwares documents (required)
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
                    " to method posthardwares" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `posthardwares`")  # noqa: E501

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
            '/hardwares', 'POST',
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

    def puthardwares_item(self, body, if_match, hardwares_id, **kwargs):  # noqa: E501
        """Replaces a hardwares document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.puthardwares_item(body, if_match, hardwares_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Hardwares body: A hardwares or list of hardwares documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str hardwares_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.puthardwares_item_with_http_info(body, if_match, hardwares_id, **kwargs)  # noqa: E501
        else:
            (data) = self.puthardwares_item_with_http_info(body, if_match, hardwares_id, **kwargs)  # noqa: E501
            return data

    def puthardwares_item_with_http_info(self, body, if_match, hardwares_id, **kwargs):  # noqa: E501
        """Replaces a hardwares document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.puthardwares_item_with_http_info(body, if_match, hardwares_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Hardwares body: A hardwares or list of hardwares documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str hardwares_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'hardwares_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method puthardwares_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `puthardwares_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `puthardwares_item`")  # noqa: E501
        # verify the required parameter 'hardwares_id' is set
        if ('hardwares_id' not in params or
                params['hardwares_id'] is None):
            raise ValueError("Missing the required parameter `hardwares_id` when calling `puthardwares_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hardwares_id' in params:
            path_params['hardwaresId'] = params['hardwares_id']  # noqa: E501

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
            '/hardwares/{hardwaresId}', 'PUT',
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
