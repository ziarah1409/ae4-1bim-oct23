# Importar el MongoClient
from conection_mongo import engine

# Crear una instancia de MongoClient

# Seleccionar la base de datos y la colección
db = engine["Matriculas"]
collection = db["RegistroEstudiantes"]

# Consultar todos los registros en la colección
resultados = collection.find()

# Imprimir los resultados
for resultado in resultados:
     print(resultado)

collection2 = db["RegistroVehiculos"]

# Consultar todos los registros en la colección
resultados2 = collection2.find()

# Imprimir los resultados
for resultadovehiculos in resultados2:
    print(resultadovehiculos)