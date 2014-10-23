from suds.client import Client
url = 'http://servicio.local/login/soap/v1?wsdl'
client = Client(url)

domains = client.service.getDomains()

for domain in domains:
	print domain

result2 = client.service.userLogin("usuario","password","dominio")

print result2