#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from pprint import pprint

class DockerHTTPConnection():
    def __init__(self):
        self.__docker_port = '5555'
        self.__docker_address = 'http://localhost:' + self.__docker_port

    def GET(self, url, data=None):
        self.base_url = self.__docker_address + "/" + url
        return requests.get(self.base_url, params=data)

    def POST(self, url, data=None):
        self.base_url = self.__docker_address + "/" + url
        return requests.post(self.base_url, params=data)

if __name__ == '__main__':
    obj = DockerHTTPConnection()
    r = obj.GET('containers/json', {'all': '1'})
    pprint(r.json())
    
