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
    body['extra_vars'] = extra_vars
    body['job_tags'] = ",".join(jobTags)
    body['credentials'] = credentials
    body_as_string = json.dumps(body)
    print "Body returned from create_payload() is %s" % body_as_string
    return body_as_string

if not ansibletower:
    print("Ansible Tower Server  must be provided")
    sys.exit(1)

if wait_interval is None:
    print("wait interval must be provided")
    sys.exit(1)

ansible_instance = AAPServer(ansibletower,username,password,apiToken)
request = ansible_instance.create_request()
headers = ansible_instance.create_header(request)

if not isWorkflow:
  api_url = '/api/v2/job_templates/%s/launch/' % job_template_id
  # body = { "extra_vars": extra_vars}
  body_as_string = create_payload(extra_vars, jobTags, credentials)
  response = request.post(api_url,body=body_as_string,contentType="application/json",headers=headers)
  result = json.loads(response.response)
  # Check the response status code to make sure the request was not successful.

  if not response.isSuccessful():
      print("Failed to run the job template. Server return [%s], with content [%s]" % (response.status, response.response))
      sys.exit(1)

  job_id= result["id"]

  print("```")
  print(">>> Job template launched with job id  " + str(job_id))
  print("```")
  print("\n")

  num_tries = 0
  api_url =  '/api/v2/jobs/%s/' % job_id


  if max_retries:
      while num_tries < int(max_retries):
      # Define the URL for the Ansible Tower API endpoint to launch a job.
          response = request.get(api_url, contentType='application/json',headers=headers)
          if response.isSuccessful():
            result = json.loads(response.response)
            status=result['status']
            print status
            if status not in ["running","pending","waiting"]:
              break
            else:
              num_tries+=1
              time.sleep(float(wait_interval))
          else:
              raise Exception("Failed !. Server return [%s], with content [%s]" % (response.status, response.response))

      if num_tries == int(max_retries):
          # maximum number of tries reached, handle the error
          raise Exception("Error: maximum number of tries reached")
      else:
          # task completed
          print("```")
          print(">>> Task completed after " + str(num_tries) + " tries with status "+ status)
          print("```")
          print("\n")
          print("```")  # started markdown code block
          job_output=request.get(api_url+'stdout/', contentType='text/plain',headers=headers).response
          print(job_output)
          print("```")
          print("\n")  # end markdown code block
          print("* [>>> Job %s Link](%s/#/jobs/%s) <<<" % (str(job_id), ansibletower['url'], str(job_id)))
          print("\n")
          result= job_output

  else:
      while True:
      # Define the URL for the Ansible Tower API endpoint to launch a job.
          response = request.get(api_url, contentType='application/json',headers=headers)
          if response.isSuccessful():
            result = json.loads(response.response)
            status=result['status']
            print status
            if status not in ["running","pending","waiting"]:
              break
            else:
              time.sleep(float(wait_interval))
          else:
              raise Exception("Failed !. Server return [%s], with content [%s]" % (response.status, response.response))
      print("```")
      print(">>> Task completed after " + str(num_tries) + " tries with status "+ status)
      print("```")
      print("\n")
      print("```")  # started markdown code block
      job_output=request.get(api_url+'stdout/', contentType='text/plain',headers=headers).response
      print(job_output)
      print("```")
      print("\n")  # end markdown code block
      print("* [>>> Job %s Link](%s/#/jobs/%s) <<<" % (str(job_id), ansibletower['url'], str(job_id)))
      print("\n")
      result= job_output
else:
  api_url = '/api/v2/workflow_job_templates/%s/launch/' % job_template_id
#   body = { "extra_vars": extra_vars}
  body_as_string = create_payload(extra_vars, jobTags, credentials)
  response = request.post(api_url,body=body_as_string,contentType="application/json",headers=headers)
  result = json.loads(response.response)
  # Check the response status code to make sure the request was not successful.

  if not response.isSuccessful():
      print("Failed to run the workflow job template. Server return [%s], with content [%s]" % (response.status, response.response))
      sys.exit(1)

  job_id= result["id"]

  print("```")
  print(">>> Workflow job template launched with job id  " + str(job_id))
  print("```")
  print("\n")

  num_tries = 0
  api_url =  '/api/v2/workflow_jobs//%s/' % job_id
  if max_retries:
      while num_tries < int(max_retries):
      # Define the URL for the Ansible Tower API endpoint to launch a job.
          response = request.get(api_url, contentType='application/json',headers=headers)
          if response.isSuccessful():
            result = json.loads(response.response)
            status=result['status']
            print status
            if status not in ["running","pending","waiting"]:
              break
            else:
              num_tries+=1
              time.sleep(float(wait_interval))
          else:
              raise Exception("Failed !. Server return [%s], with content [%s]" % (response.status, response.response))

      if num_tries == int(max_retries):
          # maximum number of tries reached, handle the error
          raise Exception("Error: maximum number of tries reached")
      else:
          # task completed
          print("```")
          print(">>> Task completed after " + str(num_tries) + " tries with status "+ status)
          print("```")
          print("\n")
          print("```")  # started markdown code block
          job_output=request.get(api_url+'stdout/', contentType='text/plain',headers=headers).response
          print(job_output)
          print("```")
          print("\n")  # end markdown code block
          print("* [>>> Job %s Link](%s/#/jobs/workflow/%s/output) <<<" % (str(job_id), ansibletower['url'], str(job_id)))
          print("\n")
          result= job_output
  else:
      while True:
      # Define the URL for the Ansible Tower API endpoint to launch a job.
          response = request.get(api_url, contentType='application/json',headers=headers)
          if response.isSuccessful():
            result = json.loads(response.response)
            status=result['status']
            print status
            if status not in ["running","pending","waiting"]:
              break
            else:
              time.sleep(float(wait_interval))
          else:
              raise Exception("Failed !. Server return [%s], with content [%s]" % (response.status, response.response))
      print("```")
      print(">>> Task completed after " + str(num_tries) + " tries with status "+ status)
      print("```")
      print("\n")
      print("```")  # started markdown code block
      job_output=request.get(api_url+'stdout/', contentType='text/plain',headers=headers).response
      print(job_output)
      print("```")
      print("\n")  # end markdown code block
      print("* [>>> Job %s Link](%s/#/jobs/workflow/%s/output) <<<" % (str(job_id), ansibletower['url'], str(job_id)))
      print("\n")
      result= job_output

if stopOnFailure and not status == 'successful':
    raise Exception("Job status is "+ status)
