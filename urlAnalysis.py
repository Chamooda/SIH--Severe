import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import whois

#10 Parameters :
#   -Protocol (https://, http:// or ftp://)
#   -Path/Directory
#   -Number of sub-domains
#   -Top level Domain (com, org, net, etc)
#   -Domain Name (google.com, gov.in)
#   -Domain Registration Date (Unsafe, might not work in some cases)
#   -Length of top level domain
#   -Length of URL
#   -Number of special characters ('-','@','#','$',etc)
#   -Number of digits

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


legalDomainDatabase=pd.read_csv("dbAttempt1.csv")
for i in legalDomainDatabase.index:
    print(i)
    url=str(legalDomainDatabase["URL"][i])
    protocolRisk="Safe"
    if "http://" in url:
        protocolRisk="Potentially Dangerous"
    elif "://" not in url:
        protocolRisk="Safe"
    elif "https://" not in url and "ftp://" not in url:
        protocolRisk="Dangerous"
    else:
        protocolRisk="Safe"
    legalDomainDatabase["Protocol Risk"][i]=protocolRisk
    
    url=re.split("//",url)[1]
    subdomains=re.split("\.",url)
    subdomainCount=len(subdomains)
    legalDomainDatabase["SubDomain Count"][i]=subdomainCount
    legalDomainDatabase["Top-level Domain"][i]=re.split("/",subdomains[-1])[0]
    if len(re.split("\.",url))>=2:
        domainName=subdomains[-2]+'.'+(re.split("/",subdomains[-1])[0])
    else:
        domainName=(re.split("/",subdomains[-1])[0])
    legalDomainDatabase["Domain Name"][i]=domainName
    if "/" in re.split("\.",url)[-1]:
        legalDomainDatabase["Path"][i]=str(re.split("/",url,1)[-1])
    else:
        legalDomainDatabase["Path"][i]="Not Specified"
    if len(domainName)>64:
        legalDomainDatabase["Domain Registration"][i]="Domain too long"
    else:
        legalDomainDatabase["Domain Registration"][i]=get_whois_info(domainName)
    
    specialCharacters=['?','-','%','=','@','!','^','&']
    legalDomainDatabase["Special Character Count"][i]=0
    for j in url:
        if j in specialCharacters:
            legalDomainDatabase["Special Character Count"][i]+=1
    
    legalDomainDatabase["Digit Count"][i]=0
    for j in url:
        if ord(j) in range(48,57):
            legalDomainDatabase["Digit Count"][i]+=1
    
    legalDomainDatabase["TLD Length"][i]=len(re.split("/",subdomains[-1])[0])
    legalDomainDatabase["URL Length"][i]=len(re.split("/",url)[0])


legalDomainDatabase.to_csv("Phishing Database 3.csv",index=False)