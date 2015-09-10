# -*- coding:utf-8 -*-
#from stronghold.decorators import public
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
import json
from django.utils.safestring import SafeString
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/root/core/website/client/code")
import aws
# Create your views here.
def acl(request):
    return render(request,'apache.html')

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    next_url = request.POST["next"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user) 
        return HttpResponseRedirect(next_url)
    else:
        return HttpResponse('username or password is errors!')

@login_required
def Servers(request):
    servers = aws.ec2_instances()
    return render(request,'servers.html',{'Servers' : json.dumps(servers)})


def index(request):
    f =  file('/root/core/website/client/data/clients.json')
    s = json.load(f)
    #return render(request,'index.html',{'Dict':json.dumps(s)})
    return HttpResponse('index page')

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
            status = j['login']
            server[bank_id] =  { "bank_flag" : bank , "name" : name ,"login" : status } 
            bank_id += 1
        servers[hostname] = server
    return render(request,'data.html',{'servers':json.dumps(servers)})

def Ajax(request):
    return render(request,'ajax.html')

