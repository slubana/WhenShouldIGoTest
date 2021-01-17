from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route('/')
def input():
    return render_template("input.html")

@app.route('/output', methods=['POST'])
def output():
    location = request.form['location']
    time = main.findBestTime(location)
    return render_template("output.html", data=time)

if __name__ == "__main__":
    app.run(debug=True)

