import urllib
import urllib2
import csv
from bs4 import BeautifulSoup

f = open('links1.txt','r')
g = open('alexa_page2_1.csv','a+b')
cot = csv.writer(g)
line = f.readline()
count = 0
cot.writerows([['ID','URL','GlobalRank','IndiaRank','SitesLinkingIn','LoadType','LoadTime','SlowerThan']])
while line:

    line=line.strip(' \r\n\t')
    url = "http://www.alexa.com/siteinfo/"+line

    response = urllib2.urlopen(url)

    page = response.read()
  
    soup=BeautifulSoup(page)

    try:
        grank=soup.find('section', attrs={'id' : 'traffic-rank-content'}).findNext('span', attrs={'class' : 'globleRank'}).findNext('strong', attrs={'class' : 'metricsUrl font-big2 valign'}).findNext('a')
        grank=grank.contents[0]
    except:
        grank='NA'

    try:
        irank=soup.find('section', attrs={'id' : 'traffic-rank-content'}).findNext('span', attrs={'class' : 'countryRank'}).findNext('strong', attrs={'class' : 'metricsUrl font-big2 valign'}).findNext('a')
        irank=irank.contents[0]
    except:
        irank='NA'
        
    try:
        name=soup.find('section', attrs={'id' : 'section-linksinv2'}).findNext('span', attrs={'class' : 'font-5 float-right'})
        name=name.contents[0]
    except:
        name='NA'

    try:        
        load=soup.find('section', attrs={'id' : 'section-load'}).findNext('section', attrs={'class' : 'panel-content'}).findNext('p')
        loadtype=load.find('span')
        loadtype=loadtype.contents[0]
    except:
        loadtype='NA'

    try:
        loadtime=load.contents[1]
        loadtimearray=loadtime.split(' ')
        loadtimearray1=loadtimearray[1][1:]
        loadtimearray2=loadtimearray[3]
    except:
        loadtimearray1='NA'
        loadtimearray2='NA'
        
    if line=='blank':
        grank='NA'
        irank='NA'
        name='NA'
        loadtype='NA'
    
    if loadtype=='NA':
	loadtimearray1='NA'
	loadtimearray2='NA'
    
    count+=1
    uid='PG'+str(count)
		                
    print (" ID: " +str(uid))
    print (" URL: " +str(line))
    print (" Global Rank: " +str(grank))
    print (" India Rank: " +str(irank))
    print (" Total sites linking in: " +str(name))
    print (" Page Load Category: " +str(loadtype))
    print (" Page Load Time: " +str(loadtimearray1) + " seconds")
    print (" Page Load Slower Than: " +str(loadtimearray2))
    print ("------------------------------------------------")

    cot.writerows([[uid,line,grank,irank,name,loadtype,loadtimearray1,loadtimearray2]])
    line = f.readline()
f.close()
g.close()
