from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'chiku'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'contact_form'

mysql = MySQL(app)

# Route for the Contact Form
@app.route('/')
def contact_form():
    return render_template('index.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
         # Save data to MySQL
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact_messages (name, email, subject, message) VALUES (%s, %s, %s, %s)", (name, email, subject, message))
        mysql.connection.commit()
        cur.close()

        return "Message successfully submitted!"

# if _name_ == '_main_':
#     app.run(debug=True)