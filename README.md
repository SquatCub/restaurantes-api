# API Rest Restaurantes - Hecha con Django

El enlace de la API lo puede encontrar [aquí](https://sleepy-inlet-51459.herokuapp.com/), el cual desplegara un mensaje de bienvenida.

Esta API le permite acceder a datos de hoteles ficticios, con el fin de realizar operaciones CRUD en ella, con manejo de excepciones en caso de tenerlas.
A continuación se muestra lo que es posible realizar, cabe recalcar que no se necesita de ninguna llave de acceso, ya que se configuro de tal manera que no necesite autenticación:

## Insertar un nuevo restaurante
Desde el enlace https://sleepy-inlet-51459.herokuapp.com/restaurante/crear, es posible insertar un nuevo restaurante desde un formulario utilizando el método HTTP POST con los siguientes parámetros, en caso de no enviar el id, la API arrojara una excepción, tambien en caso de que el rating no esté en el rango, es necesario que se manden todas las llaves por POST, aunque sus valores sean vacíos:
1. id
2. rating (Rango de 0 a 4)
3. name
4. site
5. mail
6. phone
7. street
8. city
9. state
10. lat
11. lng

## Leer un restaurante
Desde https://sleepy-inlet-51459.herokuapp.com/restaurante?id={id_restaurante} con el método GET es posible obtener los datos del restaurante en caso de obtenerlo, en caso contrario mandara un mensaje de que no ha sido posible encontrar un restaurante con el ID propuesto.
## Leer todos los restaurantes
Sin necesidad de mandar colocar ningún parametro, y accediendo a https://sleepy-inlet-51459.herokuapp.com/restaurantes con el método GET, es posible obtener un listado de todos los restaurantes existentes en la API.

## Actualizar los datos de un restaurante
Para actualizar los datos de un restaurante es necesario acceder a https://sleepy-inlet-51459.herokuapp.com/restaurante/actualizar por medio del método POST con los siguientes datos, similar a la función para crear, es necesario que se manden todas las llaves por POST, aunque sus valores sean vacíos:
1. id
2. rating (Rango de 0 a 4)
3. name
4. site
5. mail
6. phone
7. street
8. city
9. state
10. lat
11. lng

## Eliminar un restaurante
Para poder eliminar un restaurante está https://sleepy-inlet-51459.herokuapp.com/restaurante/borrar/{id_restaurante}, donde se le pasa de parámetro el id del restaurante para hacer la eliminación del restaurante. Es necesario que para enviar se utilice el método DELETE.

## Obtener estadísticas
Esta función devuelve un listado de todos los restaurantes que se encuentran dentro de un radio proporcionado en metros, enviándole la latitud y longitud de donde queremos se posicione el centro del círculo. Para acceder es necesario acceder a https://sleepy-inlet-51459.herokuapp.com/restaurantes/statistics?latitude={latitud}&longitude={longitud}&radius={radio} por el método GET.
Esto se logra mediante la libreria Shapely, que crea un circulo en un plano, donde el se encuentra en las coordenadas que se le provean, y de aqui se hace una conversion del radio en metros a grados para crear el radio. Luego de esto se crean puntos individuales de cada restaurante, con sus propias coordenadas de latitud y longitud, y en caso de que estas se encuentren en el rango del area del circulo, se comienzan a realizar las operaciones para obtener la cuenta, el promedio del rating y la desviacion estandar del rating.


# Estructura de la base de datos (Hecha en Postgres con el ORM de Django)
Restaurants ( id TEXT PRIMARY KEY, -- Unique Identifier of Restaurant
            rating INTEGER, -- Number between 0 and 4
            name TEXT, -- Name of the restaurant
            site TEXT, -- Url of the restaurant
            email TEXT,
            phone TEXT,
            street TEXT,
            city TEXT,
            state TEXT,
            lat FLOAT, -- Latitude
            lng FLOAT) -- Longitude)
 
# Dependecias utilizadas
1. Python 3
2. Django
3. Django-heroku (para deploy)
4. gunicorn
5. Shapely


# Instrucciones para correr localmente

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
