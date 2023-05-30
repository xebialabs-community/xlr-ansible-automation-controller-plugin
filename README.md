# xlr-ansible-automation-controller-plugin
a plugin developed to integrate Ansible Automation Platform Controller API with Digiatal.ai Release

# Overview

The plugin acts as a bridge between Digital.ai Release, a comprehensive release orchestration solution, and Ansible Tower (Ansible Automation Platform Controller). It allows users to incorporate Ansible Tower tasks and playbooks directly into their release pipelines, ensuring smooth integration of infrastructure provisioning, configuration management, and application deployments.

# Interfaces

## Connection / Authentication

The authentication page on the Ansible plugin allows users to securely access the plugin using both Basic Authentication and tokens generated from the Ansible Automation Platform. These authentication methods ensure a seamless integration with Digital.ai Release while maintaining robust security measures.

![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/fa278562-b226-4930-8369-3685473993bb)


## Tasks List
The plugin offers a range of tasks to :
- Get information using an Ansible Automation Controller API's endpoint
- Add or Remove a credential from a job template
- Inventory list
- Run job template
- Wait for a job template status (asyn)
- Run and wait for a job template to finish (sync)
-

![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/0e20285c-0e3f-4230-9074-d6f2897a4cfb)

### Run a job template
Input required properties are:
- A valid Ansible Automation Controller server 
- A Job Template ID or name
Input optinal properties are: 
- Extra vars: A string that represents a JSON or YAML formatted dictionary (with escaped parentheses) which includes variables given by the user, including answers to survey questions
- Is Workflow : Check if it's a workflow job template
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/1d38e93d-3711-4259-b34d-32d96693ec36)

#### Results example:
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/ccf85756-37c8-4fc4-8d54-ed3648b336a7)
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/4ac338c7-5404-4113-8550-4fbea4142e26)

### Wait for job status (async)
Input properties:
- Server: Ansible Automation Platform Controller Server to connect to
- Username: Overwrite username if defined in connection for
- Password: Overwrite password if defined in connection for
- Api token: Overwrite API token if defined in connection form
- Max_retries: Max retries default value is infinity
- Wait_interval (required): Wait interval in seconds
- Stop On Failure: if checked it fail task when job fails
- Is workflow: Check if it's a workflow job template


![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/85e1275f-0b72-47c8-95dc-50d21c3767ae)
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/5fd94c9b-cd6e-446a-a0d5-a8cd5877ba0a)

#### Results example:
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/4137d5f9-3bbe-420f-a6d3-9412a44219df)
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/04af168f-b3ea-4f0a-8ba5-54b20262e07b)

### Run and wait for job status (sync)
This task parameters are a fusion of the two previous tasks

![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/0aa1f91f-22a3-49bb-9202-d503fd51bc88)
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/7a97596e-1aaa-40dd-9d83-0ba7c2fa413e)

#### Results example:
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/7e822fb0-c0dc-4cba-bfa1-b801bb84ff46)
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/6eb06c6f-c66d-4390-9168-9c38e5a6487d)

### Get infromation from API endpoint
- Endpoint example:  /api/v2/me
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/301ecb23-fa29-479f-b3ba-f349da1293e3)

#### Results example:
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/c1938b2e-fefe-4751-b4de-cb244f643c73)

### Get inventory List
- Filter: Filter the inventory list. Empty to get the hole list. Example: ?page=1
![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/31a50882-1b2f-4a5d-a1f3-0d6b50bd7ff0)
#### Results example:

![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/73e1013d-f3f8-4a3e-aa54-313576f749ca)

### Add/Remove credential from a job template
- Job template id
- Credential id: Id of this credential
- Remove: check if you want to disassociate the credential from the job template

![image](https://github.com/MahdiSMIDA/xlr-ansible-automation-controller-plugin/assets/23388936/1f282c18-5588-4135-ac55-edd9d01d10f6)

