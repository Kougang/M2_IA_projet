import cv2
import numpy as np
import pytesseract

def extract_data(image_path):
    # Charger l'image en niveau de gris
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Appliquer le filtre de détection des bordures
    edges = cv2.Canny(image, 50, 150)

    # Utiliser la détection de contours pour trouver les cellules du tableau
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Créer une liste pour stocker les valeurs des cellules
    cell_values = []

    # Parcourir les contours et extraire les valeurs des cellules
    for contour in contours:
        # Calculer le rectangle englobant pour la cellule
        x, y, w, h = cv2.boundingRect(contour)

        # Extraire la partie de l'image correspondant à la cellule
        cell_image = image[y:y+h, x:x+w]

        # Utiliser la fonction de seuillage pour convertir l'image en binaire
        _, thresholded_image = cv2.threshold(cell_image, 127, 255, cv2.THRESH_BINARY_INV)

        # Utiliser la fonction de reconversion en chiffres pour extraire la valeur de la cellule
        value = pytesseract.image_to_string(thresholded_image, config='--psm 10')

        # Ajouter la valeur de la cellule à la liste
        cell_values.append(value)

    return cell_values


image_path = 'Capturepro.PNG'
data = extract_data(image_path)
print(data)