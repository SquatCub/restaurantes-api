from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurante
from shapely.geometry import Point
import math

# Mensaje de bienvenida
def index(request):
    if request.method == "GET":
        return JsonResponse({"status": "correcto", "mensaje": "bienvenido a la api restaurantes"}, status=200, safe=False)
    else:
        return JsonResponse({"status": "error", "mensaje": "metodo no permitido"}, status=400, safe=False)

# Obtener todos los restaurantes
def restaurantes_all(request):
    if request.method == "GET":
        try:
            restaurantes = Restaurante.objects.all()
            return JsonResponse({"restaurantes": [restaurante.serialize() for restaurante in restaurantes]}, status=200, safe=False)
        except Exception:
            return JsonResponse({"status": "error", "mensaje": "recurso no encontrado"}, status=200, safe=False)
    else:
        return JsonResponse({"status": "error", "mensaje": "metodo no permitido"}, status=400, safe=False)

# Obtener restaurante individual por ID
def restaurante(request):
    if request.method == "GET":
        try:
            id_restaurante = request.GET["id"]
            restaurante = Restaurante.objects.get(id=id_restaurante)
            return JsonResponse([restaurante.serialize()], status=200, safe=False)
        except Exception:
            return JsonResponse({"status": "error", "mensaje": "recurso no encontrado"}, status=200, safe=False)
    else:
        return JsonResponse({"status": "error", "mensaje": "metodo no permitido"}, status=400, safe=False)

# Crear un nuevo restaurante
@csrf_exempt
def restaurante_create(request):
    if request.method == "POST":
        try:
            id_restaurante = request.POST["id"]
            # SI ya existe un restaurante con el ID se lanza una excepcion
            if Restaurante.objects.filter(id=id_restaurante):
                raise Exception("ya existe un restaurante con este ID")

            # Lanza una excepcion en caso de que el rating no este en el rango
            rating = request.POST["rating"]
            if int(rating) < 0 or int(rating) > 4:
                raise Exception("rating fuera de rango")
            
            name = request.POST["name"]
            site = request.POST["site"]
            mail = request.POST["mail"]
            phone = request.POST["phone"]
            street = request.POST["street"]
            city = request.POST["city"]
            state = request.POST["state"]
            lat = request.POST["lat"]
            lng = request.POST["lng"]

            nuevo_restaurante = Restaurante(id=id_restaurante, rating=rating, name=name, site=site, email=mail, phone=phone, street=street, city=city, state=state, lat=lat, lng=lng)
            nuevo_restaurante.save()
            return JsonResponse({"status": "correcto", "mensaje": "restaurante creado con exito"}, status=201, safe=False)
        except Exception as e:
            return JsonResponse({"status": "error", "mensaje": str(e)}, status=409, safe=False)
    else:
        return JsonResponse({"status": "error", "mensaje": "metodo no permitido"}, status=400, safe=False)

# Eliminar un restaurante
@csrf_exempt
def restaurante_delete(request, id_restaurante):
    if request.method == "DELETE":
        try:
            restaurante = Restaurante.objects.get(id=id_restaurante)
            restaurante.delete()
            return JsonResponse({"status": "correcto", "mensaje": "restaurante eliminado con exito"}, status=200, safe=False)
        except Exception:
            return JsonResponse({"status": "error", "mensaje": "imposible eliminar el restaurante, revise el id"}, status=409, safe=False)
    else:
        return JsonResponse({"status": "error", "mensaje": "metodo no permitido"}, status=400, safe=False)

# Actualizar datos de un restaurante
@csrf_exempt
def restaurante_update(request, id_restaurante):
    if request.method == "POST":
        try:
            restaurante = Restaurante.objects.get(id=id_restaurante)
            restaurante.rating = request.POST["rating"]
            restaurante.name = request.POST["name"]
            restaurante.site = request.POST["site"]
            restaurante.email = request.POST["mail"]
            restaurante.phone = request.POST["phone"]
            restaurante.street = request.POST["street"]
            restaurante.city = request.POST["city"]
            restaurante.state = request.POST["state"]
            restaurante.lat = request.POST["lat"]
            restaurante.lng = request.POST["lng"]
            restaurante.save()
            return JsonResponse({"status": "correcto", "mensaje": "restaurante actualizado con exito"}, status=201, safe=False)
        except Exception:
            return JsonResponse({"status": "error", "mensaje": "imposible actualizar el restaurante, revise los datos"}, status=409, safe=False)
    else:
        return JsonResponse({"status": "error", "mensaje": "metodo no permitido"}, status=400, safe=False)

# Datos estadisticos de los restaurantes en un área
def restaurantes_statistics(request):
    if request.method == "GET":
        try:
            lat = request.GET["latitude"]
            lng = request.GET["longitude"]
            rad = request.GET["radius"]
            restaurantes = Restaurante.objects.all()

            # Punto creado con las coordenadas proveidas
            point = Point(float(lat), float(lng))

            # Conversion de el radio a grados y creacion del area a verificar (No corresponde a datos reales, es un circulo con su radio y area, simulando un plano 2D)
            distance_radius = float(rad) / 111325
            circle = point.buffer(distance_radius)
            
            restaurantes_dentro = []
            count = 0
            rating_suma = 0
            # Se recorren los restaurantes para buscar cuales entran en el area
            for restaurante in restaurantes:
                pointX = float(restaurante.lat)
                pointY = float(restaurante.lng)
                point2 = Point(pointX, pointY)
                # Si estan dentro se aumenta el contador, se suma el rating y se almacenan en una lista
                if circle.contains(point2):
                    count+=1
                    rating_suma+=restaurante.rating
                    restaurantes_dentro+=[restaurante]
            # Se establece rating_promedio a cero en caso de no encontrar ninguno y evitar un error de division entre cero        
            rating_promedio = 0
            # Sumatoria para obtener la desviacion estandar
            sumatoria = 0
            # Se obtiene la desviacion
            desviacion_estandar = 0
            if count != 0:
                rating_promedio = rating_suma/count
                for restaurante in restaurantes_dentro:
                    sumatoria += math.pow((restaurante.rating - rating_promedio), 2)
                    # Se obtiene la desviacion
                    desviacion_estandar = math.sqrt(sumatoria / rating_promedio)
            
            return JsonResponse({"count": count, "avg": rating_promedio, "std": desviacion_estandar}, status=200, safe=False)
        except Exception as e:
            return JsonResponse({"status": "error", "mensaje": str(e)}, status=409, safe=False)
    else:
        return JsonResponse({"status": "error", "mensaje": "metodo no permitido"}, status=400, safe=False)