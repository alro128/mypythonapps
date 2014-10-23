import nltk   
import urllib2


#Autenticacion Proxy
proxyurl = 'http://proxy.empresa.local:8080'
proxyusername = 'usuario'
proxypassword = 'password'
proxypassword_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

proxypassword_mgr.add_password(None, proxyurl, proxyusername, proxypassword)
auth_handler = urllib2.HTTPBasicAuthHandler(proxypassword_mgr)
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)

#Datos Entrada
dominiosub="http://www.podnapisi.net"
name="anger+management"
season="2"
episode=""
url = dominiosub+"/es/ppodnapisi/search?sJ=2&sT=1&sK="+name+"&sTS="+season+"&sTE="+episode
basedir = "C:\\Python\\workspace_python\\downloads\\"

#test = urllib2.urlopen(url,  proxies = {'http': 'http://proxy.emea.prosegur.local:8080'}).read()   
test = urllib2.urlopen(url).read()   

sane = 0
linkpagelist = []
linksublist = []
while sane == 0:
  curpos = test.find("href")
  if curpos >= 0:
    testlen = len(test)
    test = test[curpos:testlen]
    curpos = test.find('"')
    testlen = len(test)
    test = test[curpos+1:testlen]
    curpos = test.find('"')
    linkpage = test[0:curpos]
#if needle.startswith("http" or "www" or "/"):	
    if linkpage.find("subtitles") != -1:
      linkpagelist.append(linkpage)
      suburl = dominiosub+linkpage
      subpage = urllib2.urlopen(suburl).read()   
      subpos = subpage.find("button big download")
      sublen = len(subpage)
      subpage = subpage[subpos:sublen]
      subpos = subpage.find('href="')
      sublen = len(subpage)
      subpage = subpage[subpos+6:sublen]
      subpos = subpage.find('"')
      linksub = subpage[0:subpos]
      linksublist.append(linksub)
  else:
    sane = 1
for item in linkpagelist:
  print item

for item in linksublist:  
  print item
  filename = item.split('/')[-1]
  with open(basedir+filename+".zip", "wb") as code:
    code.write(urllib2.urlopen(dominiosub+item).read())
