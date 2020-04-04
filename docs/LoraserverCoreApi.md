# swagger_client.LoraserverCoreApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteloraserver_core_item**](LoraserverCoreApi.md#deleteloraserver_core_item) | **DELETE** /loraserver_core/{loraserver-coreId} | Deletes a loraserver-core document
[**getloraserver_core**](LoraserverCoreApi.md#getloraserver_core) | **GET** /loraserver_core | Retrieves one or more loraserver_core
[**getloraserver_core_item**](LoraserverCoreApi.md#getloraserver_core_item) | **GET** /loraserver_core/{loraserver-coreId} | Retrieves a loraserver-core document
[**patchloraserver_core_item**](LoraserverCoreApi.md#patchloraserver_core_item) | **PATCH** /loraserver_core/{loraserver-coreId} | Updates a loraserver-core document
[**postloraserver_core**](LoraserverCoreApi.md#postloraserver_core) | **POST** /loraserver_core | Stores one or more loraserver_core.
[**putloraserver_core_item**](LoraserverCoreApi.md#putloraserver_core_item) | **PUT** /loraserver_core/{loraserver-coreId} | Replaces a loraserver-core document

# **deleteloraserver_core_item**
> deleteloraserver_core_item(loraserver_core_id, if_match)

Deletes a loraserver-core document

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
api_instance = swagger_client.LoraserverCoreApi(swagger_client.ApiClient(configuration))
loraserver_core_id = 'loraserver_core_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a loraserver-core document
    api_instance.deleteloraserver_core_item(loraserver_core_id, if_match)
except ApiException as e:
    print("Exception when calling LoraserverCoreApi->deleteloraserver_core_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loraserver_core_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getloraserver_core**
> InlineResponse2003 getloraserver_core(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more loraserver_core

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
api_instance = swagger_client.LoraserverCoreApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more loraserver_core
    api_response = api_instance.getloraserver_core(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoraserverCoreApi->getloraserver_core: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getloraserver_core_item**
> LoraserverCore getloraserver_core_item(loraserver_core_id)

Retrieves a loraserver-core document

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
api_instance = swagger_client.LoraserverCoreApi(swagger_client.ApiClient(configuration))
loraserver_core_id = 'loraserver_core_id_example' # str | 

try:
    # Retrieves a loraserver-core document
    api_response = api_instance.getloraserver_core_item(loraserver_core_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoraserverCoreApi->getloraserver_core_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loraserver_core_id** | **str**|  | 

### Return type

[**LoraserverCore**](LoraserverCore.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchloraserver_core_item**
> patchloraserver_core_item(body, if_match, loraserver_core_id)

Updates a loraserver-core document

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
api_instance = swagger_client.LoraserverCoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoraserverCore() # LoraserverCore | A loraserver-core or list of loraserver-core documents
if_match = 'if_match_example' # str | Current value of the _etag field
loraserver_core_id = 'loraserver_core_id_example' # str | 

try:
    # Updates a loraserver-core document
    api_instance.patchloraserver_core_item(body, if_match, loraserver_core_id)
except ApiException as e:
    print("Exception when calling LoraserverCoreApi->patchloraserver_core_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoraserverCore**](LoraserverCore.md)| A loraserver-core or list of loraserver-core documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **loraserver_core_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postloraserver_core**
> postloraserver_core(body)

Stores one or more loraserver_core.

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
api_instance = swagger_client.LoraserverCoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoraserverCore() # LoraserverCore | A loraserver-core or list of loraserver-core documents

try:
    # Stores one or more loraserver_core.
    api_instance.postloraserver_core(body)
except ApiException as e:
    print("Exception when calling LoraserverCoreApi->postloraserver_core: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoraserverCore**](LoraserverCore.md)| A loraserver-core or list of loraserver-core documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putloraserver_core_item**
> putloraserver_core_item(body, if_match, loraserver_core_id)

Replaces a loraserver-core document

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
api_instance = swagger_client.LoraserverCoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoraserverCore() # LoraserverCore | A loraserver-core or list of loraserver-core documents
if_match = 'if_match_example' # str | Current value of the _etag field
loraserver_core_id = 'loraserver_core_id_example' # str | 

try:
    # Replaces a loraserver-core document
    api_instance.putloraserver_core_item(body, if_match, loraserver_core_id)
except ApiException as e:
    print("Exception when calling LoraserverCoreApi->putloraserver_core_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoraserverCore**](LoraserverCore.md)| A loraserver-core or list of loraserver-core documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **loraserver_core_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

