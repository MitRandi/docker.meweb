#!/usr/bin/python
# -*- coding: utf-8 -*-

from Connection import DockerHTTPConnection
import pprint
import json

class DockerContainer():
    def __init__(self):
        self.requests = DockerHTTPConnection()

    def ps(self):
        url = 'containers/json'
        data = {'all': True}
        response = self.requests.GET(url, data)
        docker_containers = []
        for conteiner in response.json():
            container_attr = {}
            container_attr["Id"] = conteiner["Id"]
            container_attr["Image"] = conteiner["Image"]
            container_attr["Command"] = conteiner["Command"]
            container_attr["Status"] = conteiner["Status"]
            docker_containers.append(container_attr)
        return docker_containers

    def create(self, data):
        url = 'containers/create'
        # try 
        self.requests.POST(url, __create_config_file(data))

    def delete(self, container_id):
        url = 'containers/' + container_id
        # try
        self.requests.DELETE(url)

    def start(self, container_id):
        url = 'containers/' + container_id + '/start'
        # try
        self.requests.POST(url)

    def stop(self, container_id):
        url = 'containers/' + container_id + '/stop'
        # try
        self.requests.POST(url)

    def logs(self, container_id):
        url = 'containers/' + container_id + '/logs'
        # try
        self.requests.GET(url)

if __name__ == '__main__':
    obj = DockerContainer()
    pprint.pprint(obj.ps())
