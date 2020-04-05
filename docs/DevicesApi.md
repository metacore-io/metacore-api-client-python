# metacore_api_python_cli.DevicesApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletedevices_item**](DevicesApi.md#deletedevices_item) | **DELETE** /devices/{devicesId} | Deletes a devices document
[**getdevices**](DevicesApi.md#getdevices) | **GET** /devices | Retrieves one or more devices
[**getdevices_item**](DevicesApi.md#getdevices_item) | **GET** /devices/{devicesId} | Retrieves a devices document
[**patchdevices_item**](DevicesApi.md#patchdevices_item) | **PATCH** /devices/{devicesId} | Updates a devices document
[**postdevices**](DevicesApi.md#postdevices) | **POST** /devices | Stores one or more devices.
[**putdevices_item**](DevicesApi.md#putdevices_item) | **PUT** /devices/{devicesId} | Replaces a devices document

# **deletedevices_item**
> deletedevices_item(devices_id, if_match)

Deletes a devices document

### Example
```python
from __future__ import print_function
import time
import metacore_api_python_cli
from metacore_api_python_cli.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = metacore_api_python_cli.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = metacore_api_python_cli.DevicesApi(metacore_api_python_cli.ApiClient(configuration))
devices_id = 'devices_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a devices document
    api_instance.deletedevices_item(devices_id, if_match)
except ApiException as e:
    print("Exception when calling DevicesApi->deletedevices_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdevices**
> InlineResponse2001 getdevices(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more devices

### Example
```python
from __future__ import print_function
import time
import metacore_api_python_cli
from metacore_api_python_cli.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = metacore_api_python_cli.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = metacore_api_python_cli.DevicesApi(metacore_api_python_cli.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more devices
    api_response = api_instance.getdevices(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->getdevices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdevices_item**
> Devices getdevices_item(devices_id)

Retrieves a devices document

### Example
```python
from __future__ import print_function
import time
import metacore_api_python_cli
from metacore_api_python_cli.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = metacore_api_python_cli.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = metacore_api_python_cli.DevicesApi(metacore_api_python_cli.ApiClient(configuration))
devices_id = 'devices_id_example' # str | 

try:
    # Retrieves a devices document
    api_response = api_instance.getdevices_item(devices_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->getdevices_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices_id** | **str**|  | 

### Return type

[**Devices**](Devices.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchdevices_item**
> patchdevices_item(body, if_match, devices_id)

Updates a devices document

### Example
```python
from __future__ import print_function
import time
import metacore_api_python_cli
from metacore_api_python_cli.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = metacore_api_python_cli.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = metacore_api_python_cli.DevicesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Devices() # Devices | A devices or list of devices documents
if_match = 'if_match_example' # str | Current value of the _etag field
devices_id = 'devices_id_example' # str | 

try:
    # Updates a devices document
    api_instance.patchdevices_item(body, if_match, devices_id)
except ApiException as e:
    print("Exception when calling DevicesApi->patchdevices_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Devices**](Devices.md)| A devices or list of devices documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **devices_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postdevices**
> postdevices(body)

Stores one or more devices.

### Example
```python
from __future__ import print_function
import time
import metacore_api_python_cli
from metacore_api_python_cli.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = metacore_api_python_cli.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = metacore_api_python_cli.DevicesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Devices() # Devices | A devices or list of devices documents

try:
    # Stores one or more devices.
    api_instance.postdevices(body)
except ApiException as e:
    print("Exception when calling DevicesApi->postdevices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Devices**](Devices.md)| A devices or list of devices documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putdevices_item**
> putdevices_item(body, if_match, devices_id)

Replaces a devices document

### Example
```python
from __future__ import print_function
import time
import metacore_api_python_cli
from metacore_api_python_cli.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = metacore_api_python_cli.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = metacore_api_python_cli.DevicesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Devices() # Devices | A devices or list of devices documents
if_match = 'if_match_example' # str | Current value of the _etag field
devices_id = 'devices_id_example' # str | 

try:
    # Replaces a devices document
    api_instance.putdevices_item(body, if_match, devices_id)
except ApiException as e:
    print("Exception when calling DevicesApi->putdevices_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Devices**](Devices.md)| A devices or list of devices documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **devices_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

