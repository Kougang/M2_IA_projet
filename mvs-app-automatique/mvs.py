import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Définition d'un ensemble de données linéairement séparables
X = np.array([[1, 2],[1, 3],[1, 4],[1, 5], [2, 3], [2, 5], [3.7, 5],[2, 4],[2, 7],[3, 7],[3, 6],[6, 2], [6, 4], [6, 6], [8, 8], [7, 8], [6, 8], [6, 7], [7, 5], [7, 3]])
y = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

# X = np.array([[1, 1],[-1, 1],[-1, -1],[1, -1], [2, 0], [0, 2], [-2, 0],[0, -2]])
# y = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

# Entraînement du modèle SVM
clf = svm.SVC(kernel='linear')
clf.fit(X, y)

# Coefficients du vecteur w et le biais b
w = clf.coef_[0]
b = clf.intercept_[0]

# Calcul de la marge
marge = 1 / np.linalg.norm(w)

# Affichage des données et de la séparation linéaire
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Création de la grille pour évaluer le modèle
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50),
                     np.linspace(ylim[0], ylim[1], 50))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])

# Affichage de la séparation et des marges
Z = Z.reshape(xx.shape)
plt.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
            linestyles=['--', '-', '--'])

# Affichage du vecteur w
plt.quiver(0, 0, w[0], w[1], scale=1, scale_units='xy')
plt.text(w[0], w[1], ' w', fontsize=12, color='r')

# Affichage de la marge maximale
plt.text(w[0] / 2, w[1] / 2, 'Marge = {:.2f}'.format(marge),
         horizontalalignment='center', verticalalignment='center',
         backgroundcolor='white', alpha=0.8)

plt.show()
