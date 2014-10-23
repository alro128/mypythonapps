import csv
import sys
import string
from cuentat import cuentat

#Carga de datos
titulo = str(sys.argv[1])
with open(titulo+'.csv', 'rb') as f:
	data = list(tuple(row) for row in csv.reader(f, delimiter=';'))

#Cuentas
accounts = list()
activo_gasto = ['af','ac','ge','gf']
pasivo_ingreso = ['pn','pe','ie','if']

#Listado de Asientos contables	
asiento = '1'	
for i,a in enumerate(data):
	if i==0:
		print 'Libro Diario: ' +  titulo
		print 'Total registros: ' + str(len(data))		
		print string.ljust('Asientos', 35) + string.ljust('Debe', 10) + string.ljust('Haber', 10)	
		print 'Asiento ' + a[0]

	if (i>0 and a[0] != asiento):
		asiento = a[0]
		print 'Asiento ' + a[0]
	print string.rjust(a[2], 35) + string.rjust(a[3], 10) + string.ljust(a[4], 10) + a[5]
	if not (any(acc.nombre == a[2].lower() for acc in accounts)):
		cta = cuentat(a[1].lower(),a[2].lower())
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

#Listado y Cierre de Cuentas T
activofijo = 0
activocirculante = 0
pasivo = 0
patrimonio = 0
ingresosexplotacion = 0
ingresosfinancieros = 0
gastosexplotacion = 0
gastosfinancieros = 0

print '\n****Cierre de Cuentas****\n'

for acc in accounts:
	print string.ljust(acc.nombre.title(), 35) + string.rjust(str(acc.cierre()),8)
	if (acc.tipo.lower() == 'af'):
		activofijo += acc.cierre()
	elif acc.tipo.lower() == 'ac':		
		activocirculante += acc.cierre()
	elif acc.tipo.lower() == 'pe':
		pasivo += acc.cierre()
	elif acc.tipo.lower() == 'pn':
		patrimonio += acc.cierre()
	elif acc.tipo.lower() == 'ie':
		ingresosexplotacion += acc.cierre()
	elif acc.tipo.lower() == 'if':
		ingresosfinancieros += acc.cierre()
	elif acc.tipo.lower() == 'ge':
		gastosexplotacion += acc.cierre()		
	else: 
		gastosfinancieros += acc.cierre()

print '\n****Cuenta PyG****\n'
print 'Ingresos de Explotacion:    ' + string.rjust(str(ingresosexplotacion),8)
print 'Gastos de Explotacion:      ' + string.rjust(str(gastosexplotacion),8)
print 'Ingresos Financieros:       ' + string.rjust(str(ingresosfinancieros),8)
print 'Gastos Financieros:         ' + string.rjust(str(gastosfinancieros),8)
print 'Impuestos sobre Beneficios:        0' 
print '                        --------------------'
beneficio = ingresosexplotacion-gastosexplotacion+ingresosfinancieros-gastosfinancieros
print 'Beneficio del Ejercicio:   ' + str(beneficio)

print '\n****Balance de Situacion****\n'

print 'Activo Fijo:       ' + str(activofijo)
print 'Activo Circulante: ' + str(activocirculante)
print 'Patrimonio Neto:       ' + str(patrimonio)
print 'Pasivo Exigible:           ' + str(pasivo)


print '(activofijo+activocirculante) ' + str(activofijo+activocirculante) + ' = (patrimonio neto + pasivo)' + str(patrimonio+pasivo+beneficio)

#with open(titulo+'.html', 'wb') as f:
#    f.write(html)	
	
	