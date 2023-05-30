import json
from xlrelease.HttpRequest import HttpRequest
from ansibletower import AAPServer

if not ansibletower:
    raise Exception("Ansible Automation Platform Controller Server  must be provided")

ansible_instance = AAPServer(ansibletower,username,password,apiToken)
request = ansible_instance.create_request()
headers = ansible_instance.create_header(request)

api_url = '/api/v2/job_templates/%s/credentials/' % job_template_id

if Remove:
    body = {
	    	"id": cred_id,
            "disassociate": "true"
            }
else:
    body = {
            "id": cred_id
            }

response = request.post(api_url,body= json.dumps(body),contentType="application/json",headers=headers)

# Check the response status code to make sure the request was not successful.
if not response.isSuccessful() and Remove:
	raise Exception("Failed to remove the credential to the job template. Server return [%s], with content [%s]" % (response.status, response.response))

if not response.isSuccessful() and not Remove :
    raise Exception("Failed to add the credential to the job template. Server return [%s], with content [%s]" % (response.status, response.response))
else:
    print("Done !")
