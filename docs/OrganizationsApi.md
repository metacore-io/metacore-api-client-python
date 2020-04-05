# metacore_api_python_cli.OrganizationsApi

All URIs are relative to *https://api.teke.li/api/v1/obs/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteorganizations_item**](OrganizationsApi.md#deleteorganizations_item) | **DELETE** /orgs/{organizationsId} | Deletes a organizations document
[**getorganizations_item**](OrganizationsApi.md#getorganizations_item) | **GET** /orgs/{organizationsId} | Retrieves a organizations document
[**getorgs**](OrganizationsApi.md#getorgs) | **GET** /orgs | Retrieves one or more orgs
[**patchorganizations_item**](OrganizationsApi.md#patchorganizations_item) | **PATCH** /orgs/{organizationsId} | Updates a organizations document
[**postorgs**](OrganizationsApi.md#postorgs) | **POST** /orgs | Stores one or more orgs.
[**putorganizations_item**](OrganizationsApi.md#putorganizations_item) | **PUT** /orgs/{organizationsId} | Replaces a organizations document

# **deleteorganizations_item**
> deleteorganizations_item(organizations_id, if_match)

Deletes a organizations document

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
api_instance = metacore_api_python_cli.OrganizationsApi(metacore_api_python_cli.ApiClient(configuration))
organizations_id = 'organizations_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a organizations document
    api_instance.deleteorganizations_item(organizations_id, if_match)
except ApiException as e:
    print("Exception when calling OrganizationsApi->deleteorganizations_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getorganizations_item**
> Organizations getorganizations_item(organizations_id)

Retrieves a organizations document

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
api_instance = metacore_api_python_cli.OrganizationsApi(metacore_api_python_cli.ApiClient(configuration))
organizations_id = 'organizations_id_example' # str | 

try:
    # Retrieves a organizations document
    api_response = api_instance.getorganizations_item(organizations_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->getorganizations_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizations_id** | **str**|  | 

### Return type

[**Organizations**](Organizations.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getorgs**
> InlineResponse2007 getorgs(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more orgs

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
api_instance = metacore_api_python_cli.OrganizationsApi(metacore_api_python_cli.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more orgs
    api_response = api_instance.getorgs(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->getorgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patchorganizations_item**
> patchorganizations_item(body, if_match, organizations_id)

Updates a organizations document

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
api_instance = metacore_api_python_cli.OrganizationsApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Organizations() # Organizations | A organizations or list of organizations documents
if_match = 'if_match_example' # str | Current value of the _etag field
organizations_id = 'organizations_id_example' # str | 

try:
    # Updates a organizations document
    api_instance.patchorganizations_item(body, if_match, organizations_id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->patchorganizations_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Organizations**](Organizations.md)| A organizations or list of organizations documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **organizations_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postorgs**
> postorgs(body)

Stores one or more orgs.

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
api_instance = metacore_api_python_cli.OrganizationsApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Organizations() # Organizations | A organizations or list of organizations documents

try:
    # Stores one or more orgs.
    api_instance.postorgs(body)
except ApiException as e:
    print("Exception when calling OrganizationsApi->postorgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Organizations**](Organizations.md)| A organizations or list of organizations documents | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putorganizations_item**
> putorganizations_item(body, if_match, organizations_id)

Replaces a organizations document

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
api_instance = metacore_api_python_cli.OrganizationsApi(metacore_api_python_cli.ApiClient(configuration))
body = metacore_api_python_cli.Organizations() # Organizations | A organizations or list of organizations documents
if_match = 'if_match_example' # str | Current value of the _etag field
organizations_id = 'organizations_id_example' # str | 

try:
    # Replaces a organizations document
    api_instance.putorganizations_item(body, if_match, organizations_id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->putorganizations_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Organizations**](Organizations.md)| A organizations or list of organizations documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **organizations_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

