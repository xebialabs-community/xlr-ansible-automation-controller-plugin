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

def formatted_print(message):
    print("```")
    print(message)
    print("```")
    print("\n")

ansible_instance = AAPServer(ansibletower, username, password, apiToken)
request = ansible_instance.create_request()
headers = ansible_instance.create_header(request)

if isWorkflow:
    status_path_component = "workflow_jobs"
    link_message = "* [>>> Job %s Link](%s/#/jobs/workflow/%s/output) <<<"
else:
    status_path_component = "jobs"
    link_message = "* [>>> Job %s Link](%s/#/jobs/%s) <<<"

api_url =  '/api/v2/%s/%s/' % (status_path_component, job_id)

response = request.get(api_url, contentType='application/json',headers=headers)
num_tries += 1
if response.isSuccessful():
    result = json.loads(response.response)
    status=result['status']
    task.setStatusLine("Job id %s %s" % (job_id, status))
    formatted_print(">>> Job status after " + str(num_tries) + " tries is "+ status)
    print(link_message % (str(job_id), ansibletower['url'], str(job_id)))
    print("\n")
    if status in ["running","pending","waiting"]:
        if max_retries:
            if num_tries > max_retries:
                job_output=request.get(api_url+'stdout/', contentType='text/plain',headers=headers).response
                formatted_print(job_output)
                raise Exception("Error: maximum number of tries reached")
        task.schedule("ansibletower/launchAndWait.wait_for_completion.py", int(wait_interval))
    else:
        job_output=request.get(api_url+'stdout/', contentType='text/plain',headers=headers).response
        formatted_print(job_output)
        result = job_output
        if status in ["failed"]:
            formatted_print(">>> Job failed after " + str(num_tries) + " tries")
            raise Exception("Error: job failed")
else:
    formatted_print(">>> Task failed after " + str(num_tries) + " tries.  Job status was not retrieved.")
    raise Exception("Error: server returned [%s], with content [%s]" % (response.status, response.response))
