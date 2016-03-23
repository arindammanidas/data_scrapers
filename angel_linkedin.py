import urllib
import urllib2
import csv
from bs4 import BeautifulSoup

f = open('URL_AL2.csv','r')
g = open('AngelPeopleData_New2.csv','a+b')
cot = csv.writer(g)
line = f.readline()
count = 292
cot.writerows([['ID','Name','URL','F1URL','F2URL','F3URL','F4URL','F1Facebook','F1Twitter','F1LinkedIn','F2Facebook','F2Twitter','F2LinkedIn','F3Facebook','F3Twitter','F3LinkedIn','F4Facebook','F4Twitter','F4LinkedIn','T1URL','T2URL','T3URL','T4URL','T1Facebook','T1Twitter','T1LinkedIn','T2Facebook','T2Twitter','T2LinkedIn','T3Facebook','T3Twitter','T3LinkedIn','T4Facebook','T4Twitter','T4LinkedIn','A1URL','A2URL','A3URL','A4URL','A1Facebook','A1Twitter','A1LinkedIn','A2Facebook','A2Twitter','A2LinkedIn','A3Facebook','A3Twitter','A3LinkedIn','A4Facebook','A4Twitter','A4LinkedIn','I1URL','I2URL','I3URL','I4URL','I5URL','I1Facebook','I1Twitter','I1LinkedIn','I2Facebook','I2Twitter','I2LinkedIn','I3Facebook','I3Twitter','I3LinkedIn','I4Facebook','I4Twitter','I4LinkedIn','I5Facebook','I5Twitter','I5LinkedIn','B1URL','B2URL','B3URL','B4URL','B1Facebook','B1Twitter','B1LinkedIn','B2Facebook','B2Twitter','B2LinkedIn','B3Facebook','B3Twitter','B3LinkedIn','B4Facebook','B4Twitter','B4LinkedIn']])
while line:

    f1url='NA'
    f1facebook='NA'
    f1twitter='NA'
    f1linkedin='NA'
    f2url='NA'
    f2facebook='NA'
    f2twitter='NA'
    f2linkedin='NA'
    f3url='NA'
    f3facebook='NA'
    f3twitter='NA'
    f3linkedin='NA'
    f4url='NA'
    f4facebook='NA'
    f4twitter='NA'
    f4linkedin='NA'

    t1url='NA'
    t1facebook='NA'
    t1twitter='NA'
    t1linkedin='NA'
    t2url='NA'
    t2facebook='NA'
    t2twitter='NA'
    t2linkedin='NA'
    t3url='NA'
    t3facebook='NA'
    t3twitter='NA'
    t3linkedin='NA'
    t4url='NA'
    t4facebook='NA'
    t4twitter='NA'
    t4linkedin='NA'
    
    a1url='NA'
    a1facebook='NA'
    a1twitter='NA'
    a1linkedin='NA'
    a2url='NA'
    a2facebook='NA'
    a2twitter='NA'
    a2linkedin='NA'
    a3url='NA'
    a3facebook='NA'
    a3twitter='NA'
    a3linkedin='NA'
    a4url='NA'
    a4facebook='NA'
    a4twitter='NA'
    a4linkedin='NA'

    i1url='NA'
    i1facebook='NA'
    i1twitter='NA'
    i1linkedin='NA'
    i2url='NA'
    i2facebook='NA'
    i2twitter='NA'
    i2linkedin='NA'
    i3url='NA'
    i3facebook='NA'
    i3twitter='NA'
    i3linkedin='NA'
    i4url='NA'
    i4facebook='NA'
    i4twitter='NA'
    i4linkedin='NA'
    i5url='NA'
    i5facebook='NA'
    i5twitter='NA'
    i5linkedin='NA'

    b1url='NA'
    b1facebook='NA'
    b1twitter='NA'
    b1linkedin='NA'
    b2url='NA'
    b2facebook='NA'
    b2twitter='NA'
    b2linkedin='NA'
    b3url='NA'
    b3facebook='NA'
    b3twitter='NA'
    b3linkedin='NA'
    b4url='NA'
    b4facebook='NA'
    b4twitter='NA'
    b4linkedin='NA'

    line=line.strip(' \r\n\t')
    linearray=line.split(',')
    uid=linearray[0]
    cname=linearray[1]
    url=linearray[2]
    f1url=linearray[3]
    f2url=linearray[4]
    f3url=linearray[5]
    f4url=linearray[6]
    t1url=linearray[7]
    t2url=linearray[8]
    t3url=linearray[9]
    t4url=linearray[10]
    a1url=linearray[11]
    a2url=linearray[12]
    a3url=linearray[13]
    a4url=linearray[14]
    i1url=linearray[15]
    i2url=linearray[16]
    i3url=linearray[17]
    i4url=linearray[18]
    i5url=linearray[19]
    b1url=linearray[20]
    b2url=linearray[21]
    b3url=linearray[22]
    #b4url=linearray[23]

    if f1url=='' or f1url==' ':
        f1url='NA'
    if f2url=='' or f2url==' ':
        f2url='NA'
    if f3url=='' or f3url==' ':
        f3url='NA'
    if f4url=='' or f4url==' ':
        f4url='NA'
    if t1url=='' or t1url==' ':
        t1url='NA'
    if t2url=='' or t2url==' ':
        t2url='NA'
    if t3url=='' or t3url==' ':
        t3url='NA'
    if t4url=='' or t4url==' ':
        t4url='NA'
    if a1url=='' or a1url==' ':
        a1url='NA'
    if a2url=='' or a2url==' ':
        a2url='NA'
    if a3url=='' or a3url==' ':
        a3url='NA'
    if a4url=='' or a4url==' ':
        a4url='NA'
    if i1url=='' or i1url==' ':
        i1url='NA'
    if i2url=='' or i2url==' ':
        i2url='NA'
    if i3url=='' or i3url==' ':
        i3url='NA'
    if i4url=='' or i4url==' ':
        i4url='NA'
    if i5url=='' or i5url==' ':
        i5url='NA'
    if b1url=='' or b1url==' ':
        b1url='NA'
    if b2url=='' or b2url==' ':
        b2url='NA'
    if b3url=='' or b3url==' ':
        b3url='NA'
    if b4url=='' or b4url==' ':
        b4url='NA'
         
#Founders

#F1    
    if f1url!='NA':
        try:
            response = urllib2.urlopen(f1url)
            page = response.read()
            soup=BeautifulSoup(page)
        except ValueError:
            f1facebook='NA'
            f1twitter='NA'
            f1linkedin='NA'

        try:
            f1facebook=soup.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            f1facebook='NA'

        try:
            f1twitter=soup.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            f1twitter='NA'

        try:
            f1linkedin=soup.find('a', attrs={'class' : 'linked_in-link'})['href']
            f1linkedin=f1linkedin.encode('utf-8') 
        except:
            f1linkedin='NA'

#F2
    if f2url!='NA':
        try:
            response = urllib2.urlopen(f2url)
            page = response.read()
            soup1=BeautifulSoup(page)
        except ValueError:
            f2facebook='NA'
            f2twitter='NA'
            f2linkedin='NA'

        try:
            f2facebook=soup1.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            f2facebook='NA'

        try:
            f2twitter=soup1.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            f2twitter='NA'

        try:
            f2linkedin=soup1.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            f2linkedin='NA'

#F3
    if f3url!='NA':
        try:
            response = urllib2.urlopen(f3url)
            page = response.read()
            soup2=BeautifulSoup(page)
        except ValueError:
            f3facebook='NA'
            f3twitter='NA'
            f3linkedin='NA'

        try:
            f3facebook=soup2.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            f3facebook='NA'

        try:
            f3twitter=soup2.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            f3twitter='NA'

        try:
            f3linkedin=soup2.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            f3linkedin='NA'

#F4
    if f4url!='NA':
        try:
            response = urllib2.urlopen(f4url)
            page = response.read()
            soup3=BeautifulSoup(page)
        except ValueError:
            f4facebook='NA'
            f4twitter='NA'
            f4linkedin='NA'

        try:
            f4facebook=soup3.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            f4facebook='NA'

        try:
            f4twitter=soup3.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            f4twitter='NA'

        try:
            f4linkedin=soup3.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            f4linkedin='NA'

#Team

#T1
    if t1url!='NA':
        try:
        
            response = urllib2.urlopen(t1url)
            page = response.read()
            soup4=BeautifulSoup(page)
        except ValueError:
            t1facebook='NA'
            t1twitter='NA'
            t1linkedin='NA'

        try:
            t1facebook=soup4.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            t1facebook='NA'

        try:
            t1twitter=soup4.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            t1twitter='NA'

        try:
            t1linkedin=soup4.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            t1linkedin='NA'

#T2
    if t2url!='NA':
        try:
            response = urllib2.urlopen(t2url)
            page = response.read()
            soup5=BeautifulSoup(page)
        except ValueError:
            t2facebook='NA'
            t2twitter='NA'
            t2linkedin='NA'

        try:
            t2facebook=soup5.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            t2facebook='NA'

        try:
            t2twitter=soup5.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            t2twitter='NA'

        try:
            t2linkedin=soup5.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            t2linkedin='NA'

#T3
    if t3url!='NA':
        try:
            response = urllib2.urlopen(t3url)
            page = response.read()
            soup6=BeautifulSoup(page)
        except ValueError:
            t3facebook='NA'
            t3twitter='NA'
            t3linkedin='NA'

        try:
            t3facebook=soup6.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            t3facebook='NA'

        try:
            t3twitter=soup6.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            t3twitter='NA'

        try:
            t3linkedin=soup6.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            t3linkedin='NA'

#T4
    if t4url!='NA':
        try:
            response = urllib2.urlopen(t4url)
            page = response.read()
            soup7=BeautifulSoup(page)
        except ValueError:
            t4facebook='NA'
            t4twitter='NA'
            t4linkedin='NA'

        try:
            t4facebook=soup7.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            t4facebook='NA'

        try:
            t4twitter=soup7.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            t4twitter='NA'

        try:
            t4linkedin=soup7.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            t4linkedin='NA'

    
#Advisors

#A1
    if a1url!='NA':
        try:
            response = urllib2.urlopen(a1url)
            page = response.read()
            soup8=BeautifulSoup(page)
        except ValueError:
            a1facebook='NA'
            a1twitter='NA'
            a1linkedin='NA'

        try:
            a1facebook=soup8.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            a1facebook='NA'

        try:
            a1twitter=soup8.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            a1twitter='NA'

        try:
            a1linkedin=soup8.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            a1linkedin='NA'
    
#A2
    if a2url!='NA':
        try:
            response = urllib2.urlopen(a2url)
            page = response.read()
            soup9=BeautifulSoup(page)
        except ValueError:
            a2facebook='NA'
            a2twitter='NA'
            a2linkedin='NA'

        try:
            a2facebook=soup9.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            a2facebook='NA'

        try:
            a2twitter=soup9.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            a2twitter='NA'

        try:
            a2linkedin=soup9.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            a2linkedin='NA'

#A3
    if a3url!='NA':
        try:
            response = urllib2.urlopen(a3url)
            page = response.read()
            soup10=BeautifulSoup(page)
        except ValueError:
            a3facebook='NA'
            a3twitter='NA'
            a3linkedin='NA'

        try:
            a3facebook=soup10.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            a3facebook='NA'

        try:
            a3twitter=soup10.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            a3twitter='NA'

        try:
            a3linkedin=soup10.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            a3linkedin='NA'

#A4
    if a4url!='NA':
        try:
            response = urllib2.urlopen(a4url)
            page = response.read()
            soup11=BeautifulSoup(page)
        except ValueError:
            a4facebook='NA'
            a4twitter='NA'
            a4linkedin='NA'

        try:
            a4facebook=soup11.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            a4facebook='NA'

        try:
            a4twitter=soup11.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            a4twitter='NA'

        try:
            a4linkedin=soup11.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            a4linkedin='NA'

#Investors

#I1
    if i1url!='NA':
        try:
            response = urllib2.urlopen(i1url)
            page = response.read()
            soup12=BeautifulSoup(page)
        except ValueError:
            i1facebook='NA'
            i1twitter='NA'
            i1linkedin='NA'

        try:
            ifacebook=soup12.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            i1facebook='NA'

        try:
            i1twitter=soup12.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            i1twitter='NA'

        try:
            i1linkedin=soup12.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            i1linkedin='NA'

#I2
    if i2url!='NA':
        try:
            response = urllib2.urlopen(i2url)
            page = response.read()
            soup13=BeautifulSoup(page)
        except ValueError:
            i2facebook='NA'
            i2twitter='NA'
            i2linkedin='NA'

        try:
            i2facebook=soup13.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            i2facebook='NA'

        try:
            i2twitter=soup13.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            i2twitter='NA'

        try:
            i2linkedin=soup13.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            i2linkedin='NA'

#I3
    if i3url!='NA':
        try:
            response = urllib2.urlopen(i3url)
            page = response.read()
            soup14=BeautifulSoup(page)
        except ValueError:
            i3facebook='NA'
            i3twitter='NA'
            i3linkedin='NA'

        try:
            i3facebook=soup14.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            i3facebook='NA'

        try:
            i3twitter=soup14.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            i3twitter='NA'

        try:
            i3linkedin=soup14.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            i3linkedin='NA'

#I4
    if i4url!='NA':
        try:
            response = urllib2.urlopen(i4url)
            page = response.read()
            soup15=BeautifulSoup(page)
        except ValueError:
            i4facebook='NA'
            i4twitter='NA'
            i4linkedin='NA'

        try:
            i4facebook=soup15.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            i4facebook='NA'

        try:
            i4twitter=soup15.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            i4twitter='NA'

        try:
            i4linkedin=soup15.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            i4linkedin='NA'

#I5
    if i5url!='NA':
        try:
            response = urllib2.urlopen(i5url)
            page = response.read()
            soup16=BeautifulSoup(page)
        except ValueError:
            i5facebook='NA'
            i5twitter='NA'
            i5linkedin='NA'

        try:
            i5facebook=soup16.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            i5facebook='NA'

        try:
            i5twitter=soup16.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            i5twitter='NA'

        try:
            i5linkedin=soup16.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            i5linkedin='NA'


#Board

#B1
    if b1url!='NA':
        try:
            response = urllib2.urlopen(b1url)
            page = response.read()
            soup17=BeautifulSoup(page)
        except ValueError:
            b1facebook='NA'
            b1twitter='NA'
            b1linkedin='NA'

        try:
            b1facebook=soup17.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            b1facebook='NA'

        try:
            b1twitter=soup17.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            b1twitter='NA'

        try:
            b1linkedin=soup17.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            b1linkedin='NA'

#B2
    if b2url!='NA':
        try:
            response = urllib2.urlopen(b2url)
            page = response.read()
            soup18=BeautifulSoup(page)
        except ValueError:
            b2facebook='NA'
            b2twitter='NA'
            b2linkedin='NA'

        try:
            b2facebook=soup18.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            b2facebook='NA'

        try:
            b2twitter=soup18.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            b2twitter='NA'

        try:
           b2linkedin=soup18.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            b2linkedin='NA'

#B3
    if b3url!='NA':
        try:
            response = urllib2.urlopen(b3url)
            page = response.read()
            soup19=BeautifulSoup(page)
        except ValueError:
            b3facebook='NA'
            b3twitter='NA'
            b3linkedin='NA'

        try:
            b3facebook=soup19.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            b3facebook='NA'

        try:
            b3twitter=soup19.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            b3twitter='NA'

        try:
            b3linkedin=soup19.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            b3linkedin='NA'

#B4
    if b4url!='NA':
        try:
            response = urllib2.urlopen(b4url)
            page = response.read()
            soup20=BeautifulSoup(page)
        except ValueError:
            b4facebook='NA'
            b4twitter='NA'
            b4linkedin='NA'

        try:
            b4facebook=soup20.find('a', attrs={'class' : 'facebook-link'})['href']       
        except:
            b4facebook='NA'

        try:
            b4twitter=soup20.find('a', attrs={'class' : 'twitter-link'})['href']       
        except:
            b4twitter='NA'

        try:
            b4linkedin=soup20.find('a', attrs={'class' : 'linked_in-link'})['href']       
        except:
            b4linkedin='NA'

    count+=1
   		                
    print (" ID: " +str(uid))
    print (" Company: " +str(cname))
    print (" URL: " +str(url))
    
    print (" F1-URL: " +str(f1url))
    print (" F1-Facebook: " +str(f1facebook))
    print (" F1-Twitter: " +str(f1twitter))
    print (" F1-LinkedIn: " +str(f1linkedin))
    print (" F2-URL: " +str(f2url))
    print (" F2-Facebook: " +str(f2facebook))
    print (" F2-Twitter: " +str(f2twitter))
    print (" F2-LinkedIn: " +str(f2linkedin))
    print (" F3-URL: " +str(f3url))
    print (" F3-Facebook: " +str(f3facebook))
    print (" F3-Twitter: " +str(f3twitter))
    print (" F3-LinkedIn: " +str(f3linkedin))
    print (" F4-URL: " +str(f4url))
    print (" F4-Facebook: " +str(f4facebook))
    print (" F4-Twitter: " +str(f4twitter))
    print (" F4-LinkedIn: " +str(f4linkedin))

    print (" T1-URL: " +str(t1url))
    print (" T1-Facebook: " +str(t1facebook))
    print (" T1-Twitter: " +str(t1twitter))
    print (" T1-LinkedIn: " +str(t1linkedin))
    print (" T2-URL: " +str(t2url))
    print (" T2-Facebook: " +str(t2facebook))
    print (" T2-Twitter: " +str(t2twitter))
    print (" T2-LinkedIn: " +str(t2linkedin))
    print (" T3-URL: " +str(t3url))
    print (" T3-Facebook: " +str(t3facebook))
    print (" T3-Twitter: " +str(t3twitter))
    print (" T3-LinkedIn: " +str(t3linkedin))
    print (" T4-URL: " +str(t4url))
    print (" T4-Facebook: " +str(t4facebook))
    print (" T4-Twitter: " +str(t4twitter))
    print (" T4-LinkedIn: " +str(t4linkedin))
    
    print (" A1-URL: " +str(a1url))
    print (" A1-Facebook: " +str(a1facebook))
    print (" A1-Twitter: " +str(a1twitter))
    print (" A1-LinkedIn: " +str(a1linkedin))
    print (" A2-URL: " +str(a2url))
    print (" A2-Facebook: " +str(a2facebook))
    print (" A2-Twitter: " +str(a2twitter))
    print (" A2-LinkedIn: " +str(a2linkedin))
    print (" A3-URL: " +str(a3url))
    print (" A3-Facebook: " +str(a3facebook))
    print (" A3-Twitter: " +str(a3twitter))
    print (" A3-LinkedIn: " +str(a3linkedin))
    print (" A4-URL: " +str(a4url))
    print (" A4-Facebook: " +str(a4facebook))
    print (" A4-Twitter: " +str(a4twitter))
    print (" A4-LinkedIn: " +str(a4linkedin))

    print (" I1-URL: " +str(i1url))
    print (" I1-Facebook: " +str(i1facebook))
    print (" I1-Twitter: " +str(i1twitter))
    print (" I1-LinkedIn: " +str(i1linkedin))
    print (" I2-URL: " +str(i2url))
    print (" I2-Facebook: " +str(i2facebook))
    print (" I2-Twitter: " +str(i2twitter))
    print (" I2-LinkedIn: " +str(i2linkedin))
    print (" I3-URL: " +str(i3url))
    print (" I3-Facebook: " +str(i3facebook))
    print (" I3-Twitter: " +str(i3twitter))
    print (" I3-LinkedIn: " +str(i3linkedin))
    print (" I4-URL: " +str(i4url))
    print (" I4-Facebook: " +str(i4facebook))
    print (" I4-Twitter: " +str(i4twitter))
    print (" I4-LinkedIn: " +str(i4linkedin))
    print (" I5-URL: " +str(i5url))
    print (" I5-Facebook: " +str(i5facebook))
    print (" I5-Twitter: " +str(i5twitter))
    print (" I5-LinkedIn: " +str(i5linkedin))

    print (" B1-URL: " +str(b1url))
    print (" B1-Facebook: " +str(b1facebook))
    print (" B1-Twitter: " +str(b1twitter))
    print (" B1-LinkedIn: " +str(b1linkedin))
    print (" B2-URL: " +str(b2url))
    print (" B2-Facebook: " +str(b2facebook))
    print (" B2-Twitter: " +str(b2twitter))
    print (" B2-LinkedIn: " +str(b2linkedin))
    print (" B3-URL: " +str(b3url))
    print (" B3-Facebook: " +str(b3facebook))
    print (" B3-Twitter: " +str(b3twitter))
    print (" B3-LinkedIn: " +str(b3linkedin))
    print (" B4-URL: " +str(b4url))
    print (" B4-Facebook: " +str(b4facebook))
    print (" B4-Twitter: " +str(b4twitter))
    print (" B4-LinkedIn: " +str(b4linkedin))
    
    print ("------------------------------------------------")
    print ("    COUNT >> " +str(count))
    print ("------------------------------------------------")

    cot.writerows([[uid,cname,url,f1url,f2url,f3url,f4url,f1facebook,f1twitter,f1linkedin,f2facebook,f2twitter,f2linkedin,f3facebook,f3twitter,f3linkedin,f4facebook,f4twitter,f4linkedin,t1url,t2url,t3url,t4url,t1facebook,t1twitter,t1linkedin,t2facebook,t2twitter,t2linkedin,t3facebook,t3twitter,t3linkedin,t4facebook,t4twitter,t4linkedin,a1url,a2url,a3url,a4url,a1facebook,a1twitter,a1linkedin,a2facebook,a2twitter,a2linkedin,a3facebook,a3twitter,a3linkedin,a4facebook,a4twitter,a4linkedin,i1url,i2url,i3url,i4url,i5url,i1facebook,i1twitter,i1linkedin,i2facebook,i2twitter,i2linkedin,i3facebook,i3twitter,i3linkedin,i4facebook,i4twitter,i4linkedin,i5facebook,i5twitter,i5linkedin,b1url,b2url,b3url,b4url,b1facebook,b1twitter,b1linkedin,b2facebook,b2twitter,b2linkedin,b3facebook,b3twitter,b3linkedin,b4facebook,b4twitter,b4linkedin]])
    line = f.readline()
f.close()
g.close()
