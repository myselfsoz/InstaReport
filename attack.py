#!/usr/bin/env python3
from requests import Session 
from multiprocessing import Process
from sys import exit
import string
import random
import pprin
from utils import print_success
from utils import print_error
from utils import print_status
from utils import parse_proxy_file
from user_agents import get_user_agent
page_headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate","Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3","Cache-Control":"no-cache","Connection":"keep-alive","DNT":"1",}#line:12
report_headers ={"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3","Cache-Control":"no-cache","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","DNT":"1","Host":"help.instagram.com","Origin":"help.instagram.com","Pragma":"no-cache","Referer":"https://help.instagram.com/contact/497253480400030","TE":"Trailers",}#line:13


def random_str (O0O0000000000OOOO ):#line:14
    O00O0OO0O0O0OOOOO =string .ascii_lowercase +string .ascii_uppercase +string .digits #line:15
    return ''.join (random .choice (O00O0OO0O0O0OOOOO )for O0OOO00OO0O0OO00O in range (O0O0000000000OOOO ))#line:16
    
    
    #main profile reporting start.........
def report_profile_attack (p_targetUsername ,p_proxyItems ):#line:17
    _sessionStore =Session()#line:18
    if (p_proxyItems !=None ):#line:19
        _sessionStore.proxies ={"https":"https://"+p_proxyItems ,"http":"https://"+p_proxyItems }#line:20
    randomUserAgent =get_user_agent ()#line:21
    page_headers ["User-Agent"]=randomUserAgent #line:22
    report_headers ["User-Agent"]=randomUserAgent #line:23
    try :#line:24
        fbReq =_sessionStore.get("https://www.facebook.com/",timeout =10 )#line:25
        print(fbReq.text)
    except :#line:26
        print_error ("Connection error! (FacebookRequestsError)")#line:27
        return #line:28
    if (fbReq .status_code !=200 ):#line:29
        print_error ("Connection error! (STATUS CODE:",fbReq .status_code ,")")#line:30
        return #line:31
    if ('["_js_datr","'not in fbReq .text ):#line:32
        print_error ("Connection error! (CookieErrorJSDatr)")#line:33
        return #line:34
    try :#line:35
        OO000O0O00O000O00 =fbReq .text .split ('["_js_datr","')[1 ].split ('",')[0 ]#line:36
    except :#line:37
        print_error ("Connection error! (CookieParsingError)")#line:38
        return #line:39
    _cookieTopst ={"_js_datr":OO000O0O00O000O00 }#line:40
    try :#line:41
        fbReq =_sessionStore .get ("https://help.instagram.com/contact/497253480400030",cookies =_cookieTopst ,headers =page_headers ,timeout =10 )#line:42
    except :#line:43
        print_error ("Connection error! (InstagramRequestsError)")#line:44
        return #line:45
    if (fbReq .status_code !=200 ):#line:46
        print_error ("Connection error! (STATUS CODE:",fbReq .status_code ,")")#line:47
        return #line:48
    if ("datr"not in fbReq .cookies .get_dict ()):#line:49
        print_error ("Connection error! (CookieErrorDatr)")#line:50
        return #line:51
    if ('["LSD",[],{"token":"'not in fbReq .text ):#line:52
        print_error ("Connection error! (CookieErrorLSD)")#line:53
        return #line:54
    if ('"__spin_r":'not in fbReq .text ):#line:55
        print_error ("Connection error! (CookieErrorSpinR)")#line:56
        return #line:57
    if ('"__spin_b":'not in fbReq .text ):#line:58
        print_error ("Connection error! (CookieErrorSpinB)")#line:59
        return #line:60
    if ('"__spin_t":'not in fbReq .text ):#line:61
        print_error ("Connection error! (CookieErrorSpinT)")#line:62
        return #line:63
    if ('"server_revision":'not in fbReq .text ):#line:64
        print_error ("Connection error! (CookieErrorRev)")#line:65
        return #line:66
    if ('"hsi":'not in fbReq .text ):#line:67
        print_error ("Connection error! (CookieErrorHsi)")#line:68
        return #line:69
    try :#line:70
        OOOOOO000OOOO0O00 =fbReq .text .split ('["LSD",[],{"token":"')[1 ].split ('"},')[0 ]#line:71
        OO00O0O0O00OOOOO0 =fbReq .text .split ('"__spin_r":')[1 ].split (',')[0 ]#line:72
        OO00OO000OO000OO0 =fbReq .text .split ('"__spin_b":')[1 ].split (',')[0 ].replace ('"',"")#line:73
        O00O0O0O0O00O0O00 =fbReq .text .split ('"__spin_t":')[1 ].split (',')[0 ]#line:74
        OO0O0OO00OOOOOO0O =fbReq .text .split ('"hsi":')[1 ].split (',')[0 ].replace ('"',"")#line:75
        O000OO0OOO00000OO =fbReq .text .split ('"server_revision":')[1 ].split (',')[0 ].replace ('"',"")#line:76
        O0O0OOOOOO00O00OO =fbReq .cookies .get_dict ()["datr"]#line:77
    except :#line:78
        print_error ("Connection error! (CookieParsingError)")#line:79
        return #line:80
    _cookieTopst_v2 ={"datr":O0O0OOOOOO00O00OO }#line:81
    fbReq_post_Data ={"jazoest":"2723","lsd":OOOOOO000OOOO0O00 ,"instagram_username":p_targetUsername ,"Field241164302734019_iso2_country_code":"TR","Field241164302734019":"Türkiye","support_form_id":"497253480400030","support_form_hidden_fields":"{}","support_form_fact_false_fields":"[]","__user":"0","__a":"1","__dyn":"7xe6Fo4SQ1PyUhxOnFwn84a2i5U4e1Fx-ey8kxx0LxW0DUeUhw5cx60Vo1upE4W0OE2WxO0SobEa81Vrzo5-0jx0Fwww6DwtU6e","__csr":"","__req":"d","__beoa":"0","__pc":"PHASED:DEFAULT","dpr":"1","__rev":O000OO0OOO00000OO ,"__s":"5gbxno:2obi73:56i3vc","__hsi":OO0O0OO00OOOOOO0O ,"__comet_req":"0","__spin_r":OO00O0O0O00OOOOO0 ,"__spin_b":OO00OO000OO000OO0 ,"__spin_t":O00O0O0O0O00O0O00 }#line:82
    try :#line:83
        fbReq =_sessionStore .post ("https://help.instagram.com/ajax/help/contact/submit/page",data =fbReq_post_Data ,headers =report_headers ,cookies =_cookieTopst_v2 ,timeout =10 )#line:84
    except :#line:85s
        print_error ("Connection error occurred (FormRequestsError)")#line:86
        return #line:87
    if (fbReq .status_code !=200 ):#line:88
        print_error ("Connection error occurred (STATUS CODE:",fbReq .status_code ,")")#line:89
        return #line:90
    print_success ("Successfully reported!")#line:91
    
    
def chunks (O0O0O000O000OOOO0 ,O0OO0O0OO0OOOOO00 ):#line:59
    ""#line:60
    for O000000O0OOO00OOO in range (0 ,len (O0O0O000O000OOOO0 ),O0OO0O0OO0OOOOO00 ):#line:61
        yield O0O0O000O000OOOO0 [O000000O0OOO00OOO :O000000O0OOO00OOO +O0OO0O0OO0OOOOO00 ]#line:62  
    
    
def profile_attack_process (_tarUsername ,_proxyEachItem ):#line:65
    if (len (_proxyEachItem )==0 ):#line:66
        for _OOOOO0O00O0OOOOO0 in range (10 ):#line:67
            report_profile_attack (_tarUsername ,None )#line:68
        return #line:69
    for _proxyEachItem_i in _proxyEachItem :#line:71
        report_profile_attack (_tarUsername ,_proxyEachItem_i )#line:72
            
    
if __name__=="__main__":
    proxyfilePath =input ("Enter the path to your proxy list : ")#line:249
    #with open(proxyfilePath) as f:
     #   print(f.read())
    
    parsedProxyFromFile =parse_proxy_file (proxyfilePath )#line:250
    _proxyList =list (chunks (parsedProxyFromFile ,10 ))#line:132
    targetUSername=input("Enter target username :")
    print ("Starting........")#line:134
    print_status ("Profile complaint attack is starting!\n")#line:135
    loop_i_ =1 #line:137
    for proxyEachItems in _proxyList :#line:138
        profileAttProcess =Process (target =profile_attack_process ,args =(targetUSername ,proxyEachItems ,))#line:140
        profileAttProcess .start ()#line:141
        
    #report_profile_attack("",)
