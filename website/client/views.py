# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.utils.safestring import SafeString
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.

def index(request):
    f =  file('/root/core/website/client/data/clients.json')
    s = json.load(f)
    return render(request,'index.html',{'Dict':json.dumps(s)})

def test(request):
    f =  file('/root/core/website/client/data/clients.json')
    s = json.load(f)
    banks = {"CMB":u"招","ABC":u"农","ICBC":u"工","CCB":u"建","BCM":u"交"}
    return render(request,'test.html',{'Dict': json.dumps(s),'banks':json.dumps(banks)})

def Datatables(request):
    f =  file('/root/core/website/client/data/clients.json')
    s = json.load(f)
    servers = { } 
    banks = {"CMB":u"招","ABC":u"农","ICBC":u"工","CCB":u"建","BCM":u"交"}
    for i in s:
        hostname = i 
        client_infos = s[i]
        clients = ""
        server = { } 
        bank_id = 0
        for j in client_infos:
            bank = banks[j['bank_flag']]
            name = j['card_display_name']
            server[bank_id] =  { "bank_flag" : bank , "name" : name } 
            bank_id += 1
        servers[hostname] = server
    return render(request,'data.html',{'servers':json.dumps(servers)})

def Ajax(request):
    return render(request,'ajax.html')
