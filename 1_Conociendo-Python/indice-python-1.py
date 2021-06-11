import requests
pagina = requests.get("https://www.tiobe.com/tiobe-index")
pagina.status_code
pagina.text[:500]
pagina.text.split("\n")[:5]
lineas = pagina.text.split("\n")
for linea in lineas:
    if "python" in linea.lower():
        print(linea)

