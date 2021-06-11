import requests
pagina = requests.get("https://www.tiobe.com/tiobe-index/python/")
pagina.status_code
pagina.text[:500]
pagina.text.split("\n")[:5]
lineas = pagina.text.split("\n")
for linea in lineas:
    if "Position" in linea:
        i = linea.index("<b>") + 4
        j = linea.index("</b>")
        print(linea[i:j])

print("\nObtenido de:\nhttps://www.tiobe.com/tiobe-index/python/")
