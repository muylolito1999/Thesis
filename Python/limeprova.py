from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from lime.lime_tabular import LimeTabularExplainer

# Carica il dataset breast cancer
data = load_breast_cancer()
X = data.data
y = data.target
feature_names = data.feature_names

# Dividi il dataset in training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Addestra un modello di RandomForest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Crea un oggetto LimeTabularExplainer
explainer = LimeTabularExplainer(X_train, feature_names=feature_names, class_names=data.target_names, discretize_continuous=True)

# Seleziona una singola istanza di test da spiegare
# Puoi cambiare l'indice per selezionare un'altra istanza
for i in range(10):
 instance = X_test[i].reshape(1, -1)
true_class = y_test[i]
exp = explainer.explain_instance(instance[0], model.predict_proba, num_features=30)
print(f"Spiegazione per l'istanza con indice {i} (classe vera: {true_class}):")
print(exp)
fig = exp.as_pyplot_figure()
plt.tight_layout()
plt.show()

# Genera una spiegazione per l'istanza selezionata


# Stampa la spiegazione
print(f"Spiegazione per l'istanza con indice {i} (classe vera: {true_class}):")
print(exp)

# Visualizza la spiegazione in formato leggibile
exp.show_in_notebook(show_table=True, show_all=False)

# (Facoltativo) Visualizza la spiegazione in un browser
