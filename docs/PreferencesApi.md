# metacore_api_python_cli.PreferencesApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletepreferences_item**](PreferencesApi.md#deletepreferences_item) | **DELETE** /preferences/{preferencesId} | Deletes a preferences document
[**getpreferences**](PreferencesApi.md#getpreferences) | **GET** /preferences | Retrieves one or more preferences
[**getpreferences_item**](PreferencesApi.md#getpreferences_item) | **GET** /preferences/{preferencesId} | Retrieves a preferences document
[**patchpreferences_item**](PreferencesApi.md#patchpreferences_item) | **PATCH** /preferences/{preferencesId} | Updates a preferences document
[**postpreferences**](PreferencesApi.md#postpreferences) | **POST** /preferences | Stores one or more preferences.
[**putpreferences_item**](PreferencesApi.md#putpreferences_item) | **PUT** /preferences/{preferencesId} | Replaces a preferences document

# **deletepreferences_item**
> deletepreferences_item(preferences_id, if_match)

Deletes a preferences document

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
api_instance = metacore_api_python_cli.PreferencesApi(metacore_api_python_cli.ApiClient(configuration))
preferences_id = 'preferences_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a preferences document
    api_instance.deletepreferences_item(preferences_id, if_match)
except ApiException as e:
    print("Exception when calling PreferencesApi->deletepreferences_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preferences_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpreferences**
> InlineResponse2008 getpreferences(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more preferences

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
api_instance = metacore_api_python_cli.PreferencesApi(metacore_api_python_cli.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more preferences
    api_response = api_instance.getpreferences(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreferencesApi->getpreferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpreferences_item**
> Preferences getpreferences_item(preferences_id)

Retrieves a preferences document

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
api_instance = metacore_api_python_cli.PreferencesApi(metacore_api_python_cli.ApiClient(configuration))
preferences_id = 'preferences_id_example' # str | 

try:
    # Retrieves a preferences document
    api_response = api_instance.getpreferences_item(preferences_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreferencesApi->getpreferences_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preferences_id** | **str**|  | 

### Return type

[**Preferences**](Preferences.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchpreferences_item**
> patchpreferences_item(body, if_match, preferences_id)

Updates a preferences document

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
api_instance = metacore_api_python_cli.PreferencesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Preferences() # Preferences | A preferences or list of preferences documents
if_match = 'if_match_example' # str | Current value of the _etag field
preferences_id = 'preferences_id_example' # str | 

try:
    # Updates a preferences document
    api_instance.patchpreferences_item(body, if_match, preferences_id)
except ApiException as e:
    print("Exception when calling PreferencesApi->patchpreferences_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Preferences**](Preferences.md)| A preferences or list of preferences documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **preferences_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postpreferences**
> postpreferences(body)

Stores one or more preferences.

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
api_instance = metacore_api_python_cli.PreferencesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Preferences() # Preferences | A preferences or list of preferences documents

try:
    # Stores one or more preferences.
    api_instance.postpreferences(body)
except ApiException as e:
    print("Exception when calling PreferencesApi->postpreferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Preferences**](Preferences.md)| A preferences or list of preferences documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putpreferences_item**
> putpreferences_item(body, if_match, preferences_id)

Replaces a preferences document

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
api_instance = metacore_api_python_cli.PreferencesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Preferences() # Preferences | A preferences or list of preferences documents
if_match = 'if_match_example' # str | Current value of the _etag field
preferences_id = 'preferences_id_example' # str | 

try:
    # Replaces a preferences document
    api_instance.putpreferences_item(body, if_match, preferences_id)
except ApiException as e:
    print("Exception when calling PreferencesApi->putpreferences_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Preferences**](Preferences.md)| A preferences or list of preferences documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **preferences_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

