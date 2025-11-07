import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os
import paho.mqtt.client as mqtt
import sys

# === 0. Gérer l'argument éventuel ===
# Si Node-RED envoie un argument (ex: une clé aléatoire), on l'ignore ou le loggue
if len(sys.argv) > 1:
    print(f"[INFO] Argument reçu (ignoré) : {sys.argv[1]}")

# === 1. Charger le modèle ===
model_path ="C:/Users/Lenovo/Desktop/NodeRed-MobileNet-Project/plante_model_finetuned.h5"
model = load_model(model_path)

# === 2. Charger et prétraiter l’image ===
image_path = "C:/Users/Lenovo/Desktop/NodeRed-MobileNet-Project/scripts/images/s.jpg"
img = cv2.imread(image_path)
if img is None:
    print("[ERROR] Image introuvable :", image_path)
    exit(1)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_resized = cv2.resize(img_rgb, (224, 224))
img_normalized = img_resized / 255.0
img_input = np.expand_dims(img_normalized, axis=0)

# === 3. Prédiction ===
prediction = model.predict(img_input)[0][0]  # sortie sigmoid
pourcentage = prediction * 100
print(f"[INFO] Score brut : {prediction:.4f}")

# === 4. Interprétation ===
if prediction < 0.5:
    etat = "Feuille malade"
else:
    etat = "Feuille saine"

# === 5. Annoter et sauvegarder l’image ===
cv2.putText(
    img,
    f"{etat} ({pourcentage:.0f}%)",
    (10, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.2,
    (0, 255, 0),
    3
)

output_dir = "C:/Users/Lenovo/.node-red/public"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "plante_result.jpg")
cv2.imwrite(output_path, img)

# === 6. Publier via MQTT ===
try:
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.publish("etat", etat)
    client.disconnect()
except Exception as e:
    print("[ERROR] Erreur MQTT :", str(e))

# === 7. Affichage final ===
print("[OK] État détecté :", etat)
print("[OK] Image sauvegardée :", output_path)
print("[OK] Script exécuté avec succès.")
