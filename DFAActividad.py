'''
Amilka Daniela Lopez Aguilar 
A01029277
Actividad 3.2 Programando un DFA

Este es un analizador léxico en Python que lee un archivo de texto (texto.txt) y 
lo procesa para identificar distintos tipos de tokens como números, operadores, variables, comentarios, entre otros. 
Utiliza una tabla de transiciones para procesar el texto basado en los caracteres que encuentra, 
e imprime el tipo de token correspondiente.

'''

#funcion lexer que recibe un archivo de texto
def lexerAritmetico(nombre_archivo):
    with open(nombre_archivo, 'r') as file: 
# Leemos todo el contenido del archivo y lo asignamos a la variable 's'
        s = file.read()

# Ahora 's' contiene el texto del archivo 
    print(s)  # Imprime el contenido del archivo para verificar

# Tabla de transiciones
    tabla = [
    [1,11,12,19,0,4,10,13,14,15,5,17,18,19],
    [1,7,7,2,7,7,7,7,7,7,7,7,7,19],
    [3,19,19,19,19,19,19,19,19,19,19,19,19,19],
    [3,8,8,19,8,8,8,8,8,8,8,8,8,19],
    [9,9,9,19,9,4,9,9,9,9,9,9,9,19],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,19],
    [16,16,16,16,16,16,16,16,16,16,16,16,16,19]
    ]

# Declaramos los caracteres que pueden formar blanco, digito o variable
    blanco = ' \t\n'
    digito = '0123456789Ee'
    variable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_'

    estado = 0
    p = 0
    lexema = ''  # Initialize lexema as an empty string

    while (p < len(s)):

        c = s[p]

        if c in digito:
            columna = 0
        elif c == '+':
            columna = 1
        elif c == '-':
            if p + 1 < len(s) and s[p+1] in digito:
                columna = 0  # El signo negativo pertenece a un número
            else:
                columna = 2  # Operación de resta
        elif c == '.':
            columna = 3
        elif c in blanco:
            columna = 4
        elif c in variable:
            columna = 5
        elif c == '=':
            columna = 6
        elif c == '*':
            columna = 7
        elif c == '/':
            if s[p+1:p+2] == '/':  # Detectar el inicio de un comentario
                columna = 10  # Estado para comentario
            else:
                columna = 8
        elif c == '^':
            columna = 9
        elif (c == '/' and s[p+1:p+2] == '/'):
            columna = 10
        elif (c=='('):
            columna = 11
        elif (c == ')'):
            columna = 12
        else:
            columna = 13

    # Transición de estado
        estado = tabla[estado][columna]

    # Verificar si el estado corresponde a un token válido
        if estado == 7:
            print(lexema, 'Entero')
            lexema = ''  # Reset lexema after printing
            estado = 0
            p-=1
        elif estado == 8:
            print(lexema, 'Real')
            lexema = ''
            estado = 0
            p-=1
        
        elif estado == 9:
            print(lexema, 'Variable')
            lexema = ''
            estado = 0
            p-=1

        elif estado == 10:
            print(c, 'Asignacion')
            lexema = ''
            estado = 0
    
        elif estado == 11:
            print(c, 'Suma')
            lexema = ''
            estado = 0
        elif estado == 12:
            print(c, 'Resta')
            lexema = ''
            estado = 0
        elif estado == 13:
            print(c, 'Multiplicacion')
            lexema = ''
            estado = 0
        elif estado == 14:
            print(c, 'Division')
            lexema = ''
            estado = 0
        elif estado == 15:
            print(c, 'Potencia')
            lexema = ''
            estado = 0
        elif estado == 16:
            comentario = s[p+1:].split('\n')[0]
            print('//', f"{comentario}","Comentario")
            while p < len(s) and s[p] != '\n':
                p += 1
            lexema = ''
            estado = 0
        elif estado ==17:
            print(c,"Parentesis que abre")
            lexema = ''
            estado = 0
        elif estado == 18:
            print(c,"Parentesis que cierra")
            lexema = ''
            estado = 0
        elif estado == 19:
            print('Error')
            break

    # Acumular el caracter en el lexema
        if(estado !=0):
            lexema += c
    # Avanzar uno en la posición del string
        p+=1 #avanzar uno 

lexerAritmetico("texto.txt")