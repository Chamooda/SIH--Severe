import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import re
import requests
from bs4 import BeautifulSoup

def scrapper(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    length = len(r.content)
    anchors = len(soup.find_all('a'))

    return [length, anchors]


def scrap(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    frames = len(soup.findAll('frame'))
    iframes = len(soup.findAll('iframe'))
    tags = len(soup.findAll())

    return frames, iframes, tags

def urlBreaker(originalURL):
    parameters=[]
    try:
        temp = requests.get(originalURL)
        protocolRisk = 0
        if "https://" in originalURL or "http://" in originalURL or "tls://" in originalURL or "ftps://" in originalURL or "ssl://" in originalURL:
            protocolRisk = 1

        # THis is asad removing this code
        # elif "https://" not in originalURL and "ftps://" not in originalURL:
        #     protocolRisk = 0
        # else:
        #     protocolRisk = 0

        parameters.append(protocolRisk)

        # url = re.split("//", originalURL)[1]
        subdomains = re.split("\.", originalURL)

        subdomainCount = len(subdomains)
        parameters.append(subdomainCount)

        parameters.append(len(re.split("/", subdomains[-1])[0]))
        parameters.append(len(re.split("/", originalURL)[0]))

        specialCharacters = {'?':4, '-':5, '%':6, '=':7, '@':8, '!':9, '^':10, '&':11, '#':12}
        for character in specialCharacters:
            parameters.append(0)
            for j in originalURL:
                if j in specialCharacters:
                    parameters[specialCharacters[character]] += 1

        parameters.append(0)
        for j in originalURL:
            if ord(j) in range(48, 57):
                parameters[13] += 1

        length, anchors = scrapper(originalURL)
        parameters.append(length)
        parameters.append(anchors)

        frames, iframes, tags = scrap(originalURL)
        parameters.append(frames)
        parameters.append(iframes)
        parameters.append(tags)
    except:
        pass
    return parameters

df=pd.read_csv("Updated Dataset.csv")
rfc=RandomForestClassifier(n_estimators=500)

X_train, X_test, Y_train, Y_test=train_test_split(df.drop(["Phishing"],axis=1),df["Phishing"],test_size=0.50, random_state=101)
rfc.fit(X_train,Y_train)
#predictions=rfc.predict(X_test)
#print(classification_report(Y_test,predictions))

columns = ["Protocol Risk",
           "SubDomain Count",
           "TLD Length",
           "URL Length",
           '?', '-', '%', '=', '@', '!', '^', '&', '#',
           "Digit Count",
           "Content Length",
           "Redirects",
           "Frames",
           "IFrames",
           "Tags"]

url=input("Enter the URL: ")        #SEND THE URL HERE!!!!
urlList=urlBreaker(url)
urlDict={}
if len(urlBreaker(url))==0:
    parameterDf="Invalid URL"
else:
    k=0
    for i in columns:
        urlDict[i]=urlList[k]
        k+=1
    parameterDf=rfc.predict(np.array([urlList]))

if parameterDf==0:
    print("The given website is legal")
else:
    print("The given website is a phishing website")