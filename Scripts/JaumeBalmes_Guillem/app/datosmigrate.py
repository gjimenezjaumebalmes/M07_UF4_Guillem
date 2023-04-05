import os
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JaumeBalmes_Guillem.settings.py")
django.setup()

from models import Alumno, Profesor

# Ruta del archivo JSON con los datos de los alumnos y profesores
json_file = './data/datos.json'

# Abrir el archivo JSON y leer los datos
with open(json_file) as f:
    data = json.load(f)

# Iterar sobre los datos y guardarlos en la base de datos
# Crear instancias de profesor y alumno a partir de los datos del archivo JSON
for profesor_data in data['profesorado']:
    profesor = Profesor.objects.create(
        id=profesor_data['id'],
        nombre=profesor_data['nombre'],
        asignatura=profesor_data['asignatura'],
        email=profesor_data['email'],
        curso=profesor_data['curso']
    )

for alumno_data in data['alumnado']:
    alumno = Alumno.objects.create(
        id=alumno_data['id'],
        nombre=alumno_data['nombre'],
        curso=alumno_data['curso'],
        email=alumno_data['email']
    )