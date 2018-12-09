#!usrbinpython3
#iss_tracker 
#By Davistar
#coding:utf-8

import requests
import os
import subprocess
import sys
import json
import urllib3
import time
import platform
from datetime import datetime
import random

class config():
    iss_station = 'https://api.wheretheiss.at/v1/satellites/25544/'
    geolocate_api = 'https://api.wheretheiss.at/v1/coordinates/'
    geolocate2_api = 'https://restcountries.eu/rest/v2/alpha/'
    done = '\033[1;92m'
    fail = '\033[1;91m'
    banner = '''
    \033[1;96m██╗   ███████╗   ███████╗
    \033[1;96m██║   ██╔════╝   ██╔════╝
    \033[1;96m██║   ███████╗   ███████╗
    \033[1;96m██║   ╚════██║   ╚════██║
    \033[1;96m██║██╗███████║██╗███████║
    \033[1;96m╚═╝╚═╝╚══════╝╚═╝╚══════╝
        \033[1;94m By Dxvistxr | instagram : dxvistxr
    '''
    banner2 = '''
    ██╗   ███████╗   ███████╗
    ██║   ██╔════╝   ██╔════╝
    ██║   ███████╗   ███████╗
    ██║   ╚════██║   ╚════██║
    ██║██╗███████║██╗███████║
    ╚═╝╚═╝╚══════╝╚═╝╚══════╝
            Par Dxvistxr | instagram : dxvistxr
    '''

    myip = 'https://ifconfig.me/all.json'



def ipgeo(ip):
    requests_myip = requests.get('https://ipinfo.io/'+ip+'/geo')
    content_myip = requests_myip.text
    obj_ip = json.loads(content_myip)
    yourcity = obj_ip['city']
    yourregion = obj_ip['region']
    yourcountry = obj_ip['country']
    yourloc = obj_ip['loc']
    yourpostal = obj_ip['postal']
    
    if 'Windows' not in platform.platform():
        print('\033[1;96m[\033[1;94m*\033[1;96m] YOUR CITY : \033[1;92m'+str(yourcity))
        print('\033[1;96m[\033[1;94m*\033[1;96m] YOUR REGION : \033[1;92m'+str(yourregion))
        print('\033[1;96m[\033[1;94m*\033[1;96m] YOUR COUNTRY : \033[1;92m'+str(yourcountry))
        print('\033[1;96m[\033[1;94m*\033[1;96m] YOUR LOCATION : \033[1;92m'+str(yourloc))
        print('\033[1;96m[\033[1;94m*\033[1;96m] YOUR POSTAL : \033[1;92m'+str(yourpostal))
    
    if 'Linux' not in platform.platform():
        print('[*] YOUR CITY : '+str(yourcity))
        print('[*] YOUR REGION : '+str(yourregion))
        print('[*] YOUR COUNTRY : '+str(yourcountry))
        print('[*] YOUR LOCATION : '+str(yourloc))
        print('[*] YOUR POSTAL : '+str(yourpostal))


def mylocation():
    mylocation_requests = requests.get(config.myip)
    content_ip = mylocation_requests.text
    oci = json.loads(content_ip)
    yourip = oci['ip_addr']
    rhost = oci['remote_host']
    ua = oci['user_agent']
    port = oci['port']
    method = oci['method']
    yourheaders = mylocation_requests.headers
    if 'Windows' not in platform.platform():
        print('\033[1;96m[\033[1;94m*\033[1;96m] YOUR INFORMATIONS \033[1;96m[\033[1;94m*\033[1;96m]')
        print('\033[1;96m[\033[1;94m*\033[1;96m] IP : \033[1;92m'+str(yourip))
        ipgeo(yourip)
        print('\033[1;96m[\033[1;94m*\033[1;96m] REMOTE HOST : \033[1;92m'+str(rhost))
        print('\033[1;96m[\033[1;94m*\033[1;96m] USER-AGENT : \033[1;92m'+str(ua))
        print('\033[1;96m[\033[1;94m*\033[1;96m] PORT : \033[1;92m'+str(port))
        print('\033[1;96m[\033[1;94m*\033[1;96m] METHOD : \033[1;92m'+str(method))
        print('\033[1;96m[\033[1;94m*\033[1;96m] HEADERS : \033[1;92m'+str(yourheaders))
    
    if 'Linux' not in platform.platform():
        print('[*] YOUR INFORMATIONS [*] ')
        print('[*] IP : '+str(yourip))
        ipgeo(yourip)
        print('[*] REMOTE HOST : '+str(rhost))
        print('[*] USER-AGENT : '+str(ua))
        print('[*] PORT : '+str(port))
        print('[*] METHOD : '+str(method))
        print('[*] HEADERS : '+str(yourheaders))


def requests_status():
    r1 = requests.get(config.iss_station)
    res1_request = r1.headers
    r2 = requests.get(config.geolocate_api)
    res2_request = r2.headers
    r3 = requests.get(config.geolocate2_api)
    res3_request = r3.headers
    print('[      REQUESTS INFO / REQUESTS HTTP ')
    print('[*] HTTP HEADERS  REQUESTS GET')
    print('[*] API : '+str(config.iss_station))
    print('[*] HEADERS => '+str(config.iss_station)+'\n'+str(res1_request))
    print('[********************************************]')
    print('[*] API : '+str(config.geolocate_api))
    print('[*] HEADERS => '+str(config.geolocate_api)+'\n'+str(res2_request))
    print('[*******************************************]')
    print('[*] API : '+str(config.geolocate2_api))
    print('[*] HEADERS => '+str(config.geolocate2_api)+'\n'+str(res3_request))
    print('[*******************************************]')


def systeminformation():
    sys_os = platform.system()
    version = platform.version()
    architecture = platform.machine()
    proc = platform.processor()

    if 'Linux' not in platform.platform():
        print('[      SYSTEM INFO            ]')
        print('[*] OS : '+str(sys_os+version))
        print('[*] ARCHITECTURE : '+str(architecture))
        print('[*] PROCESSOR : '+str(proc))
    
    if 'Windows' not in platform.platform():
        cpuinfo = os.system('cat /proc/cpuinfo | head')
        nameinfo = os.system('uname -n')
        hostname = os.system('hostname -I')
        print('[*] OS : '+str(sys_os))
        print('[*] DISTRIBUTION : '+str(version))
        print('[*] ARCHITECTURE : '+str(architecture))
        print('[*] PROCESSOR : '+str(proc))
        print('[*] CPUINFO : '+str(cpuinfo))
        print('[*] MACHINE NAME : '+str(nameinfo))
        print('[*] HOSTNAME : '+str(hostname))


def iss_location():
    iss = requests.get(config.iss_station)
    content = iss.text
    obj = json.loads(content)
    iss_name = obj['name']
    iss_id = obj['id']
    iss_lat = obj['latitude']
    iss_lon = obj['longitude']
    iss_vel = obj['velocity']
    iss_vis = obj['visibility']
    iss_f = obj['footprint']
    iss_ts = obj['timestamp']
    iss_dyn = obj['daynum']
    iss_sla = obj['solar_lat']
    iss_slo = obj['solar_lon']
    iss_units = obj['units']

    if 'Linux' not in platform.platform():
        print('[************************************]')
        print('[          SATELLITES INFO           ]')
        print('[************************************]')
        print('[*] SATELLITES NAME : '+str(iss_name))
        print('[*] SATELLITES ID : '+str(iss_id))
        print('[*] LATITUDE : '+str(iss_lat))
        print('[*] LONGITUDE : '+str(iss_lon))
        print('[*] VELOCITY : '+str(iss_vel))
        print('[*] VISIBILITY : '+str(iss_vis))
        print('[*] FOOTPRINT : '+str(iss_f))
        print('[*] TIMESTAMP : '+str(iss_ts))
        print('[*] DAYNUMBER : '+str(iss_dyn))
        print('[*] SOLAR LATITUDE : '+str(iss_sla))
        print('[*] SOLAR LONGITUDE : '+str(iss_slo))
        print('[*] UNITS : '+str(iss_units))
    
    if 'Windows' not in platform.platform():
        print('\033[1;96m[\033[1;94m************************************\033[1;96m]')
        print('\033[1;96m[          \033[1;92mSATELLITES INFO           \033[1;96m]')
        print('\033[1;96m[\033[1;94m************************************\033[1;96m]')
        print('[*] SATELLITES NAME : '+str(iss_name))
        print('[*] SATELLITES ID : '+str(iss_id))
        print('[*] LATITUDE : '+str(iss_lat))
        print('[*] LONGITUDE : '+str(iss_lon))
        print('[*] VELOCITY : '+str(iss_vel))
        print('[*] VISIBILITY : '+str(iss_vis))
        print('[*] FOOTPRINT : '+str(iss_f))
        print('[*] TIMESTAMP : '+str(iss_ts))
        print('[*] DAYNUMBER : '+str(iss_dyn))
        print('[*] SOLAR LATITUDE : '+str(iss_sla))
        print('[*] SOLAR LONGITUDE : '+str(iss_slo))
        print('[*] UNITS : '+str(iss_units))

def iss_location2():
    iss_gmap = requests.get(config.geolocate_api+str(iss_lat)+','+str(iss_lon))
    content_gmap = iss_gmap.text
    obj2 = json.loads(content_gmap)
    gmap_link = obj2['map_url']
    gmap_code = obj2['country_code']
    
    if 'Linux' not in platform.platform():
        print('[*] GOOGLE MAP : '+str(gmap_link))
        print('[*] COUNTRY CODE : '+str(gmap_code))
    
    if 'Windows' not in platform.platform():
        print('[*] GOOGLE MAP : '+str(gmap_link))
        print('[*] COUNTRY CODE : '+str(gmap_code))


def error_iss_location2():
    iss_gmap_error = requests.get(config.iss_station)
    content_error = iss_gmap_error.text
    payload_object = json.loads(content_error)
    po = payload_object['latitude']
    po2 = payload_object['longitude']
    var_gmap = 'https://maps.google.com/maps?q='+str(po)+','+str(po2)+'&z=4'
    print('[*] GOOLE MAP LINK : '+str(var_gmap))


def iss_location3():
    iss_geo = requests.get(config.geolocate2_api+gmap_code)
    content_geo = iss_geo.text
    obj3 = json.loads(content_geo)
    country_name = obj3['name']
    alphacode = obj3['alpha3Code']
    capital_code = obj3['capital']
    obj3region = obj3['region']
    obj3subregion = obj3['subregion']
    obj3population = obj3['population']
    obj3latlng = obj3['latlng']
    obj3timezones = obj3['timezones']
    obj3nativename = obj3['nativeName']
    obj3numericCode = obj3['numericCode']
    obj3currencies = obj3['currencies']
    obj3langages = obj3['languages']
    obj3translations = obj3['translations']

    if 'Linux' not in platform.platform():
        print('[*] COUNTRY NAME : '+str(country_name))
        print('[*] ALPHACODE : '+str(alphacode))
        print('[*] CAPITAL COUNTRY : '+str(capital_code))
        print('[*] REGION : '+str(obj3region))
        print('[*] SUBREGION : '+str(obj3subregion))
        print('[*] POPULATION : '+str(obj3population))
        print('[*] LAT - LONG COUNTRY : '+str(obj3latlng))
        print('[*] TIMEZONES : '+str(obj3timezones))
        print('[*] NATIVE NAME : '+str(obj3nativename))
        print('[*] NUMERIC CODE : '+str(obj3numericCode))
        print('[*] CURRENCIES : '+str(obj3currencies))
        print('[*] LANGAGES COUNTRY : '+str(obj3langages))
        print('[*] TRANSLATIONS LANGAGE : '+str(obj3translations))
    
    if 'Windows' not in platform.platform():
        print('[*] COUNTRY NAME : '+str(country_name))
        print('[*] ALPHACODE : '+str(alphacode))
        print('[*] CAPITAL COUNTRY : '+str(capital_code))
        print('[*] REGION : '+str(obj3region))
        print('[*] SUBREGION : '+str(obj3subregion))
        print('[*] POPULATION : '+str(obj3population))
        print('[*] LAT - LONG COUNTRY : '+str(obj3latlng))
        print('[*] TIMEZONES : '+str(obj3timezones))
        print('[*] NATIVE NAME : '+str(obj3nativename))
        print('[*] NUMERIC CODE : '+str(obj3numericCode))
        print('[*] CURRENCIES : '+str(obj3currencies))
        print('[*] LANGAGES COUNTRY : '+str(obj3langages))
        print('[*] TRANSLATIONS LANGAGE : '+str(obj3translations))
    
    

def main():
    if 'Linux' not in platform.platform():
        os.system('cls')
        os.system('cls')
        print(config.banner2)
        while True:
            main_var = str(input('[I.S.S]> '))
                
            if main_var =='help':
                print('[********************************]')
                print('[       HELP COMMANDS            ]')
                print('[********************************]')
                print('[ help         | show help      ]')
                print('[ mylocation   | show mylocation]')
                print('[ isstrack     | track I.S.S    ]')
                print('[ request      | show requests  ]')
                print('[ sysinfo      | show sysinfo   ]')
                print('[ all          | show all       ]')
                print('[ clear        | clear channel  ]')
                print('[ credits      | credits        ]')
                print('[ banner       | print banner   ]')
                print('[ quit         | exit console   ]')
                print('[********************************]')
                
            if main_var =='mylocation':
                mylocation()
                
            if main_var =='isstrack':
                try:
                    iss_location()
                except:
                    print('[*] Error MODULE ISS_LOCATION[1]')
                    pass
                
                try:
                    iss_location2()
                except:
                    error_iss_location2()
                    pass
                
                try:
                    iss_location3()
                except:
                    pass
                
            if main_var =='request':
                try:
                    requests_status()
                except:
                    pass
                
            if main_var =='sysinfo':
                systeminformation()
                
            if main_var =='quit':
                sys.exit()
                break
                
            if main_var =='all':
                try:
                    mylocation()
                except:
                    pass
                
                try:
                    requests_status()
                except:
                    pass
                
                try:
                    systeminformation()
                except:
                    pass
                
                try:
                    iss_location()
                except:
                    print('[*] ISS_LOCATION 1 ERROR MODULE')
                
                try:
                    iss_location2()
                except:
                    error_iss_location2()
                    pass
                
                try:
                    iss_location3()
                except:
                    pass
                
            if main_var =='cls':
                os.system('cls')
                os.system('cls')
                print(config.banner2)
            
            if main_var =='credits':
                print('[*] BY DXVISTXR')
                print('[*] instagram : dxvistxr')
                print('[*] youtube : Davistar')
            
            if main_var =='banner':
                print(config.banner2)

    
    if 'Windows' not in platform.platform():
        os.system('clear')
        os.system('clear')
        print(config.banner)
        while True:
            main_var = str(input('[I.S.S]> '))
                
            if main_var =='help':
                print('[********************************]')
                print('[       HELP COMMANDS            ]')
                print('[********************************]')
                print('[ help         | show help      ]')
                print('[ mylocation   | show mylocation]')
                print('[ isstrack     | track I.S.S    ]')
                print('[ request      | show requests  ]')
                print('[ sysinfo      | show sysinfo   ]')
                print('[ all          | show all       ]')
                print('[ clear        | clear channel  ]')
                print('[ credits      | show credits   ]')
                print('[ banner       | show banner    ]')
                print('[ quit         | exit console   ]')
                print('[********************************]')
                
            if main_var =='mylocation':
                mylocation()
                
            if main_var =='isstrack':
                try:
                    iss_location()
                except:
                    print('[*] ERROR Module ISS_LOCATION[1]')
                    pass
                
                try:
                    iss_location2()
                except:
                    error_iss_location2()
                    pass
                
                try:
                    iss_location3()
                except:
                    pass
                
            if main_var =='request':
                try:
                    requests_status()
                except:
                    pass
                
            if main_var =='sysinfo':
                systeminformation()
                
            if main_var =='quit':
                sys.exit('Exiting Created BY Davistar')
                break
                
            if main_var =='all':
                try:
                    mylocation()
                except:
                    print('[*] MYLOCATION MODULE ERROR')
                    pass
                
                try:
                    requests_status()
                except:
                    print('[*] REQUESTS MODULE ERROR')
                    pass
                
                try:
                    systeminformation()
                except:
                    print('[*] SYSINFO ERROR MODULE ')
                    pass
                
                try:
                    iss_location()
                except:
                    print('[*] ISS_LOCATION ERROR MODULE')
                    pass
                
                try:
                    iss_location2()
                except:
                    error_iss_location2()
                    pass
                
                try:
                    iss_location3()
                except:
                    pass
                
            if main_var =='clear':
                os.system('clear')
                os.system('clear')
                print(config.banner)
            
            if main_var =='credits':
                print('[*] BY DXVISTXR')
                print('[*] instagram : dxvistxr')
                print('[*] youtube : Davistar')
            
            if main_var =='banner':
                print(config.banner)

main()