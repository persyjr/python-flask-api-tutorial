from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#logica de la aplicacion
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


#los endpoints
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_todo = json.loads(request.data)
    todos.append(request_todo)
    return jsonify(todos), 200
    #print("peticion recibida body", request_body)
    

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if(position >= len(todos)):
        return "posicion fuera de rango",400
    if (position<0):
        return "posicion negativa",400
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

#arranque de la app
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)