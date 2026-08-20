"""Web application entry point for the ClassGroup manager."""
import os
from datetime import date
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from src.class_group import ClassGroup
from src.student import Student

app = Flask(__name__)

# Initialize CSRF Protection with a secure random key
# Fetch the key from environment variables to prevent Data Exposure
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', os.urandom(32)) #NOSONAR
csrf = CSRFProtect(app)

# Initialize a global ClassGroup with a capacity of 5 for demonstration
live_class = ClassGroup(5)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles the main dashboard and student registration."""
    error = None
    if request.method == 'POST':
        try:
            student_id = int(request.form['id'])
            name = request.form['name']
            
            # Using a static birthday for simplicity in this demo
            new_student = Student(student_id, name, date(2025, 1, 1))
            
            if live_class.add_student(new_student):
                return redirect(url_for('index'))
            else:
                error = "Class is at maximum capacity!"
        except ValueError:
            error = "Invalid ID format. Please enter a number."

    return render_template(
        'index.html', 
        students=live_class.get_students(), 
        size=live_class.get_size(), 
        capacity=live_class.get_capacity(), 
        error=error
    )

if __name__ == '__main__':
    # Deactivated debug feature for production security
    app.run(debug=False, port=5000)