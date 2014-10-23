#!/usr/bin/python
# -*- coding: utf-8 -*-
from suds.client import Client
import csv
import htmlentitydefs as entity

class Utils:
  def getHTML(self, s):
    t = ""
    for i in s:
      if ord(i) in entity.codepoint2name:
        name = entity.codepoint2name.get(ord(i))
        t += "&" + name + ";"
      else:
        t += i
    return t

u = Utils()
basedir = "C:\\python\\workspace\\utils\\webservices\\"
csvfile = "cargaMasiva_inmuebles.csv"
#22381895 Otras de espacio TEMPDEV
parentPage = 22381895

a = [];
i=0;

csvReader = csv.reader(open(basedir+csvfile, 'rb'), delimiter=';')
for row in csvReader:
  a.append(row)

print(a[0])
print(len(a)-1)

spacekey = "TEMPDEV"
user = "confluence-autoextractor"
password = "autoextractor"

url = 'http://localhost:8090/confluence/rpc/soap-axis/confluenceservice-v2?wsdl'
client = Client(url)
token = client.service.login(user, password)
print(token)

for i in range(1, len(a)):
  nwpage = {"space":spacekey, "title": u.getHTML(a[i][4]), "parentId":parentPage, "content":"<h2>Datos de Inmueble&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h2><p>&nbsp;</p><table><tbody><tr><th class='highlight-blue' colspan='4' data-highlight-colour='blue' style='text-align: center;'><strong>FICHA&nbsp;INMUEBLE&nbsp;</strong></th></tr><tr><th class='highlight-blue' colspan='2' data-highlight-colour='blue' style='text-align: center;'>Com&uacute;n</th><th class='highlight-blue' colspan='2' data-highlight-colour='blue'><p style='text-align: center;'>Alquiler</p></th></tr><tr><th><p>Pa&iacute;s</p></th><td>"+u.getHTML(a[i][0])+"</td><th>Desde</th><td colspan='1'>"+u.getHTML(a[i][1])+"</td></tr><tr><th><p>Propiedad/Alquiler</p></th><td>"+u.getHTML(a[i][2])+"</td><th>Hasta</th><td colspan='1'>"+u.getHTML(a[i][3])+"</td></tr><tr><th><p>Provincia</p></th><td>"+u.getHTML(a[i][4])+"</td><th>Propietario</th><td colspan='1'>"+u.getHTML(a[i][5])+"</td></tr><tr><th><p>Estado / Regi&oacute;n</p></th><td>"+u.getHTML(a[i][6])+"</td><th>Alquiler A&ntilde;o (mon.local)</th><td colspan='1'>"+u.getHTML(a[i][7])+"</td></tr><tr><th><p>Direcci&oacute;n</p></th><td>"+u.getHTML(a[i][8])+"</td><th><p>Meses de preaviso</p></th><td colspan='1'>"+u.getHTML(a[i][9])+"</td></tr><tr><th colspan='1'>C&oacute;digo Postal</th><td colspan='1'>"+u.getHTML(a[i][10])+"</td><th colspan='1'>A&ntilde;o valor</th><td colspan='1'>"+u.getHTML(a[i][11])+"</td></tr><tr><th><p>Suelo (m2)</p></th><td><p>"+u.getHTML(a[i][12])+"</p></td><th class='highlight-blue' colspan='2' data-highlight-colour='blue' style='text-align: center;'>Propiedad</th></tr><tr><th><p>m2 edificados</p></th><td>"+u.getHTML(a[i][13])+"</td><th>&nbsp;Fecha de Compra</th><td colspan='1'>"+u.getHTML(a[i][14])+"</td></tr><tr><th><p>C&oacute;digo Ubicaci&oacute;n</p></th><td>"+u.getHTML(a[i][15])+"</td><th class='highlight-blue' colspan='2' data-highlight-colour='blue' style='text-align: center;'>&nbsp;&nbsp;Usos</th></tr><tr><th>Tipo de Instalaci&oacute;n</th><td>"+u.getHTML(a[i][16])+"</td><th rowspan='5'><p>&nbsp;</p><p>&nbsp;</p><p>Uso&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p></th><td rowspan='5'><p>&nbsp;</p><ul><li>LVGE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;X</li><li>Vigilancia&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--</li><li>Alarmas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X</li><li>Tecnolog&iacute;a&nbsp;&nbsp;&nbsp; --</li><li>Otros&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; X</li></ul></td></tr><tr><th>V.Adquisici&oacute;n (en miles)</th><td>"+u.getHTML(a[i][17])+"</td></tr><tr><th colspan='1'>V.Neto (miles mon.local)</th><td colspan='1'>"+u.getHTML(a[i][18])+"</td></tr><tr><th colspan='1'>Valor Neto euro</th><td colspan='1'>"+u.getHTML(a[i][19])+"</td></tr><tr><th colspan='1'>A&ntilde;o Valor</th><td colspan='1'>"+u.getHTML(a[i][20])+"</td></tr><tr><th colspan='1'><p>Comentarios 1</p></th><td colspan='3'>&nbsp;&nbsp;</td></tr><tr><th colspan='1'><p>Comentarios 2</p></th><td colspan='3'>&nbsp;</td></tr></tbody></table><h3>Ubicaci&oacute;n en Mapa</h3><ac:macro ac:name='iframe'><ac:parameter ac:name='height'>400</ac:parameter><ac:parameter ac:name='width'>400</ac:parameter><ac:parameter ac:name='src'>https://www1.sedecatastro.gob.es/Cartografia/mapa.aspx</ac:parameter><ac:rich-text-body>&nbsp;</ac:rich-text-body></ac:macro><ac:macro ac:name='html'><ac:plain-text-body><![CDATA[]]></ac:plain-text-body></ac:macro><h3>Fotos</h3><p><em>pegar fotos en esta secci&oacute;n cuando edite la p&aacute;gina</em></p><ac:macro ac:name='td'><ac:parameter ac:name='width'>507px</ac:parameter><ac:parameter ac:name='align'>right</ac:parameter><ac:rich-text-body><p><ac:macro ac:name='gallery'><ac:parameter ac:name='excludeLabel'>plan, other</ac:parameter></ac:macro></p></ac:rich-text-body></ac:macro><h3><ac:macro ac:name='attachments'><ac:parameter ac:name='labels'>photo</ac:parameter><ac:parameter ac:name='upload'>false</ac:parameter></ac:macro></h3><h3>Planos</h3><p><em>Secci&oacute;n utilizada para documentar: Planos en autocad y&nbsp;Otros planos o croquis,</em></p><ac:macro ac:name='td'><ac:parameter ac:name='width'>507px</ac:parameter><ac:parameter ac:name='align'>right</ac:parameter><ac:rich-text-body><p><ac:macro ac:name='gallery'><ac:parameter ac:name='excludeLabel'>photo, other</ac:parameter></ac:macro></p></ac:rich-text-body></ac:macro><p><ac:macro ac:name='attachments'><ac:parameter ac:name='labels'>plan</ac:parameter><ac:parameter ac:name='upload'>false</ac:parameter></ac:macro></p><h3>Otros</h3><p><em>Secci&oacute;n utilizada para documentar:</em>&nbsp;<em>Contratos de alquiler, propiedad, fotos, ficheros Word, Excel, etc.</em>&nbsp;</p><ac:macro ac:name='td'><ac:parameter ac:name='width'>507px</ac:parameter><ac:parameter ac:name='align'>right</ac:parameter><ac:rich-text-body><p><ac:macro ac:name='gallery'><ac:parameter ac:name='excludeLabel'>photo, plan</ac:parameter></ac:macro></p></ac:rich-text-body></ac:macro><h3><ac:macro ac:name='attachments'><ac:parameter ac:name='labels'>other</ac:parameter><ac:parameter ac:name='upload'>false</ac:parameter></ac:macro></h3><h3>Proyectos</h3><p><em>enlaces a proyectos en Jira</em></p><p>&nbsp;</p><p>&nbsp;</p>"}
  store = client.service.storePage(token, nwpage)
  print(store)
