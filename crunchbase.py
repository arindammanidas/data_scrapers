import urllib
import urllib2
import csv
import json

f = open('EventsCBURLS.csv','r')
g = open('EVENTS_NEW_CB.csv','w+b')
cot = csv.writer(g)
line = f.readline()
count = 0
cot.writerows([['ID','Name','CompanyName','CompanyPermalink','CrunchbaseURL','HomepageURL','BlogURL','BlogFeedURL','TwitterUsername','CategoryCode','NoOfEmployees','FoundedYear','FoundedMonth','FoundedDay','DeadpooledYear','DeadpooledMonth','DeadpooledDay','DeadpooledURL','TagList','AliasList','Email','Phone','Description','CreatedAt','UpdatedAt','Product1Name','Product1Permalink','Product2Name','Product2Permalink','Product3Name','Product3Permalink','Product4Name','Product4Permalink','Relationship1Is_Past','Relationship1Title','Relationship1FirstName','Relationship1LastName','Relationship1Permalink','Relationship2Is_Past','Relationship2Title','Relationship2FirstName','Relationship2LastName','Relationship2Permalink','Relationship3Is_Past','Relationship3Title','Relationship3FirstName','Relationship3LastName','Relationship3Permalink','Relationship4Is_Past','Relationship4Title','Relationship4FirstName','Relationship4LastName','Relationship4Permalink','Competitor1Name','Competitor1Permalink','Competitor2Name','Competitor2Permalink','Competitor3Name','Competitor3Permalink','Competitor4Name','Competitor4Permalink','TotalMoneyRaised','Funding1RoundCode','Funding1RaisedAmount','Funding1RaisedCurrCode','Funding1Year','Funding1Month','Funding1Day','Funding1Investments1CompanyName','Funding1Investments1CompanyPermalink','Funding1Investments1FinanceOrgName','Funding1Investments1FinanceOrgPermalink','Funding1Investments1PersonFirstName','Funding1Investments1PersonLastName','Funding1Investments1PersonPermalink','Funding1Investments2CompanyName','Funding1Investments2CompanyPermalink','Funding1Investments2FinanceOrgName','Funding1Investments2FinanceOrgPermalink','Funding1Investments2PersonFirstName','Funding1Investments2PersonLastName','Funding1Investments2PersonPermalink','Funding1Investments3CompanyName','Funding1Investments3CompanyPermalink','Funding1Investments3FinanceOrgName','Funding1Investments3FinanceOrgPermalink','Funding1Investments3PersonFirstName','Funding1Investments3PersonLastName','Funding1Investments3PersonPermalink','Funding1Investments4CompanyName','Funding1Investments4CompanyPermalink','Funding1Investments4FinanceOrgName','Funding1Investments4FinanceOrgPermalink','Funding1Investments4PersonFirstName','Funding1Investments4PersonLastName','Funding1Investments4PersonPermalink','Funding2RoundCode','Funding2RaisedAmount','Funding2RaisedCurrCode','Funding2Year','Funding2Month','Funding2Day','Funding2Investments1CompanyName','Funding2Investments1CompanyPermalink','Funding2Investments1FinanceOrgName','Funding2Investments1FinanceOrgPermalink','Funding2Investments1PersonFirstName','Funding2Investments1PersonLastName','Funding2Investments1PersonPermalink','Funding2Investments2CompanyName','Funding2Investments2CompanyPermalink','Funding2Investments2FinanceOrgName','Funding2Investments2FinanceOrgPermalink','Funding2Investments2PersonFirstName','Funding2Investments2PersonLastName','Funding2Investments2PersonPermalink','Funding2Investments3CompanyName','Funding2Investments3CompanyPermalink','Funding2Investments3FinanceOrgName','Funding2Investments3FinanceOrgPermalink','Funding2Investments3PersonFirstName','Funding2Investments3PersonLastName','Funding2Investments3PersonPermalink','Funding2Investments4CompanyName','Funding2Investments4CompanyPermalink','Funding2Investments4FinanceOrgName','Funding2Investments4FinanceOrgPermalink','Funding2Investments4PersonFirstName','Funding2Investments4PersonLastName','Funding2Investments4PersonPermalink','Funding3RoundCode','Funding3RaisedAmount','Funding3RaisedCurrCode','Funding3Year','Funding3Month','Funding3Day','Funding3Investments1CompanyName','Funding3Investments1CompanyPermalink','Funding3Investments1FinanceOrgName','Funding3Investments1FinanceOrgPermalink','Funding3Investments1PersonFirstName','Funding3Investments1PersonLastName','Funding3Investments1PersonPermalink','Funding3Investments2CompanyName','Funding3Investments2CompanyPermalink','Funding3Investments2FinanceOrgName','Funding3Investments2FinanceOrgPermalink','Funding3Investments2PersonFirstName','Funding3Investments2PersonLastName','Funding3Investments2PersonPermalink','Funding3Investments3CompanyName','Funding3Investments3CompanyPermalink','Funding3Investments3FinanceOrgName','Funding3Investments3FinanceOrgPermalink','Funding3Investments3PersonFirstName','Funding3Investments3PersonLastName','Funding3Investments3PersonPermalink','Funding3Investments4CompanyName','Funding3Investments4CompanyPermalink','Funding3Investments4FinanceOrgName','Funding3Investments4FinanceOrgPermalink','Funding3Investments4PersonFirstName','Funding3Investments4PersonLastName','Funding3Investments4PersonPermalink','Funding4RoundCode','Funding4RaisedAmount','Funding4RaisedCurrCode','Funding4Year','Funding4Month','Funding4Day','Funding4Investments1CompanyName','Funding4Investments1CompanyPermalink','Funding4Investments1FinanceOrgName','Funding4Investments1FinanceOrgPermalink','Funding4Investments1PersonFirstName','Funding4Investments1PersonLastName','Funding4Investments1PersonPermalink','Funding4Investments2CompanyName','Funding4Investments2CompanyPermalink','Funding4Investments2FinanceOrgName','Funding4Investments2FinanceOrgPermalink','Funding4Investments2PersonFirstName','Funding4Investments2PersonLastName','Funding4Investments2PersonPermalink','Funding4Investments3CompanyName','Funding4Investments3CompanyPermalink','Funding4Investments3FinanceOrgName','Funding4Investments3FinanceOrgPermalink','Funding4Investments3PersonFirstName','Funding4Investments3PersonLastName','Funding4Investments3PersonPermalink','Funding4Investments4CompanyName','Funding4Investments4CompanyPermalink','Funding4Investments4FinanceOrgName','Funding4Investments4FinanceOrgPermalink','Funding4Investments4PersonFirstName','Funding4Investments4PersonLastName','Funding4Investments4PersonPermalink','Office1Description','Office1Address1','Office1Address2','Office1ZipCode','Office1City','Office1StateCode','Office1CountryCode','Office1Lat','Office1Long','Office2Description','Office2Address1','Office2Address2','Office2ZipCode','Office2City','Office2StateCode','Office2CountryCode','Office2Lat','Office2Long','Office3Description','Office3Address1','Office3Address2','Office3ZipCode','Office3City','Office3StateCode','Office3CountryCode','Office3Lat','Office3Long','Office4Description','Office4Address1','Office4Address2','Office4ZipCode','Office4City','Office4StateCode','Office4CountryCode','Office4Lat','Office4Long','Links1URL','Links1Title','Links2URL','Links2Title','Links3URL','Links3Title','Links4URL','Links4Title']])
while line:

    line=line.strip(' \r\n\t')
    linearray=line.split(',')
    uid=linearray[0]
    cname=linearray[1]
    url=linearray[2]
    urlarray=url.split('/')
        
    ckey=''

    urlnew='http://api.crunchbase.com/v/1/'+urlarray[3]+'/'+urlarray[4]+'.js?api_key='+ckey
    #print urlnew
    #urlnew='http://api.crunchbase.com/v/1/company/facebook.js?api_key='
    response = urllib2.urlopen(urlnew)
    json_data = json.load(response)

    row=[]

    row.append(str(uid))
    row.append(str(cname))
       
    try:
        row.append(str(json_data['name']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['permalink']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['crunchbase_url']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['homepage_url']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['blog_url']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['blog_feed_url']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['twitter_username']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['category_code']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['number_of_employees']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['founded_year']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['founded_month']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['founded_day']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['deadpooled_year']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['deadpooled_month']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['deadpooled_day']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['deadpooled_url']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['tag_list']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['alias_list']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['email_address']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['phone_number']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['description']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['created_at']))
    except:
        row.append(str('NA'))

    try:
        row.append(str(json_data['updated_at']))
    except:
        row.append(str('NA'))

    i=0
    for i in range(0, 4):
        try:
            row.append(str(json_data['products'][i]['name']))
        except:
            row.append(str('NA'))
            
        try:
            row.append(str(json_data['products'][i]['permalink']))
        except:
            row.append(str('NA'))

    i=0                    
    for i in range(0, 4):
        try:
            row.append(str(json_data['relationships'][i]['is_past']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['relationships'][i]['title']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['relationships'][i]['person']['first_name'].encode('utf-8')))
        except:
            row.append(str('NA'))

        try:            
            row.append(str(json_data['relationships'][i]['person']['last_name'].encode('utf-8')))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['relationships'][i]['person']['permalink'].encode('utf-8')))
        except:
            row.append(str('NA'))
    
    i=0
    for i in range(0, 4):
        try:
            row.append(str(json_data['competitions'][i]['competitor']['name']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['competitions'][i]['competitor']['permalink']))
        except:
            row.append(str('NA'))
            
    try:
        row.append(str(json_data['total_money_raised']))
    except:
        row.append(str('NA'))
    i=0
    for i in range(0, 4):
        try:
            row.append(str(json_data['funding_rounds'][i]['round_code']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['funding_rounds'][i]['raised_amount']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['funding_rounds'][i]['raised_currency_code']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['funding_rounds'][i]['funded_year']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['funding_rounds'][i]['funded_month']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['funding_rounds'][i]['funded_day']))
        except:
            row.append(str('NA'))

        j=0
        for j in range(0, 4):
            try:
                row.append(str(json_data['funding_rounds'][i]['investments'][j]['company']['name']))
            except:
                row.append(str('NA'))

            try:
                row.append(str(json_data['funding_rounds'][i]['investments'][j]['company']['permalink']))
            except:
                row.append(str('NA'))
           
            try:
                row.append(str(json_data['funding_rounds'][i]['investments'][j]['financial_org']['name']))
            except:
                row.append(str('NA'))

            try:
                row.append(str(json_data['funding_rounds'][i]['investments'][j]['financial_org']['permalink']))
            except:
                row.append(str('NA'))

            try:
                row.append(str(json_data['funding_rounds'][i]['investments'][j]['person']['first_name']))
            except:
                row.append(str('NA'))

            try:
                row.append(str(json_data['funding_rounds'][i]['investments'][j]['person']['last_name']))
            except:
                row.append(str('NA'))

            try:
                row.append(str(json_data['funding_rounds'][i]['investments'][j]['person']['permalink']))
            except:
                row.append(str('NA'))
                
    i=0
    for i in range(0, 4):
        try:
            row.append(str(json_data['offices'][i]['description']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['offices'][i]['address1']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['offices'][i]['address2']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['offices'][i]['zip_code']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['offices'][i]['city']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['offices'][i]['state_code']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['offices'][i]['country_code']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['offices'][i]['latitude']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['offices'][i]['longitude']))
        except:
            row.append(str('NA'))

    i=0       
    for i in range(0, 4):
        try:
            row.append(str(json_data['external_links'][i]['external_url']))
        except:
            row.append(str('NA'))

        try:
            row.append(str(json_data['external_links'][i]['title']))
        except:
            row.append(str('NA'))
            
    count+=1
   		                
    print (" ID: " +str(uid))
    print (" Name: " +str(cname))
    print ("------------------------------------------------")
    print ("    COUNT >> " +str(count))
    print ("------------------------------------------------")

    cot.writerow(row)
    line = f.readline()
    
f.close()
g.close()
