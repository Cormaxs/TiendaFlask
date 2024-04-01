from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Tienda')
def Tienda():
    return render_template('base.html')

@app.route('/descripcion')
def Descripcion():
    return render_template('descripcion.html')

# Configura la ruta estática
app.config['STATIC_FOLDER'] = 'static'  # Indica que la carpeta 'static' almacena los archivos estáticos

if __name__=='__main__':
    app.run(debug=True, port=5005)
    
