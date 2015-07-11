variables = ["a","e","i","o","u"]
ayuda_registro = {variables[0]:None,variables[1]:None,variables[2]:None,variables[3]:None,variables[4]:None}
#ayuda_registro[variables[0]]=1
#print(ayuda_registro)
palabras_clave = ["Inicio","Fin","Entero","Cadena","Mostrar"]
operadores = ["+","-","*","/","="]
numero = ["0","1","2","3","4","5","6","7","8","9"]

def separador_string(cadena):
	separador = ""
	longitud = len(cadena)
	for i in range(longitud):
		separador += ","+entrada[i]
	separador = separador.split(",")[1:]
	return separador

def esentero(entrada):
	b = {}
	entrada = str(entrada)
	longitud = len(entrada)
	for i in range(longitud):
		a = entrada[i] in numero
		if a == True:
			b[i] = "Es entero"
		else:
			b[i] = "No es entero"
	lista = list(b.values())
	#print(lista)
	c = "No es entero" in lista
	c = not c
	return c

archivo=open('/home/marlonp/python/ejemplo.txt','r')
archivo_array=archivo.readlines()
#print(archivo_array)
longitud_filas_archivo = len(archivo_array)
#print(longitud_filas_archivo)
#print(archivo_array[1][:-1])
cont = 0
for i in range(longitud_filas_archivo):
	if archivo_array[i]=="\n":
		cont = cont + 1
#print(cont)
archivo_array = archivo_array[cont:]
array_corregido = ""
for i in range(len(archivo_array)):
	array_corregido += ","+archivo_array[i][:-1]
array_corregido = array_corregido.split(",")[1:]
archivo_array = array_corregido
#print(archivo_array)
#print(archivo_array[0])
if archivo_array[0] == palabras_clave[0]:
	#print(archivo_array[0])
	a = palabras_clave[1] in archivo_array
	if a == True:
		#print(archivo_array[0])
		encontrar_fin = archivo_array.index(palabras_clave[1])
		archivo = ""
		for i in range(1,encontrar_fin):
			archivo += "," + archivo_array[i][1:]
		archivo = archivo.split(",")[1:]
		#print(archivo)
		archivo2 = {}
		for i in range(len(archivo)):
			archivo2[i] = archivo[i].split(" ")
			#print(archivo2[i])
		#print(archivo2[0][0])
		#print(len(archivo2))
		#print(archivo2)
		for i in range(len(archivo2)):
			
#palabras_clave = ["Inicio","Fin","Entero","Cadena","Mostrar"] 
			if archivo2[i][0]==palabras_clave[2] or archivo2[i][0]==palabras_clave[3]:
				encontrar_variable = archivo2[i][1] in variables
				z = int(cont)+1+int(i)+1
				if encontrar_variable != True:
					print("Error: la variable <",archivo2[i][1],"> no existe dentro de la gramatica\tError: en la fila",z)
				else:
					if archivo2[i][2] == operadores[4]:
						if archivo2[i][0] == palabras_clave[2]:
							ent = esentero(archivo2[i][3])
							if ent == False:
								print("Error: la variable <",archivo2[i][1],"> no es entero\tError: en la fila",z)
							else:	
								ayuda_registro[archivo2[i][1]] = [archivo2[i][3]]
						if archivo2[i][0] == palabras_clave[3]:
							ayuda_registro[archivo2[i][1]] = [archivo2[i][3]]

			else:
				print("no esta declarando variables")
		prueba = str(ayuda_registro.get("a"))
		prueba = prueba[2:-2]
		print(ayuda_registro)


			
		#print(archivo_array[encontrar_fin])
	else:
		print("Error: el algoritmo inicia pero no tiene fin")
	
else:
	print("Error: el algoritmo no inicia nunca")
		#if archivo_array[i][:-1]=="Inicio":
			#print("Inicio1")	
	#if archivo_array[i]!="\n":
	#	if archivo_array[i][:-1]=="Inicio":
#			print(archivo_array[i][:-1])	
	#	else:
	#		print("No existe")
	#else:
	#	cont = cont + 1
#		print("Existe salto de linea")	

#print(linea[0].count("\t"))
#print(linea[1].startswith("\t"))

#print(linea)
#while linea!="":
#	print(linea)
#	linea=archivo.readline()
	
#entrada = input("ingrese la entrada:")
#entrada = separador_string(entrada)

#def comparar(array)




	  


