import requests
import csv
import polyline

# Tu clave de API de Google Maps
API_KEY = 'TU_CLAVE_DE_API'

# Puntos de origen, destino y waypoints (coordenadas de latitud y longitud)
origin = '37.774929,-122.419416'  # San Francisco, CA
destination = '34.052234,-118.243685'  # Los Angeles, CA
waypoints = [
  '-39.814916, -73.249028',
  #"#name": "Barrio Flotante"

  '-39.832, -73.26625',
 # "name": "Torobayo"

  '-39.832056, -73.252806',
#  "name": "Uach Miraflores"
  '-39.821361,-73.250722',
#  "name": "San Sebastián"
    '-39.814167,-73.2505',
 # "name": "Los Castaños"
   '-39.810972, -73.249028',
#  "name": "UACH Facea"
    ' -39.809194, -73.242389',
#  "name": "Carampangue"
    '-39.813805,-73.235389',
#  "name": "Terminal Buses"
    '-39.809324,-73.20962'
  #"name": "Collico"
]





# Formatear los waypoints para la URL de la solicitud
waypoints_str = '|'.join(waypoints)

# URL de la API de Directions con waypoints
url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&waypoints={waypoints_str}&key={API_KEY}'

# Solicitud a la API de Directions
response = requests.get(url)
data = response.json()

# Verificar que la solicitud fue exitosa
if data['status'] == 'OK':
    # Extraer los puntos de la ruta
    route = data['routes'][0]
    overview_polyline = route['overview_polyline']['points']
    
    # Decodificar la polilínea
    points = polyline.decode(overview_polyline)
    
    # Guardar los puntos en un archivo CSV
    with open('route_points.csv', 'w', newline='') as csvfile:
        fieldnames = ['latitude', 'longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for point in points:
            writer.writerow({'latitude': point[0], 'longitude': point[1]})

    # Guardar los puntos en un archivo TXT
    with open('route_points.txt', 'w') as txtfile:
        for point in points:
            txtfile.write(f'{point[0]}, {point[1]}\n')

    print('Los datos de la ruta han sido guardados en route_points.csv y route_points.txt')
else:
    print('Error al obtener la ruta:', data['status'])
    
print("hola esta es la feature2")