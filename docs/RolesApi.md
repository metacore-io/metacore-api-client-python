# metacore_api_python_cli.RolesApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteroles_item**](RolesApi.md#deleteroles_item) | **DELETE** /roles/{rolesId} | Deletes a roles document
[**getroles**](RolesApi.md#getroles) | **GET** /roles | Retrieves one or more roles
[**getroles_item**](RolesApi.md#getroles_item) | **GET** /roles/{rolesId} | Retrieves a roles document
[**patchroles_item**](RolesApi.md#patchroles_item) | **PATCH** /roles/{rolesId} | Updates a roles document
[**postroles**](RolesApi.md#postroles) | **POST** /roles | Stores one or more roles.
[**putroles_item**](RolesApi.md#putroles_item) | **PUT** /roles/{rolesId} | Replaces a roles document

# **deleteroles_item**
> deleteroles_item(roles_id, if_match)

Deletes a roles document

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
api_instance = metacore_api_python_cli.RolesApi(metacore_api_python_cli.ApiClient(configuration))
roles_id = 'roles_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a roles document
    api_instance.deleteroles_item(roles_id, if_match)
except ApiException as e:
    print("Exception when calling RolesApi->deleteroles_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getroles**
> InlineResponse20010 getroles(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more roles

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
api_instance = metacore_api_python_cli.RolesApi(metacore_api_python_cli.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more roles
    api_response = api_instance.getroles(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->getroles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getroles_item**
> Roles getroles_item(roles_id)

Retrieves a roles document

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
api_instance = metacore_api_python_cli.RolesApi(metacore_api_python_cli.ApiClient(configuration))
roles_id = 'roles_id_example' # str | 

try:
    # Retrieves a roles document
    api_response = api_instance.getroles_item(roles_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->getroles_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles_id** | **str**|  | 

### Return type

[**Roles**](Roles.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchroles_item**
> patchroles_item(body, if_match, roles_id)

Updates a roles document

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
api_instance = metacore_api_python_cli.RolesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Roles() # Roles | A roles or list of roles documents
if_match = 'if_match_example' # str | Current value of the _etag field
roles_id = 'roles_id_example' # str | 

try:
    # Updates a roles document
    api_instance.patchroles_item(body, if_match, roles_id)
except ApiException as e:
    print("Exception when calling RolesApi->patchroles_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Roles**](Roles.md)| A roles or list of roles documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **roles_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postroles**
> postroles(body)

Stores one or more roles.

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
api_instance = metacore_api_python_cli.RolesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Roles() # Roles | A roles or list of roles documents

try:
    # Stores one or more roles.
    api_instance.postroles(body)
except ApiException as e:
    print("Exception when calling RolesApi->postroles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Roles**](Roles.md)| A roles or list of roles documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putroles_item**
> putroles_item(body, if_match, roles_id)

Replaces a roles document

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
api_instance = metacore_api_python_cli.RolesApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Roles() # Roles | A roles or list of roles documents
if_match = 'if_match_example' # str | Current value of the _etag field
roles_id = 'roles_id_example' # str | 

try:
    # Replaces a roles document
    api_instance.putroles_item(body, if_match, roles_id)
except ApiException as e:
    print("Exception when calling RolesApi->putroles_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Roles**](Roles.md)| A roles or list of roles documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **roles_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

