from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '1537'

class StudentForm(FlaskForm):
    full_name = StringField("Student's Full Name", validators=[DataRequired()])
    email = StringField("Student's Email Address", validators=[DataRequired()])
    student_number = StringField("Student Number", validators=[DataRequired()], render_kw={"type": "number", "placeholder": "e.g. 425869", "maxlength": "6"})
    grades = StringField("Grades Obtained in Course", validators=[DataRequired()], render_kw={"placeholder": "e.g. Subject: Grade"})
    satisfaction = SelectField("Overall Satisfaction with Academic Experience", choices=[('very_satisfied', 'Very Satisfied'), ('satisfied', 'Satisfied'), ('neutral', 'Neutral'), ('dissatisfied', 'Dissatisfied'), ('very_dissatisfied', 'Very Dissatisfied')], default='neutral')
    improvements = TextAreaField("Suggestions for Improvement")
    submit = SubmitField('Submit')

@app.route('/welcome.html')
def home():
    return render_template('welcome.html')

@app.route('/information.html')
def information():
    return render_template('information.html')

@app.route('/stud_data.html', methods=['GET', 'POST'])
def data_collection():
    form = StudentForm()
    if form.validate_on_submit():
        with open('data.txt', 'a') as file:
            file.write(f"Student's Full Name: {form.full_name.data}\n")
            file.write(f"Student's Email Address: {form.email.data}\n")
            file.write(f"Student Number: {form.student_number.data}\n")
            file.write(f"Grades Obtained in Course: {form.grades.data}\n")
            file.write(f"Overall Satisfaction with Academic Experience: {form.satisfaction.data}\n")
            file.write(f"Suggestions for Improvement: {form.improvements.data}\n")
        return "Form submitted successfully!"
    return render_template('stud_data.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

#just a comment for github update