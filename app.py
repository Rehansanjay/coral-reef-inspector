from flask import Flask, request, render_template, jsonify
import os
from coral_predict import classify_image
# We import database safely to prevent crash if file is missing
try:
    from database import save_prediction
except ImportError:
    save_prediction = None

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = "static/uploads"
try:
    os.makedirs(UPLOAD_FOLDER)
except FileExistsError:
    pass # If it exists, just ignore the error and keep going

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    # 1. Validation
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # 2. Save Image
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)
    
    # 3. Get User Data
    name = request.form.get("name", "Anonymous")
    country = request.form.get("country", "Unknown")
    temperature = request.form.get("temperature", "25")

    # 4. Predict
    try:
        prediction, confidence = classify_image(image_path)
        
        # 5. Database Save (Optional - wont crash if DB is off)
        db_status = "Skipped"
        if save_prediction:
            try:
                save_prediction(image_path, prediction, confidence, name, country, temperature)
                db_status = "Saved"
            except Exception as e:
                db_status = "DB Offline"

        return jsonify({
            "status": "success",
            "prediction": prediction,
            "confidence": confidence,
            "image_url": image_path,
            "db_status": db_status
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)