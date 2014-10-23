from suds.client import Client
import datetime

class Utils:
  def getTd(self, tempcont, name):
    curpos = tempcont.find(name)
    contlen = len(tempcont)
    tempcont = tempcont[curpos:contlen]
    pini = tempcont.find('<td>')
    pfin = tempcont.find('</td>')
    restd = tempcont[pini+4:pfin]
    return restd
  def correctHTML(self,s):
    s = s.replace("&", "")
    s = s.replace("tilde;", "")
    s = s.replace("acute;", "")
    s = s.replace("uml;", "")
    s = s.replace("nbsp;", " ")
    return s

#url = 'http://10.28.25.195:8090/confluence/plugins/servlet/soap-axis1/confluenceservice-v2?wsdl'
url = 'http://10.28.24.77:8090/confluence/rpc/soap-axis/confluenceservice-v2?wsdl'
client = Client(url)

fields=[]
fields.append("Pa&iacute;s")
fields.append("Desde")
fields.append("Propiedad/Alquiler")
fields.append("Hasta")
fields.append("Provincia")
fields.append("Propietario")
fields.append("Estado / Regi&oacute;n")
fields.append("Alquiler A&ntilde;o (mon.local)")
fields.append("Direcci&oacute;n")
fields.append("Meses de preaviso")
fields.append("C&oacute;digo Postal")
fields.append("A&ntilde;o valor")
fields.append("Suelo (m2)")
fields.append("m2 edificados")
fields.append("Fecha de Compra")
fields.append("C&oacute;digo Ubicaci&oacute;n")
fields.append("Tipo de Instalaci&oacute;n")
fields.append("V.Adquisici&oacute;n (en miles)")
fields.append("V.Neto (miles mon.local)")
fields.append("Valor Neto euro")
fields.append("A&ntilde;o Valor")

u = Utils()
spacekey  = "INMUEBLES"
user   = "confluence-autoextractor"
password = "joand"
token = client.service.login(user, password)
print token

rows=[]
pages = client.service.getPages(token, spacekey)
for p in pages:
    pdata = client.service.getPage(token, p.id)
    #print "----" + pdata.title + "----"
    if pdata.content is not None:
      pcontent = pdata.content
      if pcontent.find("<tbody>") != -1:
        sane = 0
        row = ""
        pcontent = pcontent.replace(" colspan=\"1\"", "")
        pcontent = pcontent.replace(" colspan=\"3\"", "")
        pcontent = pcontent.replace(" rowspan=\"5\"","")
        pcontent = pcontent.replace("<p>","")
        pcontent = pcontent.replace("</p>","")
        tini = pcontent.find("<table>")
        tfin = pcontent.find('</table>')
        pcontent = pcontent[tini:tfin+8]
        #print pcontent
        for f in fields:
            row = row + u.getTd(pcontent, f) + ";"
        rows.append(row)

basedir = "C:\\python\\workspace\\utils\\webservices\\"
reportdate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
f = open(basedir+'inmueblesData_'+reportdate+'.csv', 'w')
header = ""
for h in fields:
    header = header + u.correctHTML(h) + ";"
print header
f.write(header + '\n')
for r in rows:
    print u.correctHTML(r)
    f.write(u.correctHTML(r) + '\n')
f.close()
