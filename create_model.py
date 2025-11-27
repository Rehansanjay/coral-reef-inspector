import tensorflow as tf
from tensorflow.keras import layers, models
import os
import numpy as np

def create_dummy_model():
    print("🧠 Initializing Neural Network Construction...")

    # 1. Define the Architecture (The "Shape" of the brain)
    # We use a simple CNN (Convolutional Neural Network)
    model = models.Sequential([
        # Input Layer: Expects images 128x128 pixels with 3 colors (RGB)
        layers.Input(shape=(128, 128, 3)),
        
        # Convolutional Layer (Finds edges and patterns)
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Second Convolutional Layer
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        
        # Flatten (Turn grid into a line of numbers)
        layers.Flatten(),
        
        # Dense Layer (Decision making)
        layers.Dense(64, activation='relu'),
        
        # Output Layer: 1 neuron. 
        # < 0.5 = Bleached, > 0.5 = Healthy
        layers.Dense(1, activation='sigmoid')
    ])

    # 2. Compile the model
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # 3. Create 'model' folder if it doesn't exist
    save_path = os.path.join(os.getcwd(), 'model')
    os.makedirs(save_path, exist_ok=True)
    
    # 4. Save the model file
    full_path = os.path.join(save_path, 'coral_reef_health_classifier.h5')
    model.save(full_path)
    
    print(f"✅ SUCCESS! Model saved at: {full_path}")
    print("⚠️  NOTE: This is an untrained 'blank' model. It will run, but predictions will be random until trained on real data.")

if __name__ == "__main__":
    create_dummy_model()