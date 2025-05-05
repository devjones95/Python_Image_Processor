import os
from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def aplicar_filtros(imagem_path):
    imagem = cv2.imread(imagem_path)
    filtros = {
        'original': imagem,
        'preto_e_branco': cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY),
        'blur': cv2.GaussianBlur(imagem, (15, 15), 0),
        'negativo': cv2.bitwise_not(imagem),
        'bordas': cv2.Canny(imagem, 100, 200)
    }

    resultados = {}
    for nome, img in filtros.items():
        saida_path = f'static/{nome}.jpg'
        cv2.imwrite(saida_path, img)
        resultados[nome] = saida_path
    return resultados

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['imagem']
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            resultados = aplicar_filtros(path)
            return render_template('result.html', imagens=resultados)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
