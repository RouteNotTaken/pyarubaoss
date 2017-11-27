#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


### Working with VLANs Directory

def get_vlans(auth):
    url_vlans = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans"
    r = requests.get(url_vlans, headers=auth.cookie)
    try:
        vlans = json.loads(r.text)['vlan_element']
        return vlans
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_vlans: An Error has occured"


def get_vlan(auth, vlan_id):
    url_vlan = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans/" + str(vlan_id)
    r = requests.get(url_vlan, headers=auth.cookie)
    try:
        vlan = json.loads(r.text)
        return vlan
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_vlan: An Error has occured"


def create_vlan(auth, vlan_id, vlan_name):
    url_vlans = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans"
    payload_vlan = "{\"vlan_id\":" + str(vlan_id) + ",\"name\":\"" + vlan_name + "\"}"
    try:
        r = requests.post(url_vlans, data = payload_vlan, headers=auth.cookie)
        return r.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " create_vlan: An Error has occured"

def modify_vlan(auth, vlan_id, vlan_name):
    url_vlan = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans/" + str(vlan_id)
    payload_vlan = "{\"vlan_id\":" + str(vlan_id) + ",\"name\":\"" + vlan_name + "\"}"
    try:
        r = requests.put(url_vlan, data=payload_vlan, headers=auth.cookie)
        return r.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " modify_vlan: An Error has occured"

def delete_vlan(auth, vlan_id):
    payload_vlan = "{\"vlan_id\":" + str(vlan_id) + "}"
    url_vlans = "http://" + auth.ipaddr + "/rest/"+auth.version+"/vlans/"+str(vlan_id)
    try:
        r = requests.delete(url_vlans, data = payload_vlan, headers=auth.cookie)
        return r.status_code
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " delete_vlan: An Error has occured"

### Working with VLAN Ports

def get_vlan_ports(auth):
    url_vlan_ports = 'http://{}/rest/{}/vlans-ports'.format(auth.ipaddr, auth.version)
    r = requests.get(url_vlan_ports, headers=auth.cookie)
    vlan_ports = json.loads(r.text)
    return vlan_ports


def set_vlan_ports(auth, vlan_id, port_id, port_mode):
    '''
    Example:
    vlan_id: <int>
    port_id: <str>
    port_mode: <str> ('POM_UNTAGGED/POM_TAGGED_STATIC')
    '''
    url_vlan_ports = 'http://{}/rest/{}/vlans-ports'.format(auth.ipaddr, auth.version)
    payload_vlan_ports = {
        'vlan_id': vlan_id,
        'port_id': str(port_id),
        'port_mode': port_mode
    }
    payload_vlan_ports = json.dumps(payload_vlan_ports)
    try:
        r = requests.post(url_vlan_ports, headers=auth.cookie, data=payload_vlan_ports)
        return r.status_code
    except requests.exceptions.RequestException as error:
        return 'Error:\n {} set_vlan_ports: An Error has occured'.format(error)


def del_vlan_ports(auth, vlan_id, port_id):
    url_vlan_ports = 'http://{}/rest/{}/vlans-ports/{}-{}'.format(auth.ipaddr, auth.version, vlan_id, port_id)
    try:
        r = requests.delete(url_vlan_ports, headers=auth.cookie)
        return r.status_code
    except requests.exceptions.RequestException as error:
        return 'Error:\n {} del_vlan_ports: An Error has occured'.format(error)
