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
    raise Exception("Ansible Tower Server  must be provided")
ansible_instance = AAPServer(ansibletower,username,password,apiToken)
request = ansible_instance.create_request()
headers = ansible_instance.create_header(request)

if not isWorkflow:
  api_url = '/api/v2/job_templates/%s/launch/' % job_template_id
  body = {"extra_vars": extra_vars}
  response = request.post(api_url,body= json.dumps(body),contentType="application/json",headers=headers)
  result = json.loads(response.response)
  # Check the response status code to make sure the request was not successful.
  if not response.isSuccessful():
    raise Exception("Failed to run the job template. Server return [%s], with content [%s]" % (response.status, response.response))
  job_id= result["id"]
  print("* [>>>> Job %s Link](%s/#/jobs/%s)" % (str(job_id), ansibletower['url'], str(job_id)))

else:
  api_url = '/api/v2/workflow_job_templates/%s/launch/' % job_template_id
  body = {"extra_vars": extra_vars}
  response = request.post(api_url,body= json.dumps(body),contentType="application/json",headers=headers)
  result = json.loads(response.response)
  # Check the response status code to make sure the request was not successful.
  if not response.isSuccessful():
    raise Exception("Failed to run the workflow job template. Server return [%s], with content [%s]" % (response.status, response.response))

  job_id= result["id"]
  print("* [>>>> Workflow job %s Link](%s/#/jobs/workflow/%s/output)" % (str(job_id), ansibletower['url'], str(job_id)))


