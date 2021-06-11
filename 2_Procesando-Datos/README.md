# Conociendo Python

### Características
- Lenguaje de programación completo
- Multi propósito (automazar tareas, procesa datos, bases de datos, interfaces de usuario, interfaces de sistemas, redes, juegos, enseñanza, administración de sistemas, etc.)
- Desarrollo ágil o rápido
- Interpretado
- Multiplataforma (Linux, Mac, Windows, RaspPi)
- Multiparadigma (Estructurado, Orientado a objetos, Funcional, ...)
- Con una filosofía de: "Lo simple es bello" o "Si algo es muy complicado de explicar, seguramente hay una forma más simple de hacerlo"


### El "hola mundo" con Python

Esto es para comprobar que la instalación de Python está funcionando de forma correcta y para conocer como se puede comenzar a programar en Python.

Así que primer paso será abrir el programa conocido como la terminal, para usuarios en Windows buscar la aplicación **Anaconda Prompt** 

Luego hay que escribir el comando `python` hasta obtener los símbolos `>>>` y entonces escribir la instrucción en Python `print("Hola mundo, te voy a conquistar usando Python!")` y presionar la tecla ENTER al final.

Si todo ha funciona bien hasta aquí significa que Python está correctamente instalado y has dado tu primer paso en la programación con Python.

### Conociendo el nivel de popularidad de Python

Hoy en día existen varios índices donde se mide la popularidad de casi todos los lenguajes de programación, algunos de estos ejemplos son:

- https://www.tiobe.com/tiobe-index
- https://statisticstimes.com/tech/top-computer-languages.php
- https://insights.stackoverflow.com/survey/2020

Pero que pasa si queremos automatizar una tarea donde quicieramos obtener la posición de Python en la lista de TIOBE, pues vamos a hacerlo.

Primero hay que obtener o descargar la página del índice, para ello hay que instalar una librería o módulo de Python llamada `requests` y se realiza con el comando `pip install requests`

Luego volvemos a Python con el comando `python` y comenzamos nuestro viaje ...

Para obtener toda la información de la página hacemos lo siguiente:

```
import requests
pagina = requests.get("https://www.tiobe.com/tiobe-index")
pagina.status_code
pagina.text[:500]
pagina.text.split("\n")[:5]
lineas = pagina.text.split("\n")
for linea in lineas:
    if "python" in linea.lower():
        print(linea)
```

El código parece algo complejo, pero el resultado obtenido parece aún más complejo, así que "seguramente habrá una forma más sencilla de hacerlo".

Que pasa si en la página del índice TIOBE damos click sobre la línea de Python en la tabla, vemos que se abre otra página donde se muestra sólo la información de Python y la posición está marcada en las línea con el texto "Position", veamos si es más simple de esta forma:

```
import requests
pagina = requests.get("https://www.tiobe.com/tiobe-index")
pagina.status_code
pagina.text[:500]
pagina.text.split("\n")[:5]
lineas = pagina.text.split("\n")
for linea in lineas:
    if "python" in linea.lower():
        print(linea)
```

Genial, misión cumplida
