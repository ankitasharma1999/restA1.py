# What is meant by statelessness in RestAPI?

'''Each request from the client to server must contain all the information needed to process that request
and that information cannot be stored at the server side for any future reference. This restriction is
called Statelessness.'''

# What is 403, 503, 301 Status Codes?

# 301

'''The HTTP 301 Moved Permanently status code indicates that the URL requested by the client has been moved 
to a new location. Browsers follow 301 redirects without asking users to perform an action.'''

# 403

'''The 403 Forbidden status code indicates that the user doesn’t have permission to access the requested web page.'''

# 503

'''The 503 Service Unavailable status code indicates that the website server is currently unavailable and,
consequently, cannot process the incoming client request.'''

# Use public API and use all http methods on it.

import requests
import json
api_url="https://jsonplaceholder.typicode.com/todos"
#Get request
response=requests.get(api_url)
print(response.json())

#Post request
api_url="https://jsonplaceholder.typicode.com/todos"
response=requests.post(api_url,json={"name":"ankita"})
print(response.json())

#Put request
response=requests.patch(api_url+"/2",json={"name":"aarav"})
print(response.status_code)
print(response.json())

#Delete request
response=requests.delete(api_url+"/2",)
print(response.status_code)
print(response.json())