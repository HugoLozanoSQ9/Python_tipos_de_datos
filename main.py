print("Iniciando programa")

print("Hola koders" )#Esta funcion imprime un saludo 

print("Terminando programa")

print("Programa terminado")

x = 5
y=10
suma = x + y
print("Tu suma es:" ,suma)

#tipos de datos 
entero = 10 
flotante = 3.14 # si yo guardo 10.0 sigue siendo flotante
cadena_de_texto = "hola tilin"
lista = [1,2,3,4,5,6]
tupla = (1,2,3,4,5,6)
diccionario = {"nombre": "alfredo", "edad":"36"}

#operadores aritmeticos
suma = 2+2
resta = 2-2
multiplicacion = 3*4
division = 10/2
division_entera = 10//3
modulo = 10 % 3
exponente = 2**4 #(2 a la 4)
age = 20

#condicionales 
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Aun no eres mayor de edad")

#bucles 
    for i in range(1,5):
        print(i)

contador = 10

while contador <= 10:
    print(contador)
    contador +=1

#El decimal es directo 
#binario
0b0101011101110
#Octal
0o0123424213
#Hexadecimal
0xABC123423DEF232213

#notación científica esto aplica para flotantes
4.2e7  #nos va a recorrer el punto 7 lugares a la derecha 
4.2e-4 #nos va a recorrer el punto 4 lugares a la izquierda
 
 #caracteres de escape 
#la diagonal invertida hace que nuestro siguiente caracter no lo ejecute por obviedad del lenguaje 
'Hola koders este es un apostrofe --> \''
#también aplica con los "Enter" si yo pongo una diagonal invertida y doy enter sigo escribiendo (no se ejecuta) esto en el REPL
#por ejemplo si quiero que se vea un tabulador hago esto:
print('\t <-- aqui se ve un tabulador ')
#hereda el salto de linea de C
#unicode
print('\u2665')
#print('\N{Rigthwards Arrow}')

#Liistas de python
lista = [10,1.5,'hola tilin',[1,2,3]]
type(15)
[1,2,3][0]