from flask import Flask, render_template

app = Flask(__name__)

sonlar = [14, 8, 33, 5, 71, 22, 9, 46]

@app.route('/sonlar/toq')
def toq_sonlar():
    toq = [son for son in sonlar if son % 2 != 0]
    yigindi = sum(toq)

    return render_template(
        'toq.html',
        toq_sonlar=toq,
        yigindi=yigindi
    )

if __name__ == "__main__":
    app.run(debug=True)
