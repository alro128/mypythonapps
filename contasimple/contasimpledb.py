import csv
import sys
from cuentat import cuentat

#Carga de datos
titulo = str(sys.argv[1])
with open(titulo+'.csv', 'rb') as f:
	data = list(tuple(row) for row in csv.reader(f, delimiter=';'))

html = '<html><body style="font-family:arial">'
#Cuentas
accounts = list()
activo_gasto = ['af', 'ac', 'ga']
pasivo_ingreso = ['pn','pe','in']

#Listado de Asientos contables	
asiento = '1'	
for i,a in enumerate(data):
	if i==0:
		html += '<h1>Libro Diario: ' +  titulo + '</h1>'
		html += 'Total registros: ' + str(len(data)) + '<br/> <hr/>'
		html += '<table border=1 style="border-spacing: 0px; border-style: solid; border-color: black;">'
		html += '<tr><th colspan=4 style="background-color: #C0C0C0;" align=left>Asiento ' + a[0] + '</th><tr>'		
	if (i>0 and a[0] != asiento):
		asiento = a[0]
		html += '<tr><th colspan=4 style="background-color: #C0C0C0;" align=left>Asiento ' + a[0] + '</th><tr>'
	html += '<tr><td>' + a[2] + '</td><td>' + a[3] + '</td><td>' + a[4] + '</td><td>' + a[5] + '</td></tr>'
	if (i==len(data)):
		html += '</table><br/>'
	if not (any(acc.nombre == a[2].lower() for acc in accounts)):
		cta = cuentat(a[1].lower(),a[2].lower())
		print 'Nueva Cuenta: ' + cta.nombre + ' Tipo: ' + cta.tipo
		if(a[3] != '' and int(a[3])>=0):
			cta.asiento('debe',int(a[3]))
		else:
			cta.asiento('haber',int(a[4]))
		accounts.append(cta)
	else:
		for acc in accounts:
			if (acc.nombre == a[2].lower()):
				if(a[3] != '' and int(a[3])>=0):
					acc.asiento('debe',int(a[3]))
				else:
					acc.asiento('haber',int(a[4]))
	
	
html += '</body></html>'	

#Listado de Cuentas T
activofijo = 0
activocirculante = 0
pasivo = 0
patrimonio = 0
ingresos = 0
gastos = 0
for acc in accounts:
	print 'Cuenta: ' , acc.nombre.title() , ' Valor cierre:' , acc.cierre()
	if (acc.tipo.lower() == 'af'):
		activofijo += acc.cierre()
	elif acc.tipo.lower() == 'ac':		
		activocirculante += acc.cierre()
	elif acc.tipo.lower() == 'pe':
		pasivo += acc.cierre()
	elif acc.tipo.lower() == 'pn':
		patrimonio += acc.cierre()
	elif acc.tipo.lower() == 'in':
		ingresos += acc.cierre()
	else: 
		gastos += acc.cierre()

print 'activofijo: ' + str(activofijo)
print 'activocirculante: ' + str(activocirculante)
print 'patrimonio: ' + str(patrimonio)
print 'pasivo: ' + str(pasivo)
print 'ingresos: ' + str(ingresos)
print 'gastos: ' + str(gastos)

print '(ingresos - gastos) ' + str(ingresos-gastos)
print '(activofijo+activocirculante) ' + str(activofijo+activocirculante) + ' = (patrimonio neto + pasivo)' + str(patrimonio+pasivo+(ingresos-gastos))

with open(titulo+'.html', 'wb') as f:
    f.write(html)	
	
	