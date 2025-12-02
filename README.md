# Coral Reef Health Classifier (v1.0) 🪸

> **A web-based tool for analyzing coral reef images to detect bleaching events using Deep Learning.**

![Project Status](https://img.shields.io/badge/Status-Stable-green)
![Tech Stack](https://img.shields.io/badge/Stack-PHP_|_Python_|_MySQL_|_TensorFlow-blue)

## 📖 Project Overview

This project provides a simple, user-friendly web interface that allows users to upload images of coral reefs. The system processes these images using a Convolutional Neural Network (CNN) to classify the coral's health status.

**Core Functionality:**
1.  **Image Upload:** Users upload high-resolution images via the web interface.
2.  **Processing:** The backend passes the image to a pre-trained Python machine learning model.
3.  **Classification:** The model determines if the coral is **Healthy** or **Bleached**.
4.  **Data Storage:** The image path and analysis results are stored in a MySQL database for record-keeping.

---

## ✨ Features

* **Drag-and-Drop Interface:** Simple UI for easy image uploading.
* **Automated Analysis:** Instant classification using a `.h5` Tensorflow model.
* **Database Integration:** Automatically logs every upload and its result into `phpMyAdmin`.
* **Visual Feedback:** Displays the uploaded image alongside its health score (Confidence %).

---

## 🛠️ Deployment Requirements

To run this webpage on a local machine or server, you need the following:

### 1. Web Server Environment (XAMPP/WAMP/LAMP)
* **Apache Server** (to serve the HTML/PHP files).
* **MySQL Database** (to store the logs).
* **PHP 7.4+** (to handle file uploads and database connections).

### 2. Python Environment (For the AI Model)
The PHP script executes a Python script in the background. You need:
* **Python 3.8+** installed and added to the system PATH.
* **Required Libraries:**
    ```txt
    tensorflow
    numpy
    pillow
    imageio
    ```

---

## ⚙️ Installation & Setup

### Step 1: Clone the Project
```bash
git clone [https://github.com/yourusername/coral-health-classifier.git](https://github.com/yourusername/coral-health-classifier.git)
cd coral-health-classifier
