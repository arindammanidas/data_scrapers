import oauth2 as oauth
import httplib2
import time, os, simplejson
import urllib
import urllib2
import csv
import json

consumer_key     =   ''
consumer_secret  =   ''
user_token       =   ''
user_secret      =   ''

consumer = oauth.Consumer(consumer_key, consumer_secret)

access_token = oauth.Token(
			key=user_token,
			secret=user_secret)

client = oauth.Client(consumer, access_token)

f = open('linkedin1.csv','r')
g = open('LINKEDIN-FOUNDERS-1.csv','a+b')
cot = csv.writer(g)
line = f.readline()
count = 0
cot.writerows([['ID','CompanyName','FirstName','LastName','Headline','Industry','Location','Country','PositionsTotal','Position1Title','Position1IsCurrent','Position1CompanyName','Position1CompanyIndustry','Position1CompanyType','Position1StartMonth','Position1StartYear','Position1EndMonth','Position1EndYear','Position2Title','Position2IsCurrent','Position2CompanyName','Position2CompanyIndustry','Position2CompanyType','Position2StartMonth','Position2StartYear','Position2EndMonth','Position2EndYear','Position3Title','Position3IsCurrent','Position3CompanyName','Position3CompanyIndustry','Position3CompanyType','Position3StartMonth','Position3StartYear','Position3EndMonth','Position3EndYear','Position4Title','Position4IsCurrent','Position4CompanyName','Position4CompanyIndustry','Position4CompanyType','Position4StartMonth','Position4StartYear','Position4EndMonth','Position4EndYear','Position5Title','Position5IsCurrent','Position5CompanyName','Position5CompanyIndustry','Position5CompanyType','Position5StartMonth','Position5StartYear','Position5EndMonth','Position5EndYear','Position6Title','Position6IsCurrent','Position6CompanyName','Position6CompanyIndustry','Position6CompanyType','Position6StartMonth','Position6StartYear','Position6EndMonth','Position6EndYear','PublicURL']])
while line:
    line=line.strip(' \r\n\t')
    linearray=line.split(',')
    uid=linearray[0]
    cname=linearray[1]
    url=linearray[2]
    urlarray=url.split('/')
    resp,content = client.request("http://api.linkedin.com/v1/people/url="+str(urllib.quote_plus(url))+":(first-name,last-name,headline,industry,location,positions,public-profile-url)?format=json", "GET", "")
    #print content
    json_data = json.loads(content)

    row=[]

    row.append(str(uid))
    row.append(str(cname))
       
    try:
        row.append(str(json_data['firstName']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['lastName']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['headline']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['industry']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['location']['name']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['location']['country']['code']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['positions']['_total']))
    except:
        row.append(str('NA'))
  
    i=0
    for i in range(0, 6):
        try:
            row.append(str(json_data['positions']['values'][i]['title']))
        except:
            row.append(str('NA'))
            
        try:
            row.append(str(json_data['positions']['values'][i]['isCurrent']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['positions']['values'][i]['company']['name']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['positions']['values'][i]['company']['industry']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['positions']['values'][i]['company']['type']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['positions']['values'][i]['startDate']['month']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['positions']['values'][i]['startDate']['year']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['positions']['values'][i]['endDate']['month']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['positions']['values'][i]['endDate']['year']))
        except:
            row.append(str('NA'))

    try:
        row.append(str(json_data['publicProfileUrl']))
    except:
        row.append(str('NA'))
   
    count+=1
   		                
    print (" ID: " +str(uid))
    print (" Name: " +str(cname))
    print (" URL: " +str(url))
    print ("------------------------------------------------")
    print ("    COUNT >> " +str(count))
    print ("------------------------------------------------")

    cot.writerow(row)
    line = f.readline()
    
f.close()
g.close()


