from flask import Flask, request, jsonify
import numpy as np
import train_model as tm

app = Flask(__name__)

@app.route('/heart', methods = ['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.json['age'])
        sex = str(request.json['sex'])
        cp = str(request.json['cp'])
        trestbps = int(request.json['trestbps'])
        chol = str(request.json['chol'])
        fbs = str(request.json['fbs'])
        restecg = str(request.json['restecg'])
        thalach = int(request.json['thalach'])
        exang = str(request.json['exang'])
        oldpeak = float(request.json['oldpeak'])
        slope = str(request.json['slope'])
        ca = str(request.json['ca'])
        thal = str(request.json['thal'])

        #new ones
        if sex == '0':
            sex_0 = 1
            sex_1 = 0
        else:
            sex_0 = 1
            sex_1 = 0

        cp_0 = 0
        cp_1 = 0
        cp_2 = 0
        cp_3 = 0
        if cp == '0':
            cp_0 = 1
        elif cp == '1':
            cp_1 = 1
        elif cp == '2':
            cp_2 = 1
        else:
            cp_3 = 1


        if fbs == '0':
            fbs_0 = 1
            fbs_1 = 0
        else:
            fbs_0 = 0
            fbs_1 = 1


        restecg_0 = 0
        restecg_1 = 0
        restecg_2 = 0
        if restecg == '0':
            restecg_0 = 1
        elif restecg == '1':
            restecg_1 = 1
        else:
            restecg_2 = 1

        if exang == '0':
            exang_0 = 1
            exang_1 = 0
        else:
            exang_0 = 0
            exang_1 = 1

        slope_0 = 0
        slope_1 = 0
        slope_2 = 0
        if slope == '0':
            slope_0 = 1
        elif slope == '1':
            slope_1 = 1
        else:
            slope_2 = 1

        ca_0 = 0
        ca_1 = 0
        ca_2 = 0
        ca_3 = 0
        ca_4 = 0
        if ca == '0':
            ca_0 = 1
        elif ca == '1':
            ca_1 = 1
        elif ca == '2':
            ca_2 = 1
        elif ca == '3':
            ca_3 = 1
        else:
            ca_4 = 1


        thal_0 = 0
        thal_1 = 0
        thal_2 = 0
        thal_3 = 0
        if thal == '0':
            thal_0 = 1
        elif thal == '1':
            thal_1 = 1
        elif thal == '2':
            thal_2 = 1
        else:
            thal_3 = 1

        result = np.array([[int(age),
            int(trestbps),
            int(chol),
            int(thalach),
            float(oldpeak),
            int(sex_0),
            int(sex_1),
            int(cp_0),
            int(cp_1),
            int(cp_2),
            int(cp_3),
            int(fbs_0),
            int(fbs_1),
            int(restecg_0),
            int(restecg_1),
            int(restecg_2),
            int(exang_0),
            int(exang_1),
            int(slope_0),
            int(slope_1),
            int(slope_2),
            int(ca_0),
            int(ca_1),
            int(ca_2),
            int(ca_3),
            int(ca_4),
            int(thal_0),
            int(thal_1),
            int(thal_2),
            int(thal_3)
        ]])
        print(result.dtype)

        pred = tm.model_prediction(result)
        return jsonify({ "prediction": str(pred[0])})

if __name__ == '__main__':
    app.run(debug = True)
