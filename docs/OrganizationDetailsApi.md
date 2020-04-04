# swagger_client.OrganizationDetailsApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteorganization_details_item**](OrganizationDetailsApi.md#deleteorganization_details_item) | **DELETE** /org_details/{organization-detailsId} | Deletes a organization-details document
[**getorg_details**](OrganizationDetailsApi.md#getorg_details) | **GET** /org_details | Retrieves one or more org_details
[**getorganization_details_item**](OrganizationDetailsApi.md#getorganization_details_item) | **GET** /org_details/{organization-detailsId} | Retrieves a organization-details document
[**patchorganization_details_item**](OrganizationDetailsApi.md#patchorganization_details_item) | **PATCH** /org_details/{organization-detailsId} | Updates a organization-details document
[**postorg_details**](OrganizationDetailsApi.md#postorg_details) | **POST** /org_details | Stores one or more org_details.
[**putorganization_details_item**](OrganizationDetailsApi.md#putorganization_details_item) | **PUT** /org_details/{organization-detailsId} | Replaces a organization-details document

# **deleteorganization_details_item**
> deleteorganization_details_item(organization_details_id, if_match)

Deletes a organization-details document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationDetailsApi(swagger_client.ApiClient(configuration))
organization_details_id = 'organization_details_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a organization-details document
    api_instance.deleteorganization_details_item(organization_details_id, if_match)
except ApiException as e:
    print("Exception when calling OrganizationDetailsApi->deleteorganization_details_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_details_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getorg_details**
> InlineResponse2006 getorg_details(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more org_details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationDetailsApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more org_details
    api_response = api_instance.getorg_details(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationDetailsApi->getorg_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getorganization_details_item**
> OrganizationDetails getorganization_details_item(organization_details_id)

Retrieves a organization-details document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationDetailsApi(swagger_client.ApiClient(configuration))
organization_details_id = 'organization_details_id_example' # str | 

try:
    # Retrieves a organization-details document
    api_response = api_instance.getorganization_details_item(organization_details_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationDetailsApi->getorganization_details_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_details_id** | **str**|  | 

### Return type

[**OrganizationDetails**](OrganizationDetails.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchorganization_details_item**
> patchorganization_details_item(body, if_match, organization_details_id)

Updates a organization-details document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationDetailsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganizationDetails() # OrganizationDetails | A organization-details or list of organization-details documents
if_match = 'if_match_example' # str | Current value of the _etag field
organization_details_id = 'organization_details_id_example' # str | 

try:
    # Updates a organization-details document
    api_instance.patchorganization_details_item(body, if_match, organization_details_id)
except ApiException as e:
    print("Exception when calling OrganizationDetailsApi->patchorganization_details_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationDetails**](OrganizationDetails.md)| A organization-details or list of organization-details documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **organization_details_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postorg_details**
> postorg_details(body)

Stores one or more org_details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationDetailsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganizationDetails() # OrganizationDetails | A organization-details or list of organization-details documents

try:
    # Stores one or more org_details.
    api_instance.postorg_details(body)
except ApiException as e:
    print("Exception when calling OrganizationDetailsApi->postorg_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationDetails**](OrganizationDetails.md)| A organization-details or list of organization-details documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putorganization_details_item**
> putorganization_details_item(body, if_match, organization_details_id)

Replaces a organization-details document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.OrganizationDetailsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganizationDetails() # OrganizationDetails | A organization-details or list of organization-details documents
if_match = 'if_match_example' # str | Current value of the _etag field
organization_details_id = 'organization_details_id_example' # str | 

try:
    # Replaces a organization-details document
    api_instance.putorganization_details_item(body, if_match, organization_details_id)
except ApiException as e:
    print("Exception when calling OrganizationDetailsApi->putorganization_details_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationDetails**](OrganizationDetails.md)| A organization-details or list of organization-details documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **organization_details_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

