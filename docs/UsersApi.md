# metacore_api_python_cli.UsersApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteusers_item**](UsersApi.md#deleteusers_item) | **DELETE** /users/{usersId} | Deletes a users document
[**getusers**](UsersApi.md#getusers) | **GET** /users | Retrieves one or more users
[**getusers_item**](UsersApi.md#getusers_item) | **GET** /users/{usersId} | Retrieves a users document
[**patchusers_item**](UsersApi.md#patchusers_item) | **PATCH** /users/{usersId} | Updates a users document
[**postusers**](UsersApi.md#postusers) | **POST** /users | Stores one or more users.
[**putusers_item**](UsersApi.md#putusers_item) | **PUT** /users/{usersId} | Replaces a users document

# **deleteusers_item**
> deleteusers_item(users_id, if_match)

Deletes a users document

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
api_instance = metacore_api_python_cli.UsersApi(metacore_api_python_cli.ApiClient(configuration))
users_id = 'users_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a users document
    api_instance.deleteusers_item(users_id, if_match)
except ApiException as e:
    print("Exception when calling UsersApi->deleteusers_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getusers**
> InlineResponse20013 getusers(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more users

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
api_instance = metacore_api_python_cli.UsersApi(metacore_api_python_cli.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more users
    api_response = api_instance.getusers(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->getusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getusers_item**
> Users getusers_item(users_id)

Retrieves a users document

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
api_instance = metacore_api_python_cli.UsersApi(metacore_api_python_cli.ApiClient(configuration))
users_id = 'users_id_example' # str | 

try:
    # Retrieves a users document
    api_response = api_instance.getusers_item(users_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->getusers_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_id** | **str**|  | 

### Return type

[**Users**](Users.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchusers_item**
> patchusers_item(body, if_match, users_id)

Updates a users document

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
api_instance = metacore_api_python_cli.UsersApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Users() # Users | A users or list of users documents
if_match = 'if_match_example' # str | Current value of the _etag field
users_id = 'users_id_example' # str | 

try:
    # Updates a users document
    api_instance.patchusers_item(body, if_match, users_id)
except ApiException as e:
    print("Exception when calling UsersApi->patchusers_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Users**](Users.md)| A users or list of users documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **users_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postusers**
> postusers(body)

Stores one or more users.

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
api_instance = metacore_api_python_cli.UsersApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Users() # Users | A users or list of users documents

try:
    # Stores one or more users.
    api_instance.postusers(body)
except ApiException as e:
    print("Exception when calling UsersApi->postusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Users**](Users.md)| A users or list of users documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putusers_item**
> putusers_item(body, if_match, users_id)

Replaces a users document

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
api_instance = metacore_api_python_cli.UsersApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Users() # Users | A users or list of users documents
if_match = 'if_match_example' # str | Current value of the _etag field
users_id = 'users_id_example' # str | 

try:
    # Replaces a users document
    api_instance.putusers_item(body, if_match, users_id)
except ApiException as e:
    print("Exception when calling UsersApi->putusers_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Users**](Users.md)| A users or list of users documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **users_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

