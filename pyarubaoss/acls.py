#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_acls(auth):
    url = 'http://{}/rest/{}/acls'.format(auth.ipaddr, auth.version)
    try:
        r = requests.get(url, headers = auth.cookie)
        acls = json.loads(r.text)['acl_element']
        return acls
    except requests.exceptions.RequestException as error:
        return 'Error:\n' + str(error) + ' get_acls: An Error has occured'

def get_acl_rules(auth, acl_id=None):
    if acl_id:
        url = 'http://{}/rest/{}/acls/{}/rules'.format(auth.ipaddr, auth.version, acl_id)
    else:
        url = 'http://{}/rest/{}/acls/rules'.format(auth.ipaddr, auth.version)

    try:
        r = requests.get(url, headers = auth.cookie)
        acl_rules = json.loads(r.text)['acl_rule_element']
        return acl_rules
    except requests.exceptions.RequestException as error:
        return 'Error:\n' + str(error) + ' get_acl_rules: An Error has occured'
