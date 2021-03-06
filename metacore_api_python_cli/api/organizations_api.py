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


class OrganizationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deleteorganizations_item(self, organizations_id, if_match, **kwargs):  # noqa: E501
        """Deletes a organizations document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deleteorganizations_item(organizations_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organizations_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deleteorganizations_item_with_http_info(organizations_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.deleteorganizations_item_with_http_info(organizations_id, if_match, **kwargs)  # noqa: E501
            return data

    def deleteorganizations_item_with_http_info(self, organizations_id, if_match, **kwargs):  # noqa: E501
        """Deletes a organizations document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deleteorganizations_item_with_http_info(organizations_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organizations_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deleteorganizations_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organizations_id' is set
        if ('organizations_id' not in params or
                params['organizations_id'] is None):
            raise ValueError("Missing the required parameter `organizations_id` when calling `deleteorganizations_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `deleteorganizations_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organizations_id' in params:
            path_params['organizationsId'] = params['organizations_id']  # noqa: E501

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
            '/orgs/{organizationsId}', 'DELETE',
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

    def getorganizations_item(self, organizations_id, **kwargs):  # noqa: E501
        """Retrieves a organizations document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getorganizations_item(organizations_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organizations_id: (required)
        :return: Organizations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getorganizations_item_with_http_info(organizations_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getorganizations_item_with_http_info(organizations_id, **kwargs)  # noqa: E501
            return data

    def getorganizations_item_with_http_info(self, organizations_id, **kwargs):  # noqa: E501
        """Retrieves a organizations document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getorganizations_item_with_http_info(organizations_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organizations_id: (required)
        :return: Organizations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organizations_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getorganizations_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organizations_id' is set
        if ('organizations_id' not in params or
                params['organizations_id'] is None):
            raise ValueError("Missing the required parameter `organizations_id` when calling `getorganizations_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organizations_id' in params:
            path_params['organizationsId'] = params['organizations_id']  # noqa: E501

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
            '/orgs/{organizationsId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organizations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getorgs(self, **kwargs):  # noqa: E501
        """Retrieves one or more orgs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getorgs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getorgs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.getorgs_with_http_info(**kwargs)  # noqa: E501
            return data

    def getorgs_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more orgs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getorgs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2007
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
                    " to method getorgs" % key
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
            '/orgs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patchorganizations_item(self, body, if_match, organizations_id, **kwargs):  # noqa: E501
        """Updates a organizations document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchorganizations_item(body, if_match, organizations_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Organizations body: A organizations or list of organizations documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str organizations_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patchorganizations_item_with_http_info(body, if_match, organizations_id, **kwargs)  # noqa: E501
        else:
            (data) = self.patchorganizations_item_with_http_info(body, if_match, organizations_id, **kwargs)  # noqa: E501
            return data

    def patchorganizations_item_with_http_info(self, body, if_match, organizations_id, **kwargs):  # noqa: E501
        """Updates a organizations document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patchorganizations_item_with_http_info(body, if_match, organizations_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Organizations body: A organizations or list of organizations documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str organizations_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'organizations_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patchorganizations_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patchorganizations_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `patchorganizations_item`")  # noqa: E501
        # verify the required parameter 'organizations_id' is set
        if ('organizations_id' not in params or
                params['organizations_id'] is None):
            raise ValueError("Missing the required parameter `organizations_id` when calling `patchorganizations_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organizations_id' in params:
            path_params['organizationsId'] = params['organizations_id']  # noqa: E501

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
            '/orgs/{organizationsId}', 'PATCH',
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

    def postorgs(self, body, **kwargs):  # noqa: E501
        """Stores one or more orgs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postorgs(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Organizations body: A organizations or list of organizations documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postorgs_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.postorgs_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def postorgs_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more orgs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postorgs_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Organizations body: A organizations or list of organizations documents (required)
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
                    " to method postorgs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postorgs`")  # noqa: E501

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
            '/orgs', 'POST',
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

    def putorganizations_item(self, body, if_match, organizations_id, **kwargs):  # noqa: E501
        """Replaces a organizations document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putorganizations_item(body, if_match, organizations_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Organizations body: A organizations or list of organizations documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str organizations_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.putorganizations_item_with_http_info(body, if_match, organizations_id, **kwargs)  # noqa: E501
        else:
            (data) = self.putorganizations_item_with_http_info(body, if_match, organizations_id, **kwargs)  # noqa: E501
            return data

    def putorganizations_item_with_http_info(self, body, if_match, organizations_id, **kwargs):  # noqa: E501
        """Replaces a organizations document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putorganizations_item_with_http_info(body, if_match, organizations_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Organizations body: A organizations or list of organizations documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str organizations_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'organizations_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putorganizations_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `putorganizations_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `putorganizations_item`")  # noqa: E501
        # verify the required parameter 'organizations_id' is set
        if ('organizations_id' not in params or
                params['organizations_id'] is None):
            raise ValueError("Missing the required parameter `organizations_id` when calling `putorganizations_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'organizations_id' in params:
            path_params['organizationsId'] = params['organizations_id']  # noqa: E501

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
            '/orgs/{organizationsId}', 'PUT',
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
