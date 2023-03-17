from flask import Flask,jsonify,request,render_template
import json
import os

app = Flask(__name__)
storage_path = "./storage.data"

def get_data():
    if not os.path.exists(storage_path):
        return {}


    with open(storage_path, 'r') as storage:
        raw_data = storage.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


@app.route('/')
def index():
    return render_template('./index.html')     
    

@app.route('/api/v1/storage/json/all', methods=['GET'])
def get_all():
    data=get_data()
    return jsonify(data)



@app.route('/api/v1/storage/json/write', methods=['POST'])
def put():
    post_data = request.json
    data = get_data()
    key = str(list(post_data.keys()))
    key = key.replace("'","").replace("[","").replace("]","")
    value = str(list(post_data.values()))
    value = value.replace("'","").replace("[","").replace("]","") 
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    with open(storage_path, 'w') as storage:
        storage.write(json.dumps(data))
    return ("Success add data" + str(post_data)) 


@app.route('/api/v1/storage/json/read', methods=['GET'])
def get():
    data= get_data()
    name= request.args.get('key')
    result = data.get(name)
    if result:
      return jsonify("result:",result)
    return "Nothing found"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
