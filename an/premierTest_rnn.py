import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

# b357U78QMqA9u
# Supposez que X_train et y_train sont vos données d'entraînement
# où X_train est une liste de vecteurs de caractéristiques et y_train est une liste d'étiquettes (0, 1, 2, 3).

# Remplacez 'chemin/vers/votre/fichier.csv' par le chemin d'accès réel de votre fichier CSV
chemin_fichier_csv = 'echantillonGeneral.csv'

#vecteur de test
vecteur_test = np.array([11,11,11,14,10,10,10,10,10,10,10])
classe_test = np.array([3,2,0,1])

# Charger le fichier CSV dans un DataFrame pandas
donnees = pd.read_csv(chemin_fichier_csv)

# X = donnees[['math','physique','informatique','chimie','philosophie','svt','hist','geo',
#              'ecm','anglais','sport']]
# y = donnees['formation']

X = donnees.drop('formation', axis=1) #supprimer le target dans notre jeu de donnee
y = donnees['formation']

nombre_caracteristique = X.shape[1] 
print(nombre_caracteristique) #nombre de colonnes dans le dataframe

# Divisez les données en ensembles d'entraînement et de validation
Xtrain, X_val, ytrain, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
 
#random_state=42:  permet la separation aleatoire des donnees


# Convertissez vos données en tableaux NumPy pour être compatibles avec TensorFlow
X_train = np.array(Xtrain)
y_train = np.array(ytrain)

# Définissez le modèle sequentiel
model = models.Sequential()

# Ajoutez une couche d'entrée
model.add(layers.InputLayer(input_shape=(nombre_caracteristique)))

# Ajoutez des couches cachées avec activation Leaky ReLU
model.add(layers.Dense(64, activation=tf.nn.leaky_relu))
model.add(layers.Dense(32, activation=tf.nn.leaky_relu))

# Couche de sortie avec une activation softmax pour la classification multi-classe
model.add(layers.Dense(4, activation='softmax'))

# Compilez le modèle avec une fonction de perte appropriée pour la classification multi-classe
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entraînez le modèle
model.fit(X_train, y_train, epochs=200, validation_data=(X_val, y_val))


vecteur_test = vecteur_test.reshape(1, -1)  # Si vous avez une seule instance

probabilites_predictions_test = model.predict(vecteur_test)

# Affichez les prédictions
print("Prédictions:", probabilites_predictions_test)



    # Obtenez les indices triés des probabilités (du plus petit au plus grand)
indices_tries = np.argsort(probabilites_predictions_test)

    # Renversez les indices pour les avoir dans l'ordre décroissant (du plus grand au plus petit)
indices_tries_decroissant = indices_tries[:, ::-1]

    #tableau contenant les classes predites:
tableau_classe_predite = []

    # Affichez les classes et les probabilités correspondantes
for i in range(len(indices_tries_decroissant[0])):
    classe = indices_tries_decroissant[0][i]
    tableau_classe_predite.append(classe)
    probabilite = probabilites_predictions_test[0][classe]
    print(f"Classe {classe}: Probabilité {probabilite}")


print("les classes predites:", tableau_classe_predite)

    # Obtenez l'indice de la classe avec la probabilité maximale
classe_predite = np.argmax(probabilites_predictions_test)

    # Affichez la classe prédite
print("Classe prédite:", classe_predite)

#     # Calculez la précision en comparant les prédictions aux étiquettes de validation
# precision = accuracy_score(classe_test, tableau_classe_predite)

# print(f"Précision du modèle : {precision}")