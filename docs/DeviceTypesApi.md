# swagger_client.DeviceTypesApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletedevice_types_item**](DeviceTypesApi.md#deletedevice_types_item) | **DELETE** /device_types/{device-typesId} | Deletes a device-types document
[**getdevice_types**](DeviceTypesApi.md#getdevice_types) | **GET** /device_types | Retrieves one or more device_types
[**getdevice_types_item**](DeviceTypesApi.md#getdevice_types_item) | **GET** /device_types/{device-typesId} | Retrieves a device-types document
[**patchdevice_types_item**](DeviceTypesApi.md#patchdevice_types_item) | **PATCH** /device_types/{device-typesId} | Updates a device-types document
[**postdevice_types**](DeviceTypesApi.md#postdevice_types) | **POST** /device_types | Stores one or more device_types.
[**putdevice_types_item**](DeviceTypesApi.md#putdevice_types_item) | **PUT** /device_types/{device-typesId} | Replaces a device-types document

# **deletedevice_types_item**
> deletedevice_types_item(device_types_id, if_match)

Deletes a device-types document

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
api_instance = swagger_client.DeviceTypesApi(swagger_client.ApiClient(configuration))
device_types_id = 'device_types_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a device-types document
    api_instance.deletedevice_types_item(device_types_id, if_match)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->deletedevice_types_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_types_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdevice_types**
> InlineResponse200 getdevice_types(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more device_types

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
api_instance = swagger_client.DeviceTypesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more device_types
    api_response = api_instance.getdevice_types(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->getdevice_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdevice_types_item**
> DeviceTypes getdevice_types_item(device_types_id)

Retrieves a device-types document

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
api_instance = swagger_client.DeviceTypesApi(swagger_client.ApiClient(configuration))
device_types_id = 'device_types_id_example' # str | 

try:
    # Retrieves a device-types document
    api_response = api_instance.getdevice_types_item(device_types_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->getdevice_types_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_types_id** | **str**|  | 

### Return type

[**DeviceTypes**](DeviceTypes.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchdevice_types_item**
> patchdevice_types_item(body, if_match, device_types_id)

Updates a device-types document

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
api_instance = swagger_client.DeviceTypesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents
if_match = 'if_match_example' # str | Current value of the _etag field
device_types_id = 'device_types_id_example' # str | 

try:
    # Updates a device-types document
    api_instance.patchdevice_types_item(body, if_match, device_types_id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->patchdevice_types_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceTypes**](DeviceTypes.md)| A device-types or list of device-types documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **device_types_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postdevice_types**
> postdevice_types(body)

Stores one or more device_types.

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
api_instance = swagger_client.DeviceTypesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents

try:
    # Stores one or more device_types.
    api_instance.postdevice_types(body)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->postdevice_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceTypes**](DeviceTypes.md)| A device-types or list of device-types documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putdevice_types_item**
> putdevice_types_item(body, if_match, device_types_id)

Replaces a device-types document

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
api_instance = swagger_client.DeviceTypesApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeviceTypes() # DeviceTypes | A device-types or list of device-types documents
if_match = 'if_match_example' # str | Current value of the _etag field
device_types_id = 'device_types_id_example' # str | 

try:
    # Replaces a device-types document
    api_instance.putdevice_types_item(body, if_match, device_types_id)
except ApiException as e:
    print("Exception when calling DeviceTypesApi->putdevice_types_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceTypes**](DeviceTypes.md)| A device-types or list of device-types documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **device_types_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

