import urllib
import urllib2
import csv
from bs4 import BeautifulSoup

f = open('PGALurls.csv','r')
g = open('angeldatanew2.csv','a+b')
cot = csv.writer(g)
line = f.readline()
count = 0
cot.writerows([['ID','Name','URL','Location','Market','Website','WebTitle','WebDescription','Founders','FounderURL','Team','TeamURL','Advisors','AdvisorURL','Investors','InvestorURL','Board','BoardURL','Incubators','IncubatorURL','Funding1','Funding2','Funding3','Funding4']])
while line:

    line=line.strip(' \r\n\t')
    linearray=line.split(',')
    uid=linearray[0]
    cname=linearray[1]
    url=linearray[2]
    #url='https://angel.co/stepout'

    response = urllib2.urlopen(url)
    page = response.read()
    soup=BeautifulSoup(page)

    try:
        location=soup.find('div', attrs={'class' : 'info g-profile_lockup'}).findAll('a', attrs={'class' : 'location-tag'})
        locationall=""
        for i in location:
            locationall+=i.contents[0]+","
        locationall=locationall.rstrip(',')
    except:
        locationall='NA'

    try:
        market=soup.find('div', attrs={'class' : 'info g-profile_lockup'}).findAll('a', attrs={'class' : 'market-tag'})
        marketall=""
        for i in market:
            marketall+=i.contents[0]+","
        marketall=marketall.rstrip(',')
    except:
        marketall='NA'

    try:
        website=soup.find('a', attrs={'class' : 'website-link'})['href']
        response1 = urllib2.urlopen(website)
        page1 = response1.read()
        soup1=BeautifulSoup(page1)
        title=soup1.find('title').string.encode('utf-8').strip(' \r\n\t')
    except:
        website='NA'
        title='NA'
      
    try:
        description=soup1.find('head').find('meta', attrs={'name' : 'description'}).contents[0].strip(' \r\n\t')
    except:
        description='NA'
            
    try:
        founders=soup.find('div', attrs={'id' : 'founders_section'}).findAll('a', attrs={'class' : 'profile-link'})
        foundersall=""
        foundersurlall=""
        for i in founders:
            foundersall+=i.contents[0]+","
            foundersurlall+=i['href']+","
        foundersall=foundersall.rstrip(',').encode('utf-8')
        foundersurlall=foundersurlall.rstrip(',')
    except:
        foundersall='NA'
        foundersurlall='NA'

    try:
        team=soup.find('div', attrs={'id' : 'employees_section'}).findAll('a', attrs={'class' : 'profile-link'})
        teamall=""
        teamurlall=""
        for i in team:
            teamall+=i.contents[0]+","
            teamurlall+=i['href']+","
        teamall=teamall.rstrip(',').encode('utf-8')
        teamurlall=teamurlall.rstrip(',')
    except:
        teamall='NA'
        teamurlall='NA'

    try:
        advisors=soup.find('div', attrs={'id' : 'advisors_section'}).findAll('a', attrs={'class' : 'profile-link'})
        advisorsall=""
        advisorsurlall=""
        for i in advisors:
            advisorsall+=i.contents[0]+","
            advisorsurlall+=i['href']+","
        advisorsall=advisorsall.rstrip(',')
        advisorsurlall=advisorsurlall.rstrip(',')
    except:
        advisorsall='NA'
        advisorsurlall='NA'

    try:
        investors1=soup.find('div', attrs={'id' : 'past_investors_section'}).findAll('a', attrs={'class' : 'profile-link'})
        investors2=soup.find('div', attrs={'id' : 'past_investors_section'}).findAll('a', attrs={'class' : 'startup-link'})
        investorsall=""
        investorsurlall=""
        for i in investors1:
            investorsall+=i.contents[0]+","
            investorsurlall+=i['href']+","
        for i in investors2:
            investorsall+=i.contents[0]+","
            investorsurlall+=i['href']+","
        investorsall=investorsall.rstrip(',')
        investorsurlall=investorsurlall.rstrip(',')
    except:
        investorsall='NA'
        investorsurlall='NA'

    try:
        board=soup.find('div', attrs={'id' : 'board_members_section'}).findAll('a', attrs={'class' : 'profile-link'})
        boardall=""
        boardurlall=""
        for i in board:
            boardall+=i.contents[0]+","
            boardurlall+=i['href']+","
        boardall=boardall.rstrip(',')
        boardurlall=boardurlall.rstrip(',')
    except:
        boardall='NA'
        boardurlall='NA'

    try:
        incubators=soup.find('div', attrs={'id' : 'incubators_section'}).findAll('a', attrs={'class' : 'startup-link'})
        incubatorsall=""
        incubatorsurlall=""
        for i in incubators:
            incubatorsall+=i.contents[0]+","
            incubatorsurlall+=i['href']+","
        incubatorsall=incubatorsall.rstrip(',')
        incubatorsurlall=incubatorsurlall.rstrip(',')
    except:
        incubatorsall='NA'
        incubatorsurlall='NA'

    try:
        funding1=soup.find('div', attrs={'id' : 'funding_section'}).findAll('div', attrs={'class' : 'display half round'})
        funding2=soup.find('div', attrs={'id' : 'funding_section'}).findAll('div', attrs={'class' : 'display round'})
        fundingall=""
        for i in funding1:
            try:
                date=i.find('div', attrs={'class' : 'date_display'}).contents[0].replace(",","")
                ftype=i.find('div', attrs={'class' : 'type'}).contents[0]
                raised=i.find('div', attrs={'class' : 'raised'}).find('a').contents[0].replace(",","")
            except:
                date=i.find('div', attrs={'class' : 'date_display'}).contents[0].replace(",","")
                ftype=i.find('div', attrs={'class' : 'type'}).contents[0]
                raised=i.find('div', attrs={'class' : 'raised'}).contents[0].replace(",","")
            try:
                participants=i.find('div', attrs={'class' : 'participant_list'}).findAll('a')
                participantsall=""
                for j in participants:
                    participantsall+=j.contents[0]+":"
                participantsall=participantsall.rstrip(':')
            except:
                participantsall="NA"
            fundingall+=date+","+ftype+","+raised+","+participantsall+";"
        for i in funding2:
            try:
                date=i.find('div', attrs={'class' : 'date_display'}).contents[0].replace(",","")
                ftype=i.find('div', attrs={'class' : 'type'}).contents[0]
                raised=i.find('div', attrs={'class' : 'raised'}).find('a').contents[0].replace(",","")
            except:
                date=i.find('div', attrs={'class' : 'date_display'}).contents[0].replace(",","")
                ftype=i.find('div', attrs={'class' : 'type'}).contents[0]
                raised=i.find('div', attrs={'class' : 'raised'}).contents[0].replace(",","")
            try:
                participants=i.find('div', attrs={'class' : 'participant_list'}).findAll('a')
                participantsall=""
                for j in participants:
                    participantsall+=j.contents[0]+":"
                participantsall=participantsall.rstrip(':')
            except:
                participantsall="NA"
            fundingall+=date+","+ftype+","+raised+","+participantsall+";"
        fundingall=fundingall.rstrip(';')
    except:
        fundingall='NA'

    fundingarray=fundingall.split(';')
    
    if len(fundingarray)==1:
        fundingone=fundingarray[0]
        fundingtwo="NA"
        fundingthree="NA"
        fundingfour="NA"
    elif len(fundingarray)==2:
        fundingone=fundingarray[0]
        fundingtwo=fundingarray[1]
        fundingthree="NA"
        fundingfour="NA"
    elif len(fundingarray)==3:
        fundingone=fundingarray[0]
        fundingtwo=fundingarray[1]
        fundingthree=fundingarray[2]
        fundingfour="NA"
    elif len(fundingarray)==4:
        fundingone=fundingarray[0]
        fundingtwo=fundingarray[1]
        fundingthree=fundingarray[2]
        fundingfour=fundingarray[3]
    else:
        fundingone="NA"
        fundingtwo="NA"
        fundingthree="NA"
        fundingfour="NA"
    
    count+=1
   		                
    print (" ID: " +str(uid))
    print (" Company: " +str(cname))
    print (" URL: " +str(url))
    print (" Location: " +str(locationall))
    print (" Market: " +str(marketall))
    print (" Website: " +str(website))
    print (" Web Title: " +str(title))
    print (" Web Description: " +str(description))
    print (" Founders: " +str(foundersall))
    print (" Founders URL: " +str(foundersurlall))
    print (" Team: " +str(teamall))
    print (" Team URL: " +str(teamurlall))
    print (" Advisors: " +str(advisorsall))
    print (" Advisors URL: " +str(advisorsurlall))
    print (" Investors: " +str(investorsall))
    print (" Investors URL: " +str(investorsurlall))
    print (" Board Members: " +str(boardall))
    print (" Board Members URL: " +str(boardurlall))
    print (" Incubators: " +str(incubatorsall))
    print (" Incubators URL: " +str(incubatorsurlall))
    print (" Funding1: " +str(fundingone))
    print (" Funding2: " +str(fundingtwo))
    print (" Funding3: " +str(fundingthree))
    print (" Funding4: " +str(fundingfour))
    print ("------------------------------------------------")
    print ("    COUNT >> " +str(count))
    print ("------------------------------------------------")

    cot.writerows([[uid,cname,url,locationall,marketall,website,title,description,foundersall,foundersurlall,teamall,teamurlall,advisorsall,advisorsurlall,investorsall,investorsurlall,boardall,boardurlall,incubatorsall,incubatorsurlall,fundingone,fundingtwo,fundingthree,fundingfour]])
    line = f.readline()
f.close()
g.close()
