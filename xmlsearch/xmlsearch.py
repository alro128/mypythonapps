import urllib
#from lxml import html
import xml.etree.ElementTree as html

proxylist = ('http://proxy.empresa.local:8080')

url = "http://clarity.prosegur.es/niku/app?action=homeActionId"

root = html.fromstring(urllib.urlopen(url,  proxies = {'http': 'http://proxy.empresa.local:8080'}).read())

#Si el HTML no esta normalizado como XML no se podra parsear correctamente
print root.tag

for child in root:
 print child.tag, child.attrib

for cell in root.findall(".//td[@class='loginFooter']"):
 print cell

for celda in root.iter('.//body/table/td'):
 print celda.attrib
 
tree = html.parse('sample.xml')
raiz = tree.getroot()

for cell2 in raiz.findall(".//td[@class='loginFooter']"):
 print cell2.text
