# swagger_client.MeasurablesApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletemeasurables_item**](MeasurablesApi.md#deletemeasurables_item) | **DELETE** /measurables/{measurablesId} | Deletes a measurables document
[**getmeasurables**](MeasurablesApi.md#getmeasurables) | **GET** /measurables | Retrieves one or more measurables
[**getmeasurables_item**](MeasurablesApi.md#getmeasurables_item) | **GET** /measurables/{measurablesId} | Retrieves a measurables document
[**patchmeasurables_item**](MeasurablesApi.md#patchmeasurables_item) | **PATCH** /measurables/{measurablesId} | Updates a measurables document
[**postmeasurables**](MeasurablesApi.md#postmeasurables) | **POST** /measurables | Stores one or more measurables.
[**putmeasurables_item**](MeasurablesApi.md#putmeasurables_item) | **PUT** /measurables/{measurablesId} | Replaces a measurables document

# **deletemeasurables_item**
> deletemeasurables_item(measurables_id, if_match)

Deletes a measurables document

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
api_instance = swagger_client.MeasurablesApi(swagger_client.ApiClient(configuration))
measurables_id = 'measurables_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a measurables document
    api_instance.deletemeasurables_item(measurables_id, if_match)
except ApiException as e:
    print("Exception when calling MeasurablesApi->deletemeasurables_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measurables_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getmeasurables**
> InlineResponse2004 getmeasurables(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more measurables

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
api_instance = swagger_client.MeasurablesApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more measurables
    api_response = api_instance.getmeasurables(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeasurablesApi->getmeasurables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getmeasurables_item**
> Measurables getmeasurables_item(measurables_id)

Retrieves a measurables document

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
api_instance = swagger_client.MeasurablesApi(swagger_client.ApiClient(configuration))
measurables_id = 'measurables_id_example' # str | 

try:
    # Retrieves a measurables document
    api_response = api_instance.getmeasurables_item(measurables_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeasurablesApi->getmeasurables_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measurables_id** | **str**|  | 

### Return type

[**Measurables**](Measurables.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchmeasurables_item**
> patchmeasurables_item(body, if_match, measurables_id)

Updates a measurables document

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
api_instance = swagger_client.MeasurablesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Measurables() # Measurables | A measurables or list of measurables documents
if_match = 'if_match_example' # str | Current value of the _etag field
measurables_id = 'measurables_id_example' # str | 

try:
    # Updates a measurables document
    api_instance.patchmeasurables_item(body, if_match, measurables_id)
except ApiException as e:
    print("Exception when calling MeasurablesApi->patchmeasurables_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Measurables**](Measurables.md)| A measurables or list of measurables documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **measurables_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postmeasurables**
> postmeasurables(body)

Stores one or more measurables.

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
api_instance = swagger_client.MeasurablesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Measurables() # Measurables | A measurables or list of measurables documents

try:
    # Stores one or more measurables.
    api_instance.postmeasurables(body)
except ApiException as e:
    print("Exception when calling MeasurablesApi->postmeasurables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Measurables**](Measurables.md)| A measurables or list of measurables documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putmeasurables_item**
> putmeasurables_item(body, if_match, measurables_id)

Replaces a measurables document

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
api_instance = swagger_client.MeasurablesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Measurables() # Measurables | A measurables or list of measurables documents
if_match = 'if_match_example' # str | Current value of the _etag field
measurables_id = 'measurables_id_example' # str | 

try:
    # Replaces a measurables document
    api_instance.putmeasurables_item(body, if_match, measurables_id)
except ApiException as e:
    print("Exception when calling MeasurablesApi->putmeasurables_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Measurables**](Measurables.md)| A measurables or list of measurables documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **measurables_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

