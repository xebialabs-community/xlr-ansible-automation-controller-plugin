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
import time
import sys

def create_payload(extra_vars, jobTags, credentials):
    body = {}
    if extra_vars:
        body['extra_vars'] = extra_vars
    if jobTags:
        body['job_tags'] = ",".join(jobTags)
    body['credentials'] = credentials
    body_as_string = json.dumps(body)
    print "Body returned from create_payload() is %s" % body_as_string
    return body_as_string

def formatted_print(message):
    print("```")
    print(message)
    print("```")
    print("\n")

if not ansibletower:
    print("Ansible Tower Server  must be provided")
    sys.exit(1)

if wait_interval is None:
    print("wait interval must be provided")
    sys.exit(1)

ansible_instance = AAPServer(ansibletower, username, password, apiToken)
request = ansible_instance.create_request()
headers = ansible_instance.create_header(request)

if isWorkflow:
    launch_path_component = "workflow_job_templates"
    message_text = "workflow job template"
else:
    launch_path_component = "job_templates"
    message_text = "job template"

launch_api_url = '/api/v2/%s/%s/launch/' % (launch_path_component, job_template_id)
body_as_string = create_payload(extra_vars, jobTags, credentials)
response = request.post(launch_api_url,body=body_as_string,contentType="application/json",headers=headers)
result = json.loads(response.response)

if not response.isSuccessful():
  print("Failed to run the %s. Server return [%s], with content [%s]" % (message_text, response.status, response.response))
  sys.exit(1)

job_id= result["id"]
num_tries = 0

formatted_print(">>> %s launched with job id  %s" % (message_text.capitalize(), str(job_id)))

task.setStatusLine("Job id %s launched" % job_id)
task.schedule("ansibletower/launchAndWait.wait_for_completion.py", int(wait_interval))
