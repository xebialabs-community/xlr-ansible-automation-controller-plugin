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


