from flask import Flask, render_template, request, url_for, redirect, session, flash, jsonify

from pymongo import MongoClient, UpdateOne
from bson import ObjectId
import bcrypt

app = Flask(__name__)
app.secret_key = "secret_key"


class Database:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MongoClient('mongodb://localhost:27017/')
        return cls._instance


client = Database.get_instance()
db = client['UniversityManagementSystem']

admins = db["adminsCollection"]
teachers = db["teachersCollection"]
students = db["studentsCollection"]




class UserFactory:
    @staticmethod
    def create_user(user_type, username, password):
        if user_type == 'admin':
            return admins.insert_one({'username': username, 'password': bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())})
        elif user_type == 'doctor':
            return teachers.insert_one({'username': username, 'password': bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())})
        elif user_type == 'patient':
            return students.insert_one({'username': username, 'password': bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), "status" : "uncheck"})
        else:
            raise ValueError("Invalid user type")


@app.route('/')
def index():
    return render_template('index.html')


# Admin code start
@app.route('/adminRegister', methods=['GET', 'POST'])
def adminRegister():
    if request.method == 'POST':
        existing_user = admins.find_one({'username': request.form['admin_username']})
        
        if existing_user is None:
            UserFactory.create_user('admin', request.form['admin_username'], request.form['admin_password'])
            session['admin_username'] = request.form['admin_username']
            return redirect(url_for('adminDashboard'))
        return 'That username already exists!'    
    return render_template('adminRegister.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'admin_username' in session:
        return redirect(url_for('adminDashboard'))

    if request.method == 'POST':
        login_admin = admins.find_one({'username': request.form['admin_username']})
        if login_admin:
            if bcrypt.checkpw(request.form['admin_password'].encode('utf-8'), login_admin['password']):
                session['admin_username'] = request.form['admin_username']
                return redirect(url_for('adminDashboard'))
        return 'Invalid username/password combination'
    return render_template('adminLogin.html')

@app.route('/adminDashboard')
def adminDashboard():
    if 'admin_username' in session:
        students_data = list(db.students.find())
        teachers_data = list(db.teachers.find())
        return render_template('adminDashboard.html', admin_username=session['admin_username'], students = students_data, teachers = teachers_data)
    return redirect(url_for('admin'))

# Admin code end here



@app.post('/<id>/deleteTeacherData/')
def deleteDoctorData(id):
    teachers.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('adminDashboard'))

@app.post('/<id>/deleteStudentData/')
def deletePatientData(id):
    students.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('adminDashboard'))

@app.route('/logout')
def admin_logout():
    session.pop('admin_username', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)