from flask import Flask,request

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to flask"


@app.route("/calc",methods=["GET"])
def mathoperators():
    operation =request.json["operation"]
    numbers1=request.json["number1"]
    numbers2=request.json["number2"]
    if operation == 'Add':
        result=numbers1+numbers2

    elif operation=="multiply":
        result=numbers1+numbers2
    
    elif operation=="divison":
        result=numbers1/numbers2

    else:
        result=numbers1-numbers2

    return result




if __name__=='__main__':
    app.run(debug=True)
