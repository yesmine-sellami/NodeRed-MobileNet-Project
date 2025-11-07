import cv2
import numpy as np
from tensorflow.keras.models import load_model

def predict_image(image_path, model_path):
    """Retourne l'état et le pourcentage pour une image"""
    model = load_model(model_path)

    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image introuvable : {image_path}")

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (224, 224))
    img_normalized = img_resized / 255.0
    img_input = np.expand_dims(img_normalized, axis=0)

    prediction = model.predict(img_input)[0][0]  # sortie sigmoid
    pourcentage = prediction * 100

    etat = "Feuille malade" if prediction < 0.5 else "Feuille saine"
    return etat, pourcentage
if __name__ == "__main__":
    model_path = "C:/Users/Lenovo/Desktop/NodeRed-MobileNet-Project/plante_model_finetuned.h5"
    image_path = "C:/Users/Lenovo/Desktop/NodeRed-MobileNet-Project/scripts/images/s.jpg"

    etat, pourcentage = predict_image(image_path, model_path)
    print(f"Image : {image_path} -> Etat : {etat}, Pourcentage : {pourcentage:.2f}%")
