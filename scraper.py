import requests
from bs4 import BeautifulSoup

print("¡Hola! El robot se ha despertado correctamente.")

# Ejemplo básico de prueba con una petición web
url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    print("Conexión exitosa con la red.")
else:
    print("Hubo un problema de conexión.")
