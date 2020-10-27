#! /usr/bin/python3

import requests
import os

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, req):
        req.headers['Authentication'] = "Bearer " + self.token
        return req

url = "https://thisapiisnotreal.com/secret-data"
token = os.getenv("TOP_SECRET_API_TOKEN")

requests.get(url, auth=BearerAuth(token))
print(response.json())
