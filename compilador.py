variables = ["&a","&e","&i","&o","&u"]
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

ayuda_registro = {variables[0]:None,variables[1]:None,variables[2]:None,variables[3]:None,variables[4]:None}
ayuda_registro2 = {variables[0]:None,variables[1]:None,variables[2]:None,variables[3]:None,variables[4]:None}

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
			z = int(cont)+1+int(i)+1
#palabras_clave = ["Inicio","Fin","Entero","Cadena","Mostrar"] 
			if archivo2[i][0]==palabras_clave[2] or archivo2[i][0]==palabras_clave[3]:
				encontrar_variable = archivo2[i][1] in variables
				#z = int(cont)+1+int(i)+1
				if encontrar_variable != True:
					print("Error: la variable <",archivo2[i][1],"> no existe dentro de la gramatica\tError: en la fila",z)
				else:
					ayuda_registro2[archivo2[i][1]] =  archivo2[i][0]
				
			else:
				encontrar_variable = archivo2[i][0] in variables
				if encontrar_variable == False and archivo2[i][0] != palabras_clave[4]:
					print("Error: El tipo de la variable <",archivo2[i][0],"> no existe dentro de la gramatica\tError: en la fila",z)
			if archivo2[i][0] == palabras_clave[4]:
				ert = archivo2[i][1] in variables
				if ert == False:
					print(archivo2[i][1])
				else:
					if ayuda_registro[archivo2[i][1]] == None:
						print("Error: La variable <",archivo2[i][1],"> que deseamos imprimir no tiene valor")
					else:
						print(ayuda_registro[archivo2[i][1]])	
			else:
				
				encontrar_variable = archivo2[i][0] in variables
				qwe = ayuda_registro2.get(archivo2[i][0])
				
				#print(encontrar_variable)
				if encontrar_variable == True:
					encontrar_variable = archivo2[i][0] in variables
					if encontrar_variable != True:
						print("Error: La variable <",archivo2[i][0],"> no existe dentro de la gramatica\tError: en la fila",z)
					if encontrar_variable == True and qwe==None:
						print("Error: La variable <",archivo2[i][0],"> no esta declarada\tError: en la fila",z)
					else:
						if len(archivo2[i])==3:
							if archivo2[i][1]== operadores[4]:
								qt = archivo2[i][2] in variables
								if qt == False:
									if qwe == palabras_clave[3]:
										ayuda_registro[archivo2[i][0]] = archivo2[i][2]
									else:
										q = esentero(archivo2[i][2])
										if q == True:
											q = "Entero"
										if q == qwe:
											ayuda_registro[archivo2[i][0]] = archivo2[i][2]
										else:
											print("Error: El valor <",archivo2[i][2],"> de la variable <",archivo2[i][0],"> no es Entero\tError: en la fila",z)
								else:
									ct = ayuda_registro.get(archivo2[i][2])
									if ct == None:
										print("Error: La variable <",archivo2[i][2],"> no tiene Valor\tError: en la fila",z)
									else:
										#ct2 = ayuda_registro2[archivo2[i][0]]
										#print(ct2)
										if ayuda_registro2[archivo2[i][0]] == palabras_clave[2] and  ayuda_registro2[archivo2[i][2]]== palabras_clave[3]:
											print("Error: La variable <",archivo2[i][0],"> no Puede ser una Cadena\tError: en la fila",z)
										else:
											ayuda_registro[archivo2[i][0]] = ayuda_registro[archivo2[i][2]]
										#if ayuda_registro2[archivo2[i][0]] == "":
										#	ayuda_registro[archivo2[i][0]] = ayuda_registro[archivo2[i][2]]
										#print("Error: La variable <",archivo2[i][2],"> SI tiene Valor")
									#print(qt," --- ",archivo2[i][2])
							else:
								print("Error: <",archivo2[i][1],"> no es el operador < = > de igualdad \tError: en la fila",z)
						else:
							if archivo2[i][1]== operadores[4]:
							#operadores = ["+","-","*","/","="]
							# &i = a * b
								if ayuda_registro2[archivo2[i][0]] != palabras_clave[3]: 
									encontrar_operador = archivo2[i][3]	in operadores[:-1]
									if encontrar_operador == True:
										cx = archivo2[i][2] in variables
										if cx == False:
											v = esentero(archivo2[i][2]) 
											if v != True:
												print ("Error: La operación no puede ser procesada, El primer valor de la operación es Cadena\tError: en la fila",z)
										else:
											if  ayuda_registro2[archivo2[i][2]] == palabras_clave[3]:
												print ("Error: La operación no puede ser procesada, el valor de la variable<",archivo2[i][2],"> es Cadena\tError: en la fila",z)
											if  ayuda_registro2[archivo2[i][2]] == palabras_clave[2]:
												if ayuda_registro[archivo2[i][2]]!= None:
													archivo2[i][2] = ayuda_registro[archivo2[i][2]]
												else:
													print("Error: La variable <",archivo2[i][2],"> no tiene Valor\tError: en la fila",z)
										cx2  = archivo2[i][4] in variables
										if cx2 == False:
											v = esentero(archivo2[i][4]) 
											if v != True:
												print ("Error: La operación no puede ser procesada, El segundo valor de la operación es Cadena\tError: en la fila",z)
										else:
											if  ayuda_registro2[archivo2[i][4]] == palabras_clave[3]:
												print ("Error: La operación no puede ser procesada, el valor de la variable <",archivo2[i][4],"> es Cadena\tError: en la fila",z)
											if  ayuda_registro2[archivo2[i][4]] == palabras_clave[2]:
												if ayuda_registro[archivo2[i][4]]!= None:
													archivo2[i][4] = ayuda_registro[archivo2[i][4]]
													#print(archivo2[i][4])
												else:
										 			print("Error: La variable <",archivo2[i][4],"> no tiene Valor\tError: en la fila",z)
										#print(archivo2[i][2])
										if esentero(archivo2[i][2]) == True and esentero(archivo2[i][4]) == True:
											if archivo2[i][3] == operadores[0]:
											 	ayuda_registro[archivo2[i][0]] = int(archivo2[i][2]) + int(archivo2[i][4])
											if archivo2[i][3] == operadores[1]:
											 	ayuda_registro[archivo2[i][0]] = int(archivo2[i][2]) - int(archivo2[i][4])
											if archivo2[i][3] == operadores[2]:
											 	ayuda_registro[archivo2[i][0]] = int(archivo2[i][2]) * int(archivo2[i][4])
											 	#print(ayuda_registro[archivo2[i][0]])
											if archivo2[i][3] == operadores[3]:
											 	ayuda_registro[archivo2[i][0]] = int(archivo2[i][2]) // int(archivo2[i][4])
										#print(ayuda_registro[archivo2[i][0]])		
									else:
										print("Error: El operador <",archivo2[i][3],"> no existe dentro de la gramatica\tError: en la fila",z)
								else:
									print ("Error: La operación no puede ser procesada, la variable <",archivo2[i][0],"> es una Cadena\tError: en la fila",z)

							#operadores = ["+","-","*","/","="]
								#if archivo2[i][3] = operadores[0]:


								#print(cx,"---------",cx2)
							else:
								print("Error: <",archivo2[i][1],"> no es el operador < = > de igualdad \tError: en la fila",z)
							#cx = ayuda_registro.get(archivo2[i]archivo2[i][3] 
							#print(cx) 
							#if archivo2[i][2]==archivo2[i][4]:
								#if archivo 
							#print(archivo2[i])
							#print(encontrar_operador)

				#	print("salto")
					#print(archivo2[i][0])
					#if archivo2[i][0]!=palabras_clave[2] and archivo2[i][0]!= palabras_clave[3]:
				#	print(archivo2[i])
						#if archivo2[i][0]== palabras_clave[3]:
							#print("Error: La variable <",archivo2[i][0],"> no existe dentro de la gramatica\tError: en la fila",z)

				#else:
				#	print("asd")			
				#print(archivo2[i][0])
				#print("no esta declarando variables")
		#print(archivo2)
		#prueba = str(ayuda_registro.get("a"))
		#prueba = prueba[2:-2]
		#print(ayuda_registro)
		#print(ayuda_registro2)


			
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




	  


