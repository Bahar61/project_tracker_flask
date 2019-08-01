"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def get_info():


    return render_template("new_student.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template('student_info.html', first=first, last=last, github=github)
    
    return  html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    new_student = request.form.get('new_name')



    return render_template("added_student.html", new_student=new_student)




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
