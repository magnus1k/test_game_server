# coding:utf8

from firefly.server.globalobject import netserviceHandle


@netserviceHandle
def echo_1(_conn, data):
    print (data, "On Server")
    return data


@netserviceHandle
def echo_2(_conn, data):
    print (data, "Off Server")
    return data


@netserviceHandle
def run_3(_conn, data):
    print (data, "Between Server")
    return "Hello Client"
