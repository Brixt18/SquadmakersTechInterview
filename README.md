# Tech Interview

Este proyecto es una API construida en [Flask](https://flask.palletsprojects.com/en/2.1.x/) para la entrevista ténica de Squadmakers


## Instalación

Clonar el proyecto como normalmente clonas un proyecto de github.

```
$ git clone https://github.com/Brixt18/SquadmakersTechInterview
```
O descargando el archivo .zip del mismo.

Una vez clonado el proyecto, **Crear** dentro de la carpeta `app/configuration` un archivo `.env` con las variables de entorno.
```
SECRET_KEY="12345"
CONF_MODE="Local"
```

Debería quedar un arbol así:
```bash
└───app
    ├───api
    │   └───...
    ├───config
    │   └───.env
    └───...
```


## Requisitos
* [Python >= 3.10.8](https://www.python.org/downloads/release/python-3108/)

## Dependencias
Instalar usando pip
```
$ pip install -r requirements.txt
```

## Cómo Usar

### Inicializar
Una vez instaladas todas las dependencias, ejecutar el archivo `run.py`
```
$ python run.py
```
Y la aplicación comenzará a ejectuar en entorno Local con el puerto 5000 (`localhost:5000`).

### Configuración
Se pueden cambiar las configuraciones del proyecto desde `app/configuration/configuration.py`.
Se puede cambiar el puerto de ejecución cambiando (o agregando) `SERVER_NAME=HOST:PORT` en el archivo `.env`


# Endpoints

## Chistes

- ### GET /api/ : obtener un chiste aleatório
- ### GET /api/?param=dad : obtener un chiste desde icanhazdadjoke
- ### GET /api/?param=chuck : obtener un chiste desde chuck norris api
Respuesta:
```json
{
    "data": "..."
}
```
- ### POST /api/ : guarda un chiste en la base de datos local
- ### PATCH /api/?number={ID} : actualizar un chiste guardado en la base de datos local
JSON Parámetros:
```json
{
    "joke": "..."
}
```
- ### DELETE /api/?number={ID} : eliminar un chiste de la base de datos local

## Matemáticas
- ### GET /api/math/least-common-multiple/?numbers=1,2,4 : obtener el mínimo común múltiplo
- ### GET /api/math/add-one/?number=4 : obtener ese número +1
Respuesta:
```json
{
    "data": "..."
}
```

## Utilizar curl
```bash
curl -v -X GET http://localhost:5000/api/ #200 chiste
curl -v -X GET http://localhost:5000/api/?param=dad #200 chiste dad
curl -v -X GET http://localhost:5000/api/?param=chuck #200 chiste cuck
curl -v -X GET http://localhost:5000/api/?param=error #400 bad param error
curl -v -X POST -d "{\"joke\": \"This is a joke\"}" -H "Content-Type: application/json" http://localhost:5000/api/ #201 Header Location: url
curl -v -X PATCH -d "{\"joke\": \"This is a joke\"}" -H "Content-Type: application/json" http://localhost:5000/api/?number={id} #204 NO CONTENT
curl -v -X DELETE http://localhost:5000/api/?number={id} #204 NO CONTENT

# MATH API
curl -v -X GET http://localhost:5000/api/math/least-common-multiple/?numbers=1,2,4 #200 {data: 4}
curl -v -X GET http://localhost:5000/api/math/add-one/?number=4 #200 {data: 5}
```