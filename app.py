from flask import Flask, request, jsonify
from flask_cors import CORS
app=Flask(__name__)

CORS(app)

@app.route("/saludo")
def getSaludo():
    return "hola mundo"

@app.route('/sumar', methods=['POST'])
def sumar():
    try:
        data = request.get_json()

        operandos = data.get('operandos', [])
        #print(data)

        resultado = float(operandos[0])+float(operandos[1])
        #print(resultado)
        return jsonify({'resultado': resultado})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restar', methods=['POST'])
def restar():
    try:
        data = request.get_json()
        operandos = data.get('operandos', [])
        #print(data)
        if not operandos or len(operandos) < 2:
            return jsonify({'error': 'Se requieron dos numeros para la operacion'}), 400

        resultado = float(operandos[0]) - float(operandos[1])
        #print(resultado)
        return jsonify({'resultado': resultado})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    try:
        data = request.get_json()
        operandos = data.get('operandos', [])
        #print(data)
        if not operandos or len(operandos) < 2:
            return jsonify({'error': 'Se requieron dos numeros para la operacion'}), 400

        resultado = float(operandos[0]) * float(operandos[1])
        #print(resultado)
        return jsonify({'resultado': resultado})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/dividir', methods=['POST'])
def dividir():
    try:
        data = request.get_json()
        operandos = data.get('operandos', [])
        #print(data)
        if not operandos or len(operandos) < 2:
            return jsonify({'error': 'Se requieron dos numeros para la operacion'}), 400

        resultado = float(operandos[0]) / float(operandos[1])
        #print(resultado)
        return jsonify({'resultado': resultado})

    except ZeroDivisionError:
        return jsonify({'error': 'No se puede dividir por cero'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/potencia', methods=['POST'])
def potencia():
    try:
        data = request.get_json()
        operandos = data.get('operandos', [])
        #print(data)
        if not operandos or len(operandos) < 2:
            return jsonify({'error': 'Se requieron dos numeros para la operacion'}), 400

        resultado = float(operandos[0]) ** float(operandos[1])
        return jsonify({'resultado': resultado})

    except Exception as e:
        return jsonify({'error': str(e)}), 500






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)