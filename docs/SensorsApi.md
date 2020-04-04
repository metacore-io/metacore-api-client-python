# swagger_client.SensorsApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletesensors_item**](SensorsApi.md#deletesensors_item) | **DELETE** /sensors/{sensorsId} | Deletes a sensors document
[**getsensors**](SensorsApi.md#getsensors) | **GET** /sensors | Retrieves one or more sensors
[**getsensors_item**](SensorsApi.md#getsensors_item) | **GET** /sensors/{sensorsId} | Retrieves a sensors document
[**patchsensors_item**](SensorsApi.md#patchsensors_item) | **PATCH** /sensors/{sensorsId} | Updates a sensors document
[**postsensors**](SensorsApi.md#postsensors) | **POST** /sensors | Stores one or more sensors.
[**putsensors_item**](SensorsApi.md#putsensors_item) | **PUT** /sensors/{sensorsId} | Replaces a sensors document

# **deletesensors_item**
> deletesensors_item(sensors_id, if_match)

Deletes a sensors document

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
sensors_id = 'sensors_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a sensors document
    api_instance.deletesensors_item(sensors_id, if_match)
except ApiException as e:
    print("Exception when calling SensorsApi->deletesensors_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensors_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getsensors**
> InlineResponse20011 getsensors(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more sensors

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more sensors
    api_response = api_instance.getsensors(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->getsensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getsensors_item**
> Sensors getsensors_item(sensors_id)

Retrieves a sensors document

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
sensors_id = 'sensors_id_example' # str | 

try:
    # Retrieves a sensors document
    api_response = api_instance.getsensors_item(sensors_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->getsensors_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensors_id** | **str**|  | 

### Return type

[**Sensors**](Sensors.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchsensors_item**
> patchsensors_item(body, if_match, sensors_id)

Updates a sensors document

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Sensors() # Sensors | A sensors or list of sensors documents
if_match = 'if_match_example' # str | Current value of the _etag field
sensors_id = 'sensors_id_example' # str | 

try:
    # Updates a sensors document
    api_instance.patchsensors_item(body, if_match, sensors_id)
except ApiException as e:
    print("Exception when calling SensorsApi->patchsensors_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sensors**](Sensors.md)| A sensors or list of sensors documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **sensors_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postsensors**
> postsensors(body)

Stores one or more sensors.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Sensors() # Sensors | A sensors or list of sensors documents

try:
    # Stores one or more sensors.
    api_instance.postsensors(body)
except ApiException as e:
    print("Exception when calling SensorsApi->postsensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sensors**](Sensors.md)| A sensors or list of sensors documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putsensors_item**
> putsensors_item(body, if_match, sensors_id)

Replaces a sensors document

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Sensors() # Sensors | A sensors or list of sensors documents
if_match = 'if_match_example' # str | Current value of the _etag field
sensors_id = 'sensors_id_example' # str | 

try:
    # Replaces a sensors document
    api_instance.putsensors_item(body, if_match, sensors_id)
except ApiException as e:
    print("Exception when calling SensorsApi->putsensors_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sensors**](Sensors.md)| A sensors or list of sensors documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **sensors_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

