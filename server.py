from flask import Flask, request, jsonify

app = Flask(__name__)

# Variable global para almacenar el gesto recibido
current_gesture = None

@app.route('/gesture', methods=['POST', 'GET'])
def gesture():
    global current_gesture

    if request.method == 'POST':
        # Procesa los datos del POST
        data = request.get_json()  # Obtiene los datos JSON enviados en la solicitud
        if data and 'gesture' in data:
            current_gesture = data['gesture']  # Guarda el gesto en la variable global
            return jsonify({"message": current_gesture, "gesture": current_gesture}), 200
        else:
            return jsonify({"error": "No se recibió ningún gesto"}), 400

    elif request.method == 'GET':
        # Retornar el gesto actual en formato JSON
        if current_gesture is not None:
            return jsonify({"gesture": current_gesture})  # Envía el gesto almacenado
        else:
            return jsonify({"gesture": "ninguno"}), 200  # Retorna 'ninguno' si no hay gesto

if __name__ == "__main__":
    app.run(debug=True)
