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

from xlrelease.HttpRequest import HttpRequest
from org.apache.http.client import ClientProtocolException
from base64 import b64encode

global configuration

params = {'url': configuration.url, 'proxyHost': configuration.proxyHost, 'proxyPort': configuration.proxyPort,
          'proxyUsername': configuration.proxyUsername, 'proxyPassword': configuration.proxyPassword,
          'proxyDomain': configuration.proxyDomain}

path = configuration.checkConfigurationPath
response = None

try:
    headers = None
    if configuration.apiToken and configuration.password:
        raise ValueError("You have set both password and API Token but only one is allowed(either Password or API Token)")
    # Connection using apiToken
    if configuration.apiToken:
        params['apiToken'] = configuration.apiToken
        auth = b64encode('%s:%s' % (configuration.username, configuration.apiToken))
        headers = {'Authorization': 'Bearer %s' % configuration.apiToken}
    # Connection using username/password
    elif configuration.password:
        params['username'] = configuration.username
        params['password'] = configuration.password
        auth = b64encode('%s:%s' % (configuration.username, configuration.password))
        headers = {'Authorization': 'Basic %s' % auth}
    response = HttpRequest(params).get(path,contentType='application/json', headers=headers)
except ClientProtocolException:
    raise Exception("URL is not valid")

# In case of response failure
if not response.isSuccessful():
    reason = "Unknown"
    if response.status == 400:
        reason = "Bad request"
    elif response.status == 401:
        reason = "Unauthorized"
    elif response.status == 403:
        reason = "Forbidden"
    raise Exception("HTTP response code %s (%s)" % (response.status, reason))
                                                                                
