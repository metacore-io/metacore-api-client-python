# swagger_client.TenantsApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletetenants_item**](TenantsApi.md#deletetenants_item) | **DELETE** /tenants/{tenantsId} | Deletes a tenants document
[**gettenants**](TenantsApi.md#gettenants) | **GET** /tenants | Retrieves one or more tenants
[**gettenants_item**](TenantsApi.md#gettenants_item) | **GET** /tenants/{tenantsId} | Retrieves a tenants document
[**patchtenants_item**](TenantsApi.md#patchtenants_item) | **PATCH** /tenants/{tenantsId} | Updates a tenants document
[**posttenants**](TenantsApi.md#posttenants) | **POST** /tenants | Stores one or more tenants.
[**puttenants_item**](TenantsApi.md#puttenants_item) | **PUT** /tenants/{tenantsId} | Replaces a tenants document

# **deletetenants_item**
> deletetenants_item(tenants_id, if_match)

Deletes a tenants document

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
tenants_id = 'tenants_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a tenants document
    api_instance.deletetenants_item(tenants_id, if_match)
except ApiException as e:
    print("Exception when calling TenantsApi->deletetenants_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenants_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gettenants**
> InlineResponse20012 gettenants(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more tenants

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more tenants
    api_response = api_instance.gettenants(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->gettenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gettenants_item**
> Tenants gettenants_item(tenants_id)

Retrieves a tenants document

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
tenants_id = 'tenants_id_example' # str | 

try:
    # Retrieves a tenants document
    api_response = api_instance.gettenants_item(tenants_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->gettenants_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenants_id** | **str**|  | 

### Return type

[**Tenants**](Tenants.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchtenants_item**
> patchtenants_item(body, if_match, tenants_id)

Updates a tenants document

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Tenants() # Tenants | A tenants or list of tenants documents
if_match = 'if_match_example' # str | Current value of the _etag field
tenants_id = 'tenants_id_example' # str | 

try:
    # Updates a tenants document
    api_instance.patchtenants_item(body, if_match, tenants_id)
except ApiException as e:
    print("Exception when calling TenantsApi->patchtenants_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tenants**](Tenants.md)| A tenants or list of tenants documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **tenants_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **posttenants**
> posttenants(body)

Stores one or more tenants.

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Tenants() # Tenants | A tenants or list of tenants documents

try:
    # Stores one or more tenants.
    api_instance.posttenants(body)
except ApiException as e:
    print("Exception when calling TenantsApi->posttenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tenants**](Tenants.md)| A tenants or list of tenants documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **puttenants_item**
> puttenants_item(body, if_match, tenants_id)

Replaces a tenants document

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Tenants() # Tenants | A tenants or list of tenants documents
if_match = 'if_match_example' # str | Current value of the _etag field
tenants_id = 'tenants_id_example' # str | 

try:
    # Replaces a tenants document
    api_instance.puttenants_item(body, if_match, tenants_id)
except ApiException as e:
    print("Exception when calling TenantsApi->puttenants_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tenants**](Tenants.md)| A tenants or list of tenants documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **tenants_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

