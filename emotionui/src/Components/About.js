import React from 'react';
import './About.css'; // Optional: for styling the About section

const About = () => {
  return (
    <div className="about-container">
      <h2>About the Emotion Detection Web Application</h2>
      <p>
        Welcome to the Emotion Detection Web Application! This project is designed to classify human emotions using deep learning models, 
        specifically leveraging the power of Convolutional Neural Networks (CNNs) and ResNet architecture. 
        Our goal is to create an intuitive user interface that allows users to upload or capture images, 
        and our advanced AI model will classify the predominant emotion in the image.
      </p>

      <h3>Key Features:</h3>
      <ul>
        <li>Real-Time Emotion Detection: Capture an image directly through your webcam, and let the AI analyze it instantly.</li>
        <li>Image Upload Support: If you have an image file ready, simply upload it to see the detected emotion.</li>
        <li>High Accuracy with ResNet: Our model is built on ResNet, providing robust and accurate emotion classification results.</li>
        <li>Simple and Clean UI: Easy-to-use interface developed using React.js to ensure a seamless user experience.</li>
      </ul>

      <h3>Technology Stack:</h3>
      <ul>
        <li><strong>Backend:</strong> Python-based Flask server hosting the deep learning model, powered by TensorFlow/Keras.</li>
        <li><strong>Frontend:</strong> React.js for building an interactive and responsive UI.</li>
        <li><strong>Model Architecture:</strong> ResNet, a state-of-the-art CNN model for computer vision tasks, trained on an extensive dataset of facial expressions.</li>
      </ul>

      <p>
        Thank you for using our application! We hope this tool can help in understanding emotions better 
        and open up possibilities for further exploration in the field of AI and human-computer interaction.
      </p>
    </div>
  );
};

export default About;
