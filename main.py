from flask import Flask, render_template, url_for, request
import pandas as pd

app = Flask(__name__)
filename = 'file.csv'


@app.route("/1.html")
def index():
    return render_template("1.html")


@app.route("/")
def goHome():
    return render_template("1.html")

@app.route("/username/<username>")
def username(username):
    return "User %s" % username

@app.route("/username")
def userName(username=None):
    return "User %s" % username

@app.route("/answer", methods=['POST'])
def getValumeForm():
    name = request.form['name']
    email = request.form['email']
    answer = request.form['message']

    with open(filename, 'a') as file_object:
        file_object.write(name)
        file_object.write(',')
        file_object.write(email)
        file_object.write(',')
        file_object.write(answer)
        file_object.write("\n")

    return render_template("1.html")

@app.route("/result.html")
def result():
    return render_template("/result.html")

@app.route("/sort", methods=['POST'])
def sort():
    string = list(map(int, request.form['stringInt'].split()))
    string = sortstr(string)
    string = " ".join(map(str, string))
    return render_template('/result.html', ans=string)

@app.route("/findUser", methods=['POST'])
def findsting():
    name1 = request.form['name1']
    f = pd.read_csv(filename)
    userName = f[f['name'] == name1].values

    if userName.size != 0:
        userName = ' '.join(userName[0])
    else:
        userName = name1 +' is missing!'

    return render_template('/put.html', userName=userName)



def sortstr(Y):
    for i in range(1, len(Y)):
        b = Y[i]
        j = i - 1
        while (j >= 0) and (b < Y[j]):
            Y[j + 1] = Y[j]
            j -= 1
        Y[j + 1] = b
    return Y

# with app.test_request_context():
#     print (url_for('index'))


if __name__=='__main__':
    app.run(debug=True)



