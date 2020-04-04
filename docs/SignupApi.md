# swagger_client.SignupApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletesignup_item**](SignupApi.md#deletesignup_item) | **DELETE** /signup/{signupId} | Deletes a signup document
[**getsignup_item**](SignupApi.md#getsignup_item) | **GET** /signup/{signupId} | Retrieves a signup document
[**patchsignup_item**](SignupApi.md#patchsignup_item) | **PATCH** /signup/{signupId} | Updates a signup document
[**postsignup**](SignupApi.md#postsignup) | **POST** /signup | Stores one signup.
[**putsignup_item**](SignupApi.md#putsignup_item) | **PUT** /signup/{signupId} | Replaces a signup document

# **deletesignup_item**
> deletesignup_item(signup_id, if_match)

Deletes a signup document

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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
signup_id = 'signup_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a signup document
    api_instance.deletesignup_item(signup_id, if_match)
except ApiException as e:
    print("Exception when calling SignupApi->deletesignup_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getsignup_item**
> Signup getsignup_item(signup_id)

Retrieves a signup document

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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
signup_id = 'signup_id_example' # str | 

try:
    # Retrieves a signup document
    api_response = api_instance.getsignup_item(signup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignupApi->getsignup_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_id** | **str**|  | 

### Return type

[**Signup**](Signup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchsignup_item**
> patchsignup_item(body, if_match, signup_id)

Updates a signup document

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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
body = swagger_client.Signup() # Signup | A signup document.
if_match = 'if_match_example' # str | Current value of the _etag field
signup_id = 'signup_id_example' # str | 

try:
    # Updates a signup document
    api_instance.patchsignup_item(body, if_match, signup_id)
except ApiException as e:
    print("Exception when calling SignupApi->patchsignup_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Signup**](Signup.md)| A signup document. | 
 **if_match** | **str**| Current value of the _etag field | 
 **signup_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postsignup**
> postsignup(body)

Stores one signup.

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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
body = swagger_client.Signup() # Signup | A signup document.

try:
    # Stores one signup.
    api_instance.postsignup(body)
except ApiException as e:
    print("Exception when calling SignupApi->postsignup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Signup**](Signup.md)| A signup document. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putsignup_item**
> putsignup_item(body, if_match, signup_id)

Replaces a signup document

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
api_instance = swagger_client.SignupApi(swagger_client.ApiClient(configuration))
body = swagger_client.Signup() # Signup | A signup document.
if_match = 'if_match_example' # str | Current value of the _etag field
signup_id = 'signup_id_example' # str | 

try:
    # Replaces a signup document
    api_instance.putsignup_item(body, if_match, signup_id)
except ApiException as e:
    print("Exception when calling SignupApi->putsignup_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Signup**](Signup.md)| A signup document. | 
 **if_match** | **str**| Current value of the _etag field | 
 **signup_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

