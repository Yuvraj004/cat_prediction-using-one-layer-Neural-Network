from flask import Flask,request,jsonify
import util
app = Flask(__name__) #module

@app.route('/')
def hello():
    return "Hi"

@app.route('/predict_cat', methods=['GET', 'POST'])
def predict_cat():
    cat_image = float(request.form['cat_image'])

    response = jsonify({
        'Cat_Or_Not': util.predict_cat(cat_image)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ =="__main__":
    print("Cat Prediction Server")
    util.load_saved_artifacts()
    app.run()