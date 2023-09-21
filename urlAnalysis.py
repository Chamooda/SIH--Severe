import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import whois

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


legalDomainDatabase=pd.read_csv("verified_online.csv")
for i in legalDomainDatabase.index:
    print(i)
    url=str(legalDomainDatabase["Domain"][i])
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

legalDomainDatabase.to_csv("Phishing Database 2.csv",index=False)