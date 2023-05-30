import json
from xlrelease.HttpRequest import HttpRequest
from ansibletower import AAPServer

if not ansibletower:
    raise Exception("Ansible Tower Server  must be provided")

ansible_instance = AAPServer(ansibletower,username,password,apiToken)
request = ansible_instance.create_request()
headers = ansible_instance.create_header(request)
if inventory_filter:
    api_url = '/api/v2/inventories/'+ inventory_filter
else: 
    api_url = '/api/v2/inventories/'

response = request.get(api_url, contentType='application/json',headers=headers)
result = json.loads(response.response)

# Check the response status code to make sure the request was not successful.
if not response.isSuccessful():
    raise Exception("Failed to get the inventory list. Server return [%s], with content [%s]" % (response.status, response.response))
