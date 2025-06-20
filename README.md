# 🧬 HematoVision: Advanced Blood Cell Classification Using Transfer Learning

HematoVision is a deep learning web application that classifies microscopic blood cell images into four types:
- Eosinophil
- Lymphocyte
- Monocyte
- Neutrophil

It uses **Transfer Learning (MobileNetV2)** for high accuracy and is built with **Flask** for a simple, interactive web interface.

---

## 🚀 Demo

🔗 **Live Demo (coming soon via Render)**  
📷 Upload a blood cell image → 🧠 Model predicts the cell type → 📊 Result with image preview

---

## 🛠️ Tech Stack

- **Model:** TensorFlow / Keras (MobileNetV2)
- **Web Framework:** Flask
- **Preprocessing:** OpenCV
- **Frontend:** HTML + CSS (with base64 image rendering)

---

## 📦 Project Structure

HematoVision/
├── app.py # Flask app
├── Blood Cell.h5 # Pretrained model file (~60MB)
├── requirements.txt # Python dependencies
├── Procfile # For Render deployment
├── static/ # Uploaded images go here
└── templates/ # HTML pages
├── home.html # Upload page
└── result.html # Result display page


---

## 💻 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/sathvik-bandla/HematoVision-Advanced-Blood-Cell-Classification-Using-Transfer-Learning.git
cd HematoVision-Advanced-Blood-Cell-Classification-Using-Transfer-Learning
```
### 2.(Optional) Create Virtual Environment

python -m venv venv
venv\Scripts\activate #Windows
# source venv/bin/activate # macOS/Linux

### 3.











