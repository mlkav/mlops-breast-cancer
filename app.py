from flask import Flask, request, render_template, jsonify
import requests
import json
import base64
import tensorflow as tf

app = Flask(__name__)

# Endpoint model
MODEL_URL = "https://mlops-bc-mkavaldo.up.railway.app/v1/models/bc-model:predict"

def prepare_json(inputs: dict) -> str:
    features = {k: tf.train.Feature(float_list=tf.train.FloatList(value=[float(v)])) 
                for k, v in inputs.items()}
    example = tf.train.Example(features=tf.train.Features(feature=features)).SerializeToString()
    encoded_example = base64.b64encode(example).decode()
    return json.dumps({"signature_name": "serving_default", "instances": [{"examples": {"b64": encoded_example}}]})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract feature values from form
        features = {
            'radius_mean': request.form['radius_mean'],
            'texture_mean': request.form['texture_mean'],
            'perimeter_mean': request.form['perimeter_mean'],
            'area_mean': request.form['area_mean'],
            'smoothness_mean': request.form['smoothness_mean'],
            'compactness_mean': request.form['compactness_mean'],
            'concavity_mean': request.form['concavity_mean'],
            'concave_points_mean': request.form['concave_points_mean'],
            'symmetry_mean': request.form['symmetry_mean'],
            'fractal_dimension_mean': request.form['fractal_dimension_mean'],
            'radius_se': request.form['radius_se'],
            'texture_se': request.form['texture_se'],
            'perimeter_se': request.form['perimeter_se'],
            'area_se': request.form['area_se'],
            'smoothness_se': request.form['smoothness_se'],
            'compactness_se': request.form['compactness_se'],
            'concavity_se': request.form['concavity_se'],
            'concave_points_se': request.form['concave_points_se'],
            'symmetry_se': request.form['symmetry_se'],
            'fractal_dimension_se': request.form['fractal_dimension_se'],
            'radius_worst': request.form['radius_worst'],
            'texture_worst': request.form['texture_worst'],
            'perimeter_worst': request.form['perimeter_worst'],
            'area_worst': request.form['area_worst'],
            'smoothness_worst': request.form['smoothness_worst'],
            'compactness_worst': request.form['compactness_worst'],
            'concavity_worst': request.form['concavity_worst'],
            'concave_points_worst': request.form['concave_points_worst'],
            'symmetry_worst': request.form['symmetry_worst'],
            'fractal_dimension_worst': request.form['fractal_dimension_worst']
        }
        
        # Prepare JSON payload
        payload = prepare_json(features)
        
        # Send request to model endpoint
        response = requests.post(MODEL_URL, data=payload, headers={"Content-Type": "application/json"})
        
        # Process the response
        result = response.json()
        prediction = result.get("predictions", [])
        if prediction:
            diagnosis = "❗ Kanker Ganas (Malignant)." if prediction[0][0] >= 0.5 else "⚠️ Kanker Jinak (Benign)."
        else:
            diagnosis = "Error: Prediksi tidak diketahui."
        
        return render_template('index.html', diagnosis=diagnosis)
    
    return render_template('index.html', diagnosis=None)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
