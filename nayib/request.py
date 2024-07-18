import requests

URL = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(URL)
#aqui verificamos si el request fue exitoso
if response.status_code == 200:
    print('Disponible')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', n\
        response.text)
    
    