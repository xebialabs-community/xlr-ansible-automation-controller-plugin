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
import time 
import sys
from ansibletower import AAPServer

if not ansibletower:
    raise Exception("Ansible Tower must be provided")
if job_id is None:
    raise Exception("job id must be provided")
if wait_interval is None:
    raise Exception("wait interval must be provided")
if not isWorkflow:
  num_tries = 0
  api_url =  '/api/v2/jobs/%s/' % job_id
  ansible_instance = AAPServer(ansibletower,username,password,apiToken)
  request = ansible_instance.create_request()
  headers = ansible_instance.create_header(request)
  
  
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
          # task completed successfully
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
      result= job_output
else:
  num_tries = 0
  api_url =  '/api/v2/workflow_jobs/%s/' % job_id
  ansible_instance = AAPServer(ansibletower,username,password,apiToken)
  request = ansible_instance.create_request()
  headers = ansible_instance.create_header(request)
  
  
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
          # task completed successfully
          print("```")
          print(">>> Task completed after " + str(num_tries) + " tries with status "+ status)
          print("```")
          print("\n")
          print("```")  # started markdown code block
          job_output=request.get(api_url+'stdout/', contentType='text/plain',headers=headers).response
          print(job_output)
          print("```")
          print("\n")  # end markdown code block
          print("* [>>> Workflow job %s link](%s/#/jobs/workflow/%s/output) <<<" % (str(job_id), ansibletower['url'], str(job_id)))
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
      print("* [>>> Workflow job %s link](%s/#/jobs/workflow/%s/output)  <<<" % (str(job_id), ansibletower['url'], str(job_id)))    
      result= job_output


if stopOnFailure and not status == 'successful':
    raise Exception("Job status is "+ status)





