#!/usr/bin/env python 
#  
# IP locations from various JSON sources
# Part 1 of a bigger project
# Sofa King 2/4/17 
# 
from urllib2 import urlopen
from contextlib import closing
import json
import sys
from optparse import OptionParser, OptionGroup

t_ip = '8.8.8.8'
t_city = 'Stubenville'
t_state = 'Ohio'
t_locCode = 'OH'
t_timezone = 'Central'
t_long = '-30.3022'
t_lat = '22.8383'
t_cuntCode = 'US'
t_country = 'United States'
t_zip = 'OU812'
t_org = 'Organization'
t_as = 'Name'
sysVerbose = False
sysDebug = False
sysTarget = 'NULL'

def showSettings():
    if sysVerbose == True:		
        print "Verbose is on."
    if sysDebug == True:		
        print "Debug messages on."

    if sysDebug == False and sysVerbose == False:
        print "Using default settings."

def showData(source):
    sys.stdout.write("IP: '%s' Source: '%s'\n" % (t_ip,source))
    sys.stdout.write("%s, %s - %s - %s\n" % (t_city, t_state, t_zip, t_country))
    if sysVerbose == True:
        sys.stdout.write("%s - %s\n" % (t_org, t_as))
        sys.stdout.write("%s,%s\n" % (t_long, t_lat))
    sys.stdout.write("----------------------------------------\n")

def get_freegeoip(target):
    global t_ip, t_city, t_state, t_locCode, t_timezone, t_long, t_lat, t_cuntCode, t_country, t_zip, t_org, t_as
    url = 'http://freegeoip.net/json/'+target
    with closing(urlopen(url)) as responce:
        location = json.loads(responce.read())
        if sysDebug == True:
            print("DEBUG - get_freegeoip() - raw JSON data")
            print(location)
        t_ip = location['ip']
        t_city = location['city']
        t_state = location['region_name']
        t_locCode = location['region_code']
        t_cuntCode = location['country_code']
        t_country = location['country_name']
        t_zip = location['zip_code']
        t_long = location['longitude']
        t_lat = location['latitude']
        t_as = 'N/A'
        t_org = 'N/A'

def get_ip_api(target):
    global t_ip, t_city, t_state, t_locCode, t_timezone, t_long, t_lat, t_cuntCode, t_country, t_zip, t_org, t_as
    url = 'http://ip-api.com/json/'+target
    with closing(urlopen(url)) as responce:
        location = json.loads(responce.read())
        if sysDebug == True:
            print("DEBUG - get_ip-api() - raw JSON data")
            print(location)
        t_ip = location['query']
        t_city = location['city']
        t_state = location['regionName']
        t_locCode = location['region']
        t_cuntCode = location['countryCode']
        t_country = location['country']
        t_zip = location['zip']
        t_long = location['lon']
        t_lat = location['lat']
        t_as = location['as']
        t_org = location['org']

def get_ipinfo(target):
    global t_ip, t_city, t_state, t_locCode, t_timezone, t_long, t_lat, t_cuntCode, t_country, t_zip, t_org, t_as
    url = 'http://ipinfo.io/'
    url += target
    url += '/json'
    with closing(urlopen(url)) as responce:
        location = json.loads(responce.read())
        if sysDebug == True:
            print("DEBUG - get_ipinfo() - raw JSON data")
            print(location)
        t_ip = location['ip']
        t_city = location['city']
        t_state = location['region']
        t_locCode = 'N/A'
        t_cuntCode = location['country']
        t_country = 'N/A'
        t_zip = location['postal']
        t_long = location['loc']
        t_lat = ' '
        t_as = 'N/A'
        t_org = location['org']

def get_extreme_ip_lookup(target):
    global t_ip, t_city, t_state, t_locCode, t_timezone, t_long, t_lat, t_cuntCode, t_country, t_zip, t_org, t_as
    url = 'http://extreme-ip-lookup.com/json/'+target
    with closing(urlopen(url)) as responce:
        location = json.loads(responce.read())
        if sysDebug == True:
            print("DEBUG - get_extreme_ip_info() - raw JSON data")
            print(location)
        t_ip = location['query']
        t_city = location['city']
        t_state = location['region']
        t_locCode = 'N/A'
        t_cuntCode = location['countryCode']
        t_country = location['country']
        t_zip = 'N/A'
        t_long = location['lon']
        t_lat = location['lat']
        t_as = location['isp']
        t_org = location['org']

def doArgv():
    global sysVerbose
    global sysDebug
    global sysTarget
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    desc = """Gets IP location from multiple sources."""
    parser = OptionParser(description=desc)
    parser.add_option("-v", "--verbose", action="store_true", help="Show all messages.", dest="verbose")
    parser.add_option("-i", "--ip", dest="tip", help = "IP to locate.")
    group = OptionGroup(parser, "Debug Options")
    group.add_option("-d", "--debug", help="Debug messages on", action="store_true", dest="debug")
    parser.add_option_group(group)
    (options,args) = parser.parse_args()
    if options.tip:
        sysTarget = options.tip
    if options.verbose:
        sysVerbose = True
    if options.debug:
        sysDebug = True
    showSettings()



### Main

sys.stdout.write("IP geo locations - By: Sofa King\n")
doArgv()
if sysDebug == True:
    sys.stdout.write("DEBUG: sysTarget = '%s'\n" % sysTarget)
if sysTarget == 'NULL':
    sys.stdout.write("Missing target.  Use -i option with IP address.\n\n")
    sys.exit(-1)

sys.stdout.write("----------------------------------------\n")
get_freegeoip(sysTarget)
showData('freegeoip')
get_ip_api(sysTarget)
showData('ip-api')
get_ipinfo(sysTarget)
showData('ipinfo')
get_extreme_ip_lookup(sysTarget)
showData('extreme-ip-lookup')


