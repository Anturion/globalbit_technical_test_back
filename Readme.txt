# Prueba para Globalbit

## Back end de la prueba

Para correr el servidor debe tener instalada una version de python igual o mayor a la 3 
después se debe crear un entorno virtual para instalar las dependencias, 
para ello se pueden usar los siguientes comandos.

Para Windows:
```shell
--python3 -m venv <nombre_del_entorno>
--<nombre_del_entorno>\Scripts\activate.bat
```

Para Linux o MAC:
```shell
--python3 -m venv <nombre_del_entorno>
--source <nombre_del_entorno>/bin/activate
```

una vez hecho se usa el paquete pip para instalar las dependencias:

```shell
pip install -r requirements.txt
```

Una se termine de instalar las dependencias, solo hace falta correr el siguiente comando:

```shell
uvicorn app.main:app --reload --port 5000 
```

Con esto el servidor estará corriendo en la ruta http://127.0.0.1:5000.

Donde se encuentran los endpoints construidos con FastAPI, para mayor información, puede poner
el siguiente enlace en el navegador una vez este corriendo la instancia. http://127.0.0.1:5000/docs

Esta es la ruta a la cual el front ejecutará las peticiones.

Finalmente al correr la instancia del back end se genera una base de datos sql con el nombre app.db,
donde se guardarán los datos enviados desde el front.



