import requests
import json


def request_data():
	
	#El id dado en el test es 179571326 
	user_id = int(input("Ingrese el ID del usuario que desea buscar: "))
	request_data = requests.get(f"https://api.mercadolibre.com/sites/MLA//search?seller_id={user_id}").json()
	
	
	request_data = request_data['results']
	
	
	try:
		with open(f"{user_id}.log", "w+") as file:
		
			file.write("ID + --- + TITLE + --- + CATEGORY_ID + --- + NAME\n\n")
		
			for key in request_data:
				id = key["id"]
				title = key["title"]
				category_id = key["category_id"]
				name = key["domain_id"]
			
				file.writelines(f"{id} +  ---  + {title} +  ---  + {category_id} +  ---  + {name}\n")
			
			print("Archivo log guardado exitosamente")
			
	except IOError:
		print("Hubo un error al procesar el archivo")

request_data()
