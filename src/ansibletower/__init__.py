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

from base64 import b64encode
import sys
from xlrelease.HttpRequest import HttpRequest
from com.xebialabs.xlrelease.plugin.webhook import JsonPathResult

class AAPServer:

    def __init__(self, ansibletower , username, password, api_token):
        if ansibletower is None:
            print "No server provided."
            raise Exception
        self.ansibletower = ansibletower
        self.username = username
        self.password = password
        self.api_token = api_token

    def create_request(self):
        params = self.ansibletower.copy()
        if params['apiToken'] and params['password']:
            raise Exception("\nYou have set both password and API Token but only one is allowed (either Username/Password or API Token)")

        elif params['apiToken']:
            params.pop('username')
            params.pop('password')

        elif params['username'] and params['password']:
            params.pop('apiToken')

        elif self.api_token:
            params['apiToken']= self.api_token
        elif self.username and self.password and not self.api_token:
            params['username'] = self.username
            params['password'] = self.password
        else:
            raise Exception("\n check your connection parameters")
        return HttpRequest(params)

    def create_header(self, request):
        headers = None
        if self.api_token:
            headers = {'Authorization': 'Bearer %s' % (self.api_token)}
        elif self.password and self.username :
            headers = {'Authorization': 'Basic %s' % b64encode('%s:%s' % (self.username, self.password))}
        elif self.password and self.ansibletower['username']:
            headers = {'Authorization': 'Basic %s' % b64encode('%s:%s' % (self.ansibletower['username'], self.password))}
        elif self.username and self.ansibletower['password']:
            headers = {'Authorization': 'Basic %s' % b64encode('%s:%s' % (self.username , self.ansibletower['password']))}           
        elif self.ansibletower['username'] and self.ansibletower['password']:
            headers = {'Authorization': 'Basic %s' % b64encode('%s:%s' % (self.ansibletower['username'] , self.ansibletower['password']))}
        elif self.ansibletower['apiToken']:
            headers = {'Authorization': 'Bearer %s' % (self.ansibletower['apiToken'])}
        else:
            raise Exception('Error! check your request information')
        return headers
