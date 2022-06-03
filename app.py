from flask import Flask, request, render_template
import house


app = Flask(__name__)


@app.route("/",methods = ["GET","POST"])
def house_pred():
    if(request.method == "POST"):
        med  = request.form["medinc"]
        value = 0
        if(med != ""):
            value = house.house_rate(float(med))
    return render_template("index.html", medval = med, val = value)


if __name__ == "__main__":
    app.run(debug = True)