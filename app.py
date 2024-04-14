from flask import Flask, request
from flask_cors import CORS



'''
at the / endpoint when you get the request with the name make another POST request 
with a body to the other dockerized flask app t
hat is running and add it to an existing dictionary or list there. change the functionality of this app to 
when you get the request for the name to get it from the other app's dictionary or list.
and for further work see a little bit about docker-compose and run all of it with docker-compose
'''

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST'])
def index():
    try:
        #get json data
        json_data = request.get_json()
        name = json_data['name']

        # if name is not a string return bad request 400
        if name.isdigit():
            # return "Bad request", 400
            return "bad  request", 400

        response = request.post("http://172.20.10.7:3001/employees", json=json_data)
        return response

    except Exception as e:
        print(e)

@app.route("/employees", methods=['POST'])
def employees():
    try:
        #get json data
        json_data = request.get_json()
        name = json_data['name']

        employe = [
            {"firstname": "Max", "name": "Mustermann", "last_name": "Müller", "age": 35, "profession": "Ingenieur"},
            {"firstname": "Anna", "name": "Schmidt", "last_name": "Meier", "age": 28,
             "profession": "Softwareentwickler"},
            {"firstname": "Julia", "name": "Fischer", "last_name": "Schulz", "age": 42, "profession": "Manager"},
            {"firstname": "David", "name": "Wagner", "last_name": "Koch", "age": 31, "profession": "Verkäufer"},
            {"firstname": "Lena", "name": "Becker", "last_name": "Lehmann", "age": 45, "profession": "Anwalt"}]

        for i in employe:
            if i["name"] == name:
                return i

        return "Not found", 404

    except Exception as e:
        print(e)



if __name__ == "__main__":
    app.run(port=3001, host="0.0.0.0", debug=True, threaded=True)
