import urllib
import urllib2
import csv
from bs4 import BeautifulSoup

f = open('PGALurls.csv','r')
g = open('ecell_leaderboard.txt','w')
cot = csv.writer(g)
line = f.readline()
cot.writerows([['College','TeamLeader','Email','Phone']])

url='http://ecell.in/nec/leaderboard/'
response = urllib2.urlopen(url)
page = response.read()
soup=BeautifulSoup(page)
location=soup.find('table', attrs={'id' : 'leader'}).findAll('td')
for i in location:
    g.write(i.get_text())
    
cot.writerows([[uid,cname,url,locationall,marketall,website,title,description,foundersall,foundersurlall,teamall,teamurlall,advisorsall,advisorsurlall,investorsall,investorsurlall,boardall,boardurlall,incubatorsall,incubatorsurlall,fundingone,fundingtwo,fundingthree,fundingfour]])
g.close()
