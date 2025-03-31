
# Analizador Léxico en Python

## Descripción

Este es un **analizador léxico** en Python que lee un archivo de texto (`texto.txt`) y lo procesa para identificar distintos tipos de tokens como números, operadores, variables, comentarios, entre otros. Utiliza una **tabla de transiciones** para procesar el texto basado en los caracteres que encuentra, e imprime el tipo de token correspondiente.

## Requisitos

Para ejecutar este programa, necesitas tener instalado Python 3 en tu sistema (se instaló la extensión en VS Code)

Debe tener el archivo de texto con los ejemplos de strings a analizar dentro de la misma carpeta en donde se encuentra el programa Lexer. Para este ejemplo, la funcion lexer recibe el archivo texto.txt. Ambos se encuentran dentro de una misma carpeta. Por ende, lo unico que debe hacer el usuario es correrlo, ya sea con el botón de run en VS Code o escribiendo el siguiente comando en la terminal:

python DFAActividad.py

## Salida
Se imprime directamente en la terminal la siguiente tabla:
- b Variable
- = Asignacion
- 7 Entero
- a Variable
- = Asignacion
- 32.4 Real
- '*' Multiplicacion
- ( Parentesis que abre
- -8.6 Real
- '-' Resta
- b Variable
- ) Parentesis que cierra
- / Division
- 6.1E-8 Real
- d Variable
- = Asignacion
- a Variable
- ^ Potencia
- b Variable
Igualmente, imprime el archivo de texto para asegurarnos de que se lee correctamente. 

## DFA que resuelve el problema
