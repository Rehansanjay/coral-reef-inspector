import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Define path dynamically
MODEL_PATH = os.path.join(os.getcwd(), "model", "coral_reef_health_classifier.h5")
model = None

# Load model safely
if os.path.exists(MODEL_PATH):
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
else:
    print(f"⚠️ Warning: Model not found at {MODEL_PATH}")

def classify_image(img_path):
    if model is None:
        # Fallback for testing UI without model
        return "Model Missing", 0.0

    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)[0][0]
    confidence = float(prediction)
    
    # 0 = Bleached, 1 = Healthy
    predicted_class = "Healthy" if confidence > 0.5 else "Bleached"
    
    # Adjust confidence display
    display_confidence = confidence if confidence > 0.5 else 1 - confidence

    return predicted_class, display_confidence
