nombre = 'Alfredo'
apellido='Altamirano'
#3 variables diferentes

print('Hola', nombre)

#en este curso vamos a manejar snake case
nombre_de_usuario = 2
#se pueden usar numeros pero al final / enmedio del nombre
edad = 36
edad = edad + 10 
nombre_completo = nombre + " " + apellido + " "
#Un string se puede multiplicar N veces
print(nombre_completo * 5)
#Python no concatena string y numeros tenemos que convertir los datos enteros a string
print(edad)
#se pueden hacer condicionales jeje 
comida = input('Grr dame de comer ')
if comida == 'x':
    print('Gracias jsjs')
 
entero = int('101')
print(entero) #ya nos convierte este valor en int 
#y se puede proceder ya con operaciones 
suma = entero + 10
print (suma)

flotante = float('101') # ahora se convierte a flotante (da de resultado 101.0)
string = str(101) #Ahora es un string y se puede concatenar con otro string

#con los números si nosotros hacemos un valor diferente de 0 nos retornará un valor verdadero, pero si el valor es 0 entonces es falso
verdadero = bool(1) #true si se intenta imprimir nos mostrará que es True
falso = bool(2) #false

#En el caso de los strings si es un string vacío será falso, en caso de que el string NO esté vacio será un dato verdadero
bool ('a') #Esto nos daría verdadero 
bool ('') #esto sería un dato falso

#Es una función que me permite obtener diccionarios
fun = dict(name = 'Alfredo', apellido = 'Altamirano')
print (fun) 





