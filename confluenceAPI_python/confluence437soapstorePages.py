from suds.client import Client

url = 'http://10.28.25.195:8090/confluence/plugins/servlet/soap-axis1/confluenceservice-v2?wsdl'
client = Client(url)

spacekey  = "ESPACIO" #sys.argv[2]
user   = "confluence-testuser" #sys.argv[3]
password = "testuser" #sys.argv[4]
token = client.service.login(user,password)

print token

#pages = client.service.getPages(token,spacekey)
#print pages

parentPage = client.service.getPage(token, spacekey, "nuevas")
print parentPage
print parentPage.id

newpagedata = {"space":spacekey,"title":"PaginaPython1","content":"<h1>titulo</h1><p>new content</p>","parentId":parentPage.id}

store = client.service.storePage(token, newpagedata)
print store