# se importa el engine
from conection_mongo import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
db = engine["Matriculas"]
collection = db["RegistroEstudiantes"]
# Se crea la una entidad llamada Autor, que hereda
# de Base


data_01 ={"Nombre":"Ziarah", "Apellido":"Apolo","Curso":"Tranformacion Digital de Empresas", "Universidad":"UTPL"}
collection.insert_one(data_01)

collection2 = db ["RegistroVehiculos"]
data_02 ={ "Marca":"Toyota","Modelo":2023,"Motor":"2.9", "Color":"Gris"}
collection2.insert_one(data_02)
