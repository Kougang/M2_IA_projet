import requests

# Remplacez 'votre_cle_api' par votre propre clé d'API OCR.space
api_key = 'K82227944388957'

# Spécifiez l'URL de l'API OCR.space
ocr_url = 'https://api.ocr.space/parse/image'

# Spécifiez le nom du fichier image que vous souhaitez analyser
file_name = 'Capturepro.PNG'

# Paramètres de la requête
payload = {
    'apikey': api_key,
    'language': 'eng',  # Langue de l'OCR (anglais ici, changez selon vos besoins)
}

# Envoyez la requête POST à l'API OCR.space pour l'analyse de l'image
with open(file_name, 'rb') as image_file:
    response = requests.post(ocr_url, files={'file': image_file}, data=payload)

# Parsez la réponse JSON pour obtenir le texte extrait
result = response.json()
# if result['IsErroredOnProcessing']:
#     print("Erreur lors du traitement de l'image.")
# else:
# extracted_text = result['ParsedResults'][0]['ParsedText']
print(result )
