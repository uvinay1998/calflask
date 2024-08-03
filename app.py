from flask import Flask,request,jsonify

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
        result=int(numbers1)+int(numbers2)

    elif operation=="multiply":
        result=int(numbers1)*int(numbers2)
    
    elif operation=="divison":
        result=int(numbers1)/int(numbers2)

    else:
        result=int(numbers1)-int(numbers2)

    return "the operation is {} and the result is {}".format(operation,result)




if __name__=='__main__':
    app.run(debug=True)
