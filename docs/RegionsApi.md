# swagger_client.RegionsApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteregions_item**](RegionsApi.md#deleteregions_item) | **DELETE** /regions/{regionsId} | Deletes a regions document
[**getregions**](RegionsApi.md#getregions) | **GET** /regions | Retrieves one or more regions
[**getregions_item**](RegionsApi.md#getregions_item) | **GET** /regions/{regionsId} | Retrieves a regions document
[**patchregions_item**](RegionsApi.md#patchregions_item) | **PATCH** /regions/{regionsId} | Updates a regions document
[**postregions**](RegionsApi.md#postregions) | **POST** /regions | Stores one or more regions.
[**putregions_item**](RegionsApi.md#putregions_item) | **PUT** /regions/{regionsId} | Replaces a regions document

# **deleteregions_item**
> deleteregions_item(regions_id, if_match)

Deletes a regions document

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
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
regions_id = 'regions_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a regions document
    api_instance.deleteregions_item(regions_id, if_match)
except ApiException as e:
    print("Exception when calling RegionsApi->deleteregions_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getregions**
> InlineResponse2009 getregions(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more regions

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
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more regions
    api_response = api_instance.getregions(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->getregions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getregions_item**
> Regions getregions_item(regions_id)

Retrieves a regions document

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
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
regions_id = 'regions_id_example' # str | 

try:
    # Retrieves a regions document
    api_response = api_instance.getregions_item(regions_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->getregions_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions_id** | **str**|  | 

### Return type

[**Regions**](Regions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchregions_item**
> patchregions_item(body, if_match, regions_id)

Updates a regions document

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
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Regions() # Regions | A regions or list of regions documents
if_match = 'if_match_example' # str | Current value of the _etag field
regions_id = 'regions_id_example' # str | 

try:
    # Updates a regions document
    api_instance.patchregions_item(body, if_match, regions_id)
except ApiException as e:
    print("Exception when calling RegionsApi->patchregions_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Regions**](Regions.md)| A regions or list of regions documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **regions_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postregions**
> postregions(body)

Stores one or more regions.

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
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Regions() # Regions | A regions or list of regions documents

try:
    # Stores one or more regions.
    api_instance.postregions(body)
except ApiException as e:
    print("Exception when calling RegionsApi->postregions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Regions**](Regions.md)| A regions or list of regions documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putregions_item**
> putregions_item(body, if_match, regions_id)

Replaces a regions document

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
api_instance = swagger_client.RegionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Regions() # Regions | A regions or list of regions documents
if_match = 'if_match_example' # str | Current value of the _etag field
regions_id = 'regions_id_example' # str | 

try:
    # Replaces a regions document
    api_instance.putregions_item(body, if_match, regions_id)
except ApiException as e:
    print("Exception when calling RegionsApi->putregions_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Regions**](Regions.md)| A regions or list of regions documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **regions_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

