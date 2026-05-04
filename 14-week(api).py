from flask import Flask,request,jsonify
import pandas as pd
import io

app=Flask(__name__)

def compute_corr(df):
    corr=df[['a','b','c']].corr()
    return corr.round(6).to_dict()

@app.route('/',methods=['GET'])
def index():
    return jsonify({
        "project":"data-heatmap-project",
        "endpoints":{
            "GET/corr":"triple.csv read,returns matrix",
            "POST/corr":"download file,get matrix(form-data: file=triple.csv)"
        }
    })

@app.route('/corr',methods=['GET'])
def get_corr():
    try:
        df=pd.read_csv("triple.csv")
        result=compute_corr(df)
        return jsonify({
            "status":"ok",
            "method":"GET",
            "corr_matrix":result
        })
    except FileNotFoundError:
        return jsonify({"error":"triple.csv not found"}),404

@app.route('/corr',methods=['POST'])
def post_corr():
    if 'file' not in request.files:
        return jsonify({"error":"no file field"}),400

    file=request.files['file']
    if file.filename=='':
        return jsonify({"error":"file not selected"}),400

    try:
        content=file.read().decode('utf-8')
        df=pd.read_csv(io.StringIO(content))

        missing=[col for col in ['a','b','c'] if col not in df.columns]
        if missing:
            return jsonify({"error":f"missing columns:{missing}"}),400

        result=compute_corr(df)
        return jsonify({
            "status":"ok",
            "method":"POST",
            "filename":file.filename,
            "rows":len(df),
            "corr_matrix":result
        })
    except Exception as e:
        return jsonify({"error":str(e)}),500

if __name__=='__main__':
    print("server started:http://127.0.0.1:5000")
    print("GET http://127.0.0.1:5000/corr")
    print("POST http://127.0.0.1:5000/corr (form-data: file)")
    app.run(debug=True)