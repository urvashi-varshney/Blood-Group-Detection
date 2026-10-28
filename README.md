# 🩸 Blood Group Detection Using Fingerprints

## 📌 Project Overview
Blood Group Detection Using Fingerprints is a Python-based project that aims to predict a person's blood group from fingerprint images using Machine Learning and Deep Learning techniques. The project uses image processing and a Convolutional Neural Network (CNN) model to analyze fingerprint images and predict one of the supported blood group categories.

This project is developed for educational and research purposes to explore the application of Artificial Intelligence in biometric image analysis.

## 🎯 Objectives
- To explore fingerprint image analysis using Python.
- To develop a deep learning model for blood group prediction.
- To build a simple web interface for uploading fingerprint images.
- To display the model's predicted result to the user.
- To understand the use of Flask, TensorFlow, and OpenCV in an AI-based application.

## ✨ Features
- User registration and login interface.
- Fingerprint image upload functionality.
- Image preprocessing using OpenCV.
- Deep learning model integration using TensorFlow/Keras.
- Prediction result display through a web interface.
- Model training using an EfficientNetB0-based architecture.

## 🛠️ Technologies Used
- **Programming Language:** Python
- **Web Framework:** Flask
- **Deep Learning:** TensorFlow / Keras
- **Image Processing:** OpenCV
- **Model Architecture:** EfficientNetB0-based CNN
- **Frontend:** HTML and CSS
- **Development Environment:** Visual Studio Code

## 📂 Project Structure

```text
Blood-Group-Detection/
│
├── 📂templates
     ├── index.html
     ├── result.html
     ├── task_manager.html
     ├── upload.html
├── 📂uploads
├── app.py
├── requirements.txt
├── main.py
└── README.md
```

**Note:** Flask HTML templates should be placed inside a folder named `templates/`. The model file and dataset must also be available at the paths configured in the Python code. Adjust this structure to match your actual repository.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Urvashi-Varshney/Blood-Group-Detection
```

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

Install the required libraries:

```bash
pip install flask tensorflow opencv-python numpy pillow
```

If a `requirements.txt` file is available, use:

```bash
pip install -r requirements.txt
```

### Step 5: Configure the Model and Dataset

Place the trained model file in the location expected by `app.py`. If you want to train the model, configure the dataset path in `main.py` to match your computer.

### Step 6: Run the Application

Start the Flask web application:

```bash
python app.py
```

Open the local URL shown in your terminal, usually:

```text
http://127.0.0.1:5000/
```

The application will run only after its required dependencies, templates, model file, and other configurations are set up correctly.

## 🔍 How It Works
1. The user opens the web application.
2. The user uploads a fingerprint image.
3. The application preprocesses the image and resizes it to the required dimensions.
4. The trained deep learning model analyzes the image.
5. The application displays the predicted blood group category.

## 🧪 Model Information
The training script uses an EfficientNetB0-based deep learning architecture to learn patterns from fingerprint images.

The training code lists these eight blood group classes:

- A+
- A-
- B+
- B-
- AB+
- AB-
- O+
- O-

**Important:** The class labels in the training script and web application must match. Check the label lists in `main.py` and `app.py` before running predictions.

## 🔮 Future Improvements
- Improve the quality and diversity of the dataset.
- Evaluate the model using suitable performance metrics.
- Add input validation and secure file-upload handling.
- Improve the user interface and error messages.
- Store user accounts securely using a database.
- Deploy the application to a suitable hosting platform.

## 🔐 Security Considerations
- Never upload passwords, API keys, or other secrets to GitHub.
- Use secure password hashing instead of storing plain-text passwords.
- Configure a strong secret key using environment variables.
- Disable Flask debug mode in production.
- Validate uploaded files before processing them.
- Avoid uploading private or sensitive fingerprint datasets without proper permission.

## ⚠️ Disclaimer
This project is intended for educational and research purposes only. Fingerprint-based blood group prediction is not established as a clinically reliable method for determining blood type. The predictions must not be used for medical diagnosis, blood transfusion, or treatment decisions. Blood type should be confirmed through validated laboratory testing.

## 👩‍💻 Author
**Project:** Blood Group Detection Using Fingerprints  
**Language:** Python  
**Domain:** Artificial Intelligence, Machine Learning, and Image Processing

## ⭐ Acknowledgements
This project was developed as a learning exercise to explore deep learning, fingerprint image processing, and web application development using Python.
