# Emotion Detection Web Application

This project is a web-based application that detects and classifies human emotions from facial images. The core of the application is a Convolutional Neural Network (CNN) model based on the ResNet architecture, which has been trained to recognize a variety of emotions with high accuracy. The web application has been built using React.js for the frontend and a Fastapi server to host the deep learning model.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)

## Features
- **Real-time emotion detection**: Capture an image using the webcam and classify emotions instantly.
- **Image upload functionality**: Upload any facial image to detect emotions.
- **Highly accurate model**: The application uses a ResNet model, which outperforms traditional CNN models in emotion classification tasks.
- **User-friendly UI**: The web interface is designed with React.js, providing a clean and responsive user experience.

## Technology Stack
- **Frontend**: React.js
- **Backend**: Fastapi (Python)
- **Deep Learning Model**:Lenet, ResNet (TensorFlow/Keras)
- **Webcam Integration**: react-webcam

## Installation

### Prerequisites
- Node.js and npm
- Python 3.x
- Fastapi
- TensorFlow/Keras

### Backend Setup
1. Clone the repository and navigate to the `backend` folder.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
