
import urllib2
import json
import time
import os
precv=0
precf=0

def get_page_data(page_id,access_token):
    api_endpoint = "https://graph.facebook.com/v3.0/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,fan_count,unread_notif_count,notifications{title},link&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason
        
while 1:
    page_id = "825164851011192" # username or id 
    token = "EAACEdEose0cBAME9ZCWsp2yNpAD2i5uJ3EpFSWz3fdGtCLYg7BsPtzKVEiyeJZCrrQ6v7D2bqRFW2l4wWJSy4gJaKdZB6wiZACq2OAm67ALzfwOnCVZB75fkdf9uhOqZCB07GXzyWQBtQDtjjulD61oThyIhZCGLTVU4PEKatjEdYlg4yOk89V1fAxg2BUxsaXU5V65aCjvVwZDZD"  # Access Token
    page_data = get_page_data(page_id,token)
    fan=page_data['fan_count']
    notif=page_data['unread_notif_count']
    if(precf<fan  or precv<notif):      
        bash='flite -voice slt -t "Page name: '+ page_data['name'] + '"'
        os.system(bash)
        print('                      ')
        print('                      ')
        print('                      ')
        print('                      ')
        c=page_data['notifications']['data'][0]['title'].encode('utf-8').strip()
        bash='flite -voice slt -t "New notification : '+ c+ '"'
        os.system(bash)
        print('                      ')
        print('                      ')
        print('                      ')
        print('                      ')
        
        bash='flite -voice slt -t "Followers : '+ str(page_data['fan_count'] )+ '"'
        os.system(bash)
        print('                      ')
        print('                      ')
        print('                      ')
        bash='flite -voice slt -t "Notifications : '+ str(page_data['unread_notif_count']) + '"'
        os.system(bash)
        precf=fan
        precv=notif
    time.sleep(0.5)
