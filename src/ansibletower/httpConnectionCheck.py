
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
                                                                                
