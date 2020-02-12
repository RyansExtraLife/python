#Import the Flask Framework.
from flask import Flask, render_template, redirect, url_for, request

#Import the student module
from student import Student

#
students = []

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def students_page():

    if request.method == "POST":
        #Reqeust the dictonary.
        new_student_id = request.form.get("student-id","")
        new_student_name = request.form.get("name","")
        new_student_last_name = request.form.get("last_name","")

        #Create new Student Class and append it to the list. 
        new_student = Student(name=new_student_name, student_id=new_student_id)
        students.append(new_student)

        #Redrict the user to the same page as they started from.
        return redirect(url_for("students_page"))

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
