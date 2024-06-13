from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
        'id': 1,
        'title': 'Data Analytic',
        'local': 'SP, Brazil',
        'salario': 'R$ 5.000'
    },
    {
        'id': 2,
        'title': 'Flask Developer',
        'local': 'SP, Brazil',
        'salario': 'R$ 5.000'
    },
    {
        'id': 3,
        'title': 'Node.js Developer',
        'local': 'SP, Brazil',
        'salario': 'R$ 5.000'
    },
    {
        'id': 4,
        'title': 'Ruby Developer',
        'local': 'SP, Brazil',
        'salario': 'R$ 5.000'
    },
    {
        'id': 5,
        'title': 'Python Developer',
        'local': 'SP, Brazil',
        'salario': 'R$ 5.000'
    }
]

@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS)

@app.route('/jobs')
def listJobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)