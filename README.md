Image Processor Web App
A simple web application built with Flask and OpenCV that allows users to upload an image and apply basic image processing filters, such as grayscale, blur, negative, and edge detection.

📸 Features
Upload an image

Apply multiple filters:

Grayscale

Gaussian Blur

Negative

Edge Detection (Canny)

View and download processed images

🧰 Tech Stack
Python 3

Flask

OpenCV (cv2)

HTML + CSS (vanilla)

🗂️ Project Structure
cpp
Copiar
Editar
image_processor/
├── app.py
├── static/
│   ├── styles.css
│   └── *.jpg (processed images)
├── templates/
│   ├── index.html
│   └── result.html
├── uploads/
│   └── *.jpg (uploaded images)
└── README.md
🚀 How to Run
Clone the repository

bash
Copiar
Editar
git clone https://github.com/yourusername/image-processor.git
cd image-processor
Install dependencies

bash
Copiar
Editar
pip install flask opencv-python
Run the app

bash
Copiar
Editar
python app.py
Open in your browser

Go to: http://127.0.0.1:5000

🧪 Example
After uploading an image, the app will display several versions:

original.jpg

grayscale.jpg

blur.jpg

negative.jpg

edges.jpg

All outputs are stored in the /static folder.
