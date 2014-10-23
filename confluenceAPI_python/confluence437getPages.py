from suds.client import Client

url = 'http://locahost:8090/confluence/rpc/soap-axis/confluenceservice-v2?wsdl'
client = Client(url)

spacekey  = "ESPACIO"
user   = "confluence-testuser-contributor"
password = "testuser"
token = client.service.login(user,password)

print token

#parentId por pais
pages = client.service.getPages(token, spacekey)
for p in pages:
    pdata = client.service.getPage(token, p.id)
    pcontent = pdata.content
    sane = 0
    row = ""
    while sane == 0:
      curpos = pcontent.find("<td>")
      if curpos >= 0:
        textlen = len(pcontent)
        pcontent = pcontent[curpos:textlen]
        curpos = pcontent.find('>')
        textlen = len(pcontent)
        pcontent = pcontent[curpos+1:textlen]
        curpos = pcontent.find('</td>')
        row = row + "; " + pcontent[0:curpos]
      else:
        sane = 1
        print str(p.id) + " " + p.title
        print row

#pdata = client.service.getPage(token,spacekey,"Hamburg")
#pdata = client.service.getPage(token, 20746199)
#print str(pdata.created)
#print pdata.content


#newpagedata = {"space":spacekey,"title":"PaginaPython1","content":"<h1>titulo</h1><p>new content</p>","parentId":parentPage.id}

#store = client.service.storePage(token, newpagedata)
#print store