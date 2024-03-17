# # # 
# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# # procfile.txt
# # web: gunicorn app:app
# # first file that we have to run first : flask server name
# app = Flask(__name__)
# pkl_file = open('model.pkl', 'rb')
# model = pickle.load(open('model.pkl', 'rb'))
# index_dict = pickle.load(pkl_file)


# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/predict', methods=['POST'])
# def predict():

#     if request.method == 'POST':
#         result = request.form

#         index_dict = pickle.load(open('cat', 'rb'))
#         location_cat = pickle.load(open('DISTRICT_cat', 'rb'))

#         new_vector = np.zeros(33)

#         result_DISTRICT = result['DISTRICT']

#         if result_DISTRICT not in location_cat:
#            new_vector[28] = 1
#         else:
#            new_vector[index_dict[str(result['DISTRICT'])]] = 1

#         # Handle missing key errors
#         # try:
#         new_vector[index_dict[str(result['COLLEGE'])]] = 1
#         new_vector[0] = result['YEAR']
#         new_vector[1] = result['CATEGORY']
#         # except KeyError:
#         #     return render_template('index.html', Predict_score='Invalid input. Please check your form fields and try again.')

#         new = [new_vector]

#         prediction = model.predict(new)

#         return render_template('index.html', Predict_score='ESTIMATED ADMISSION PREDICTION IS % {} ACCURACY'.format(prediction[0]))

#     # Handle non-POST requests
#     else:
#         return render_template('index.html', Predict_score='Invalid request method. Please use the POST method.')


# if __name__ == "__main__":
#     app.run(debug=True)


# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle

# app = Flask(__name__)

# # Load the saved model and index dictionary
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)
    
# with open('index_dict.pkl', 'rb') as f:
#     index_dict = pickle.load(f)
    
# @app.route('/')
# def index():
#     return render_template('index.html', Predict_score="")


# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the input values from the form
#     year = int(request.form['YEAR'])
#     district = request.form['DISTRICT']
#     college = request.form['COLLEGE']
#     category = request.form['CATEGORY']
    
#     # Create the input vector using the index dictionary
#     input_vector = np.zeros(len(index_dict))
#     input_vector[0] = year
#     input_vector[index_dict['DISTRICT'][district]] = 1
#     input_vector[index_dict['COLLEGE'][college]] = 1
#     input_vector[index_dict['CATEGORY'][category]] = 1
    
#     # Make the prediction using the loaded model
#     prediction = model.predict(input_vector.reshape(1, -1))[0]
    
#     # Return the prediction to the user
#     return render_template('index.html', prediction=prediction)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         # Get form data
#         DISTRICT = request.form.get('DISTRICT')
#         COLLEGE = request.form.get('COLLEGE')
#         CATEGORY = request.form.get('CATEGORY')
#         YEAR = request.form.get('YEAR')

#         # Call your function to get the prediction score
#         predict_score = predict('DISTRICT','COLLEGE','CATEGORY','YEAR')

#         # Pass the prediction score to the template
#         return render_template('index.html', predict_score=predict)
#     else:
#         return render_template('index.html')


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
pkl_file = open('model.pkl', 'rb')
model = pickle.load(open('model.pkl', 'rb'))
index_dict = pickle.load(pkl_file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':
        result = request.form

        index_dict = pickle.load(open('cat', 'rb'))
        location_cat = pickle.load(open('DISTRICT_cat', 'rb'))

        new_vector = np.zeros(33)

        result_DISTRICT = result['DISTRICT']

        if result_DISTRICT not in location_cat:
           new_vector[28] = 1
        else:
           new_vector[index_dict[str(result['DISTRICT'])]] = 1

        try:
            new_vector[index_dict[str(result['COLLEGE'])]] = 1
            new_vector[0] = result['YEAR']
            new_vector[1] = result['CATEGORY']
        except KeyError:
            return render_template('index.html', Predict_score='Invalid input. Please check your form fields and try again.')

        new = [new_vector]

        prediction = model.predict(new)

        return render_template('index.html', Predict_score='ESTIMATED ADMISSION PREDICTION IS % {} ACCURACY'.format(prediction[0]))

    else:
        return render_template('index.html', Predict_score='Invalid request method. Please use the POST method.')


if __name__ == "__main__":
    app.run(debug=True)
