try:
					encontrar_operador = archivo2[i][3] in operadores
					print(encontrar_operador)
				except IndexError:
					if encontrar_variable != True:
						print("Error: la variable <",archivo2[i][0],"> no existe dentro de la gramatica\tError: en la fila",z)
					else:
						if archivo2[i][1] == operadores[4]:
							asd = ayuda_registro2.get(archivo2[i][0])
							encontrar_v = archivo2[i][2] in variables 
							encontrar_n = esentero(archivo2[i][2])	
							if asd == None:
								print("Error: la variable <",archivo2[i][0],"> no esta declarada\tError: en la fila",z)
							else:
								if encontrar_v == True or encontrar_n == True:
									print("hola")
								else:
									print("es cadena")			