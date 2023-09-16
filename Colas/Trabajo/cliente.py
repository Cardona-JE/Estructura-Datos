import requests
from faker import Faker



url = 'https://humble-guide-7v7xjpwqxp9hjww-8000.app.github.dev'


faker = Faker()


def generar_elemento():
    nombre = faker.first_name()
    productos = [faker.word() for _ in range(2)]
    return {
        "nombre": nombre,
        "productos": productos
    }


for _ in range(10):
    elemento_a_encolar = generar_elemento()
    response = requests.post(f'{url}/encolar', json=elemento_a_encolar)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Elemento encolado exitosamente: {data}")
    else:
        print(f'Error en POST a /encolar: {response.status_code}')

