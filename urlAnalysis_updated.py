import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import whois
import requests
from bs4 import BeautifulSoup


#!!! Before running the code, set the parameter columns in the csv file with column names mentioned below
#15 Parameters  :
#   -Protocol (https://, http:// or ftp://) -- Column Name - "Protocol Risk"
#   -Path/Directory -- Column Name - "Path"
#   -Number of sub-domains -- Column Name - "SubDomain Count"
#   -Top level Domain (com, org, net, etc) -- Column Name - "Top-level Domain"
#   -Domain Name (google.com, gov.in) -- Column Name - "Domain Name"
#   -Domain Registration Date (Unsafe, might not work in some cases) -- Column Name - "Domain Registration"
#   -Length of top level domain -- Column Name - "TLD Length"
#   -Length of URL -- Column Name - "URL Length"
#   -Number of special characters ('-','@','#','$',etc) -- Column Name - "Special Character Count"
#   -Number of digits -- Column Name - "Digit Count"
#   -Length of website content -- Column Name - "Content Length"
#   -Number of redirects -- Column Name - "Redirects"
#   -Frames -- Column Name - "Frames"
#   -IFrames -- Column Name - "IFrames"
#   -Number of tags -- Column Name - "Tags"

def scrapper(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    length = len(r.content)
    anchors = len(soup.find_all('a'))

    return [length,anchors]

def scrap(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    
    frames = len(soup.findAll('frame'))
    iframes = len(soup.findAll('iframe'))
    tags = len(soup.findAll())

    return frames,iframes,tags


def get_whois_info(domain_name):
    try:
        # Query WHOIS information for the domain
        whois_info = whois.whois(domain_name)
        
        # Print the WHOIS information
        return whois_info.creation_date

        # You can also access specific WHOIS fields like this:
        # print("Domain Name:", whois_info.domain_name)
        # print("Registrar:", whois_info.registrar)
        # print("Creation Date:", whois_info.creation_date)
        # ...
        
    except whois.parser.PywhoisError as e:
        return("Error:", e)


legalDomainDatabase= pd.read_csv("dbAttempt1.csv")


columns=["Protocol Risk", "Path",
         "SubDomain Count",
         "Top-level Domain",
         "Domain Registration",
         "Domain Name",
         "TLD Length",
         "URL Length",
         '?','-','%','=','@','!','^','&','#',
         "Digit Count",
         "Content Length",
         "Redirects",
         "Frames",
         "IFrames",
         "Tags"]


for i in columns:
    if i not in legalDomainDatabase:
        legalDomainDatabase[i] = None

for i in legalDomainDatabase.index:
    print(i)
    originalURL=str(legalDomainDatabase["URL"][i])
    protocolRisk = 0
    if "https://" in originalURL or "http://" in originalURL or "tls://" in originalURL or"ftps://" in originalURL or "ssl://" in originalURL:
        protocolRisk = 1


    # THis is asad removing this code
    # elif "https://" not in originalURL and "ftps://" not in originalURL:
    #     protocolRisk = 0
    # else:
    #     protocolRisk = 0

    legalDomainDatabase["Protocol Risk"][i] = protocolRisk
    
    
    url = re.split("//", originalURL)[1]
    subdomains = re.split("\.", url)
    
    subdomainCount = len(subdomains)
    legalDomainDatabase["SubDomain Count"][i] = subdomainCount

    #legalDomainDatabase["Top-level Domain"][i] = re.split("/",subdomains[-1])[0]


    domainName = ""
    if len(re.split("\.",url))>=2:
        domainName = subdomains[-2]+'.'+(re.split("/",subdomains[-1])[0])

    else:
        domainName = (re.split("/",subdomains[-1])[0])
        #legalDomainDatabase["Domain Name"][i] = domainName



    '''
    THis is asad removing this code
    We are no longer using path as a parameter:

    # if "/" in re.split("\.",url)[-1]:
    #     legalDomainDatabase["Path"][i]=str(re.split("/",url,1)[-1])

    # else:
    #     legalDomainDatabase["Path"][i]="Not Specified"

    '''


    #I'll let this slide for now
    if len(domainName) > 64:
        legalDomainDatabase["Domain Registration"][i] = "Domain too long"
    else:
        legalDomainDatabase["Domain Registration"][i] = get_whois_info(domainName)
    


    specialCharacters=['?','-','%','=','@','!','^','&','#']
    for character in specialCharacters:
        legalDomainDatabase[f"{character}"][i] = 0
        for j in url:
            if j in specialCharacters:
                legalDomainDatabase[f"{character}"][i]+=1
    



    legalDomainDatabase["Digit Count"][i] = 0
    for j in url:
        if ord(j) in range(48,57):
            legalDomainDatabase["Digit Count"][i]+= 1



    
    legalDomainDatabase["TLD Length"][i] = len(re.split("/",subdomains[-1])[0])
    legalDomainDatabase["URL Length"][i] = len(re.split("/",url)[0])


    length, anchors = scrapper(originalURL)
    legalDomainDatabase["Content Length"][i] = length
    legalDomainDatabase["Redirects"][i] = anchors
    
    frames, iframes, tags = scrap(originalURL)
    legalDomainDatabase["Frames"][i] = frames
    legalDomainDatabase["IFrames"][i] = iframes
    legalDomainDatabase["Tags"][i] = tags

legalDomainDatabase.to_csv("Phishing Database 3.csv",index=False)
