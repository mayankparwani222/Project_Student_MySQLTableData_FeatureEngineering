from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="studentDetails",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    course = request.form["course"]
    semester = request.form["semester"]
    marks = int(request.form["marks"])
    result = "Pass" if marks >= 40 else "Fail"

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (name, course, semester, marks, result)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, course, semester, marks, result))

    conn.commit()
    cur.close()
    conn.close()

    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)