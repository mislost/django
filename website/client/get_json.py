#!/usr/bin/python
# coding:utf-8
import json
f =  file('/root/core/website/client/data/clients.json')
s = json.load(f)
List = []
banks = {"CMB":u"招","ABC":u"农","ICBC":u"工","CCB":u"建","BCM":u"交"}
for i in s:
    hostname = i
    client_infos = s[i]
    clients = []
    l = []
    for j in client_infos:
        client = []
        bank = banks[j['bank_flag']]
        name = j['card_display_name']
        state = j['login']
        client.append(bank)
        client.append(name)
        client.append(state)
        clients.extend(client)
    l = [hostname]
    l.extend(clients)
    List.append(l)

print List
