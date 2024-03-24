# Modules
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

# Creating Flask app instance
app = Flask(__name__)
# Secret key for CSRF protection
app.config['SECRET_KEY'] = '1537'

# Define a form class for student data
class StudentForm(FlaskForm):
    full_name = StringField("Student's Full Name", validators=[DataRequired()])
    email = StringField("Student's Email Address", validators=[DataRequired()])
    student_number = StringField("Student Number", validators=[DataRequired()], render_kw={"type": "number", "placeholder": "e.g. 425869", "maxlength": "6"})
    grades = StringField("Grades Obtained in Course", validators=[DataRequired()], render_kw={"placeholder": "e.g. Subject: Grade"})
    satisfaction = SelectField("Overall Satisfaction with Academic Experience", choices=[('very_satisfied', 'Very Satisfied'), ('satisfied', 'Satisfied'), ('neutral', 'Neutral'), ('dissatisfied', 'Dissatisfied'), ('very_dissatisfied', 'Very Dissatisfied')], default='neutral')
    improvements = TextAreaField("Suggestions for Improvement")
    submit = SubmitField('Submit')

# Route for the main page
@app.route('/welcome.html')
def home():
    return render_template('welcome.html')

# Route for the information page
@app.route('/information.html')
def information():
    return render_template('information.html')

# Route for student data collection page
@app.route('/stud_data.html', methods=['GET', 'POST'])
def data_collection():
    form = StudentForm()
    # If form is submitted and validated
    if form.validate_on_submit():
        # Write form data to a text file
        with open('data.txt', 'a') as file:
            file.write(f"Student's Full Name: {form.full_name.data}\n")
            file.write(f"Student's Email Address: {form.email.data}\n")
            file.write(f"Student Number: {form.student_number.data}\n")
            file.write(f"Grades Obtained in Course: {form.grades.data}\n")
            file.write(f"Overall Satisfaction with Academic Experience: {form.satisfaction.data}\n")
            file.write(f"Suggestions for Improvement: {form.improvements.data}\n")
        return "Form submitted successfully!"
    # Render the student data collection template with the form
    return render_template('stud_data.html', form=form)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
