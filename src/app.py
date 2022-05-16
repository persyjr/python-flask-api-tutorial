from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#logica de la aplicacion
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


#los endpoints
@app.route('/todos', methods=['GET'])# estoy especificando mi endpoint para usarlo con flask
def hello_world():
    return jsonify(todos)# me esta consultando y retornando en formato json mi lista de objetos todos

@app.route('/todos', methods=['POST']) #TAREA nueva del cliente en mi lista de objetos todos
def add_new_todo():
    request_todo = json.loads(request.data)#ingresa tarea nueva del cliente en mi lista de objetos request data tiene mi info en formato JSON
    todos.append(request_todo)
    return jsonify(todos), 200 #me retorna mi informacion en formato JSON y nos comunica un codigo 200
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
  #este es el puerto donde me va a mostrar mis endpoints