#MIT License

#Copyright (c) 2023 Mahdi SMIDA

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

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
