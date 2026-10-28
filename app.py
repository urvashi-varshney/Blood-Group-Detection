import os
import time # For simulating delay
import numpy as np
import cv2
import tensorflow as tf
from flask import Flask, render_template, request, redirect, url_for, flash, session
from pathlib import Path


# Create the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key' # Required for flashing messages


# Define the model path and dataset path
MODEL_PATH = "blood_group_model.keras"
DATASET_PATH = " " 


# Blood groups for prediction
blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+']


# Simple storage to hold registered users for demonstration purposes
users = {} # Dictionary to store username:password pairs


# Load the trained model
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


# Predict blood group
def predict_blood_group(model, image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    return np.argmax(predictions)


@app.route('/')
def home():
    return render_template('index.html') # Implement your login page


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']


    # Check if the username already exists
    if username in users:
        flash("Username already exists. Please choose a different one.")
        return redirect(url_for('home'))


    # Add user to the dictionary for demonstration
    users[username] = password


    flash("Registration successful! You can log in now.") # Flash message
    return redirect(url_for('home'))


@app.route('/validate_login', methods=['POST'])
def validate_login():
    username = request.form['username']
    password = request.form['password']


    # Check credentials against registered users
    if username in users and users[username] == password:
        session['username'] = username
        flash("You are logged in!") # Flash message only on successful login
        return redirect(url_for('task_manager')) # Redirect to the task manager after login
    else:
        flash("Invalid credentials. Please try again.")
        return redirect(url_for('home'))


@app.route('/task_manager')
def task_manager():
    if 'username' not in session:
        flash("Please log in first!") # Flash message for not logged in
        return redirect(url_for('home'))
    return render_template('task_manager.html') # Render task manager page


@app.route('/upload')
def upload():
    if 'username' not in session:
        flash("Please log in first!") # Flash message for not logged in
        return redirect(url_for('home'))
    return render_template('upload.html') # Render upload page


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        flash("No file part")
        return redirect(url_for('upload'))


    file = request.files['file']
    
    if file.filename == '':
        flash("No selected file")
        return redirect(url_for('upload'))


    os.makedirs('uploads', exist_ok=True)
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)


    try:
        model = load_model()
        time.sleep(3) # Simulate loading time of 3 seconds
        # Predict the blood group
        blood_group_index = predict_blood_group(model, file_path)


        blood_group = blood_groups[blood_group_index]
        return render_template('result.html', blood_group=blood_group)


    except Exception as e:
        flash(f"Error: {str(e)}") # Flash any errors
        return redirect(url_for('upload'))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You've been logged out.") # Flash message for logout
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)