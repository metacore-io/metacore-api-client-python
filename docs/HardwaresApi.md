# swagger_client.HardwaresApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletehardwares_item**](HardwaresApi.md#deletehardwares_item) | **DELETE** /hardwares/{hardwaresId} | Deletes a hardwares document
[**gethardwares**](HardwaresApi.md#gethardwares) | **GET** /hardwares | Retrieves one or more hardwares
[**gethardwares_item**](HardwaresApi.md#gethardwares_item) | **GET** /hardwares/{hardwaresId} | Retrieves a hardwares document
[**patchhardwares_item**](HardwaresApi.md#patchhardwares_item) | **PATCH** /hardwares/{hardwaresId} | Updates a hardwares document
[**posthardwares**](HardwaresApi.md#posthardwares) | **POST** /hardwares | Stores one or more hardwares.
[**puthardwares_item**](HardwaresApi.md#puthardwares_item) | **PUT** /hardwares/{hardwaresId} | Replaces a hardwares document

# **deletehardwares_item**
> deletehardwares_item(hardwares_id, if_match)

Deletes a hardwares document

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
api_instance = swagger_client.HardwaresApi(swagger_client.ApiClient(configuration))
hardwares_id = 'hardwares_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a hardwares document
    api_instance.deletehardwares_item(hardwares_id, if_match)
except ApiException as e:
    print("Exception when calling HardwaresApi->deletehardwares_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardwares_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gethardwares**
> InlineResponse2002 gethardwares(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more hardwares

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
api_instance = swagger_client.HardwaresApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more hardwares
    api_response = api_instance.gethardwares(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwaresApi->gethardwares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gethardwares_item**
> Hardwares gethardwares_item(hardwares_id)

Retrieves a hardwares document

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
api_instance = swagger_client.HardwaresApi(swagger_client.ApiClient(configuration))
hardwares_id = 'hardwares_id_example' # str | 

try:
    # Retrieves a hardwares document
    api_response = api_instance.gethardwares_item(hardwares_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwaresApi->gethardwares_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardwares_id** | **str**|  | 

### Return type

[**Hardwares**](Hardwares.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchhardwares_item**
> patchhardwares_item(body, if_match, hardwares_id)

Updates a hardwares document

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
api_instance = swagger_client.HardwaresApi(swagger_client.ApiClient(configuration))
body = swagger_client.Hardwares() # Hardwares | A hardwares or list of hardwares documents
if_match = 'if_match_example' # str | Current value of the _etag field
hardwares_id = 'hardwares_id_example' # str | 

try:
    # Updates a hardwares document
    api_instance.patchhardwares_item(body, if_match, hardwares_id)
except ApiException as e:
    print("Exception when calling HardwaresApi->patchhardwares_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Hardwares**](Hardwares.md)| A hardwares or list of hardwares documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **hardwares_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **posthardwares**
> posthardwares(body)

Stores one or more hardwares.

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
api_instance = swagger_client.HardwaresApi(swagger_client.ApiClient(configuration))
body = swagger_client.Hardwares() # Hardwares | A hardwares or list of hardwares documents

try:
    # Stores one or more hardwares.
    api_instance.posthardwares(body)
except ApiException as e:
    print("Exception when calling HardwaresApi->posthardwares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Hardwares**](Hardwares.md)| A hardwares or list of hardwares documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **puthardwares_item**
> puthardwares_item(body, if_match, hardwares_id)

Replaces a hardwares document

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
api_instance = swagger_client.HardwaresApi(swagger_client.ApiClient(configuration))
body = swagger_client.Hardwares() # Hardwares | A hardwares or list of hardwares documents
if_match = 'if_match_example' # str | Current value of the _etag field
hardwares_id = 'hardwares_id_example' # str | 

try:
    # Replaces a hardwares document
    api_instance.puthardwares_item(body, if_match, hardwares_id)
except ApiException as e:
    print("Exception when calling HardwaresApi->puthardwares_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Hardwares**](Hardwares.md)| A hardwares or list of hardwares documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **hardwares_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

