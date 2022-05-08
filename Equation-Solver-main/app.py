import json
import os

from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_cors import CORS
from flask_restful import Api

from calculator import calculate

root = os.getcwd()

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        #eq = request.form.get('equation')
        data=request.get_json()
        eq1 = data['equation1']
        eq2 = data['equation2']
        id = data['id']
        print(eq1)
        try:
            soltn= calculate(eq1,eq2,id)
            res = 'Solved Successfully'
        except:
            res = 'Unuccessful'
        return redirect(url_for('predict', response=res,solution = soltn ))
    return render_template('index.html')


@app.route('/predict')
def predict():
    response = request.args.get('response', None)
    sol = request.args.get('solution',None)
    # sol2 = request.args.get('solution2',None)
    return jsonify({'response': 'OK', 'reponse_msg':response, 'solution': sol})
    return sol
    return render_template('pre.html', solution = sol1,equation = eq)    


# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     return None

# class Predict(Resource):
    
#     def post(self):
#         print("solution :", calculate(equation))
#         os.mkdir('internals')
#         shutil.move('segmented', 'internals')
#         shutil.move('input.png', 'internals')
#         shutil.move('segmented_characters.csv', 'internals')
#         formatted_equation, solution = calculate(equation)
#         solution = " ".join(str(x) for x in solution)
#         return json.dumps({
#             'Entered_equation': equation,
#             'solution': solution
#         })

# api.add_resource(Predict, "/predict")

# if __name__ == "__main__":
#     app.run(debug=True)
