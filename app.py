# from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
# from werkzeug.utils import secure_filename
# from flask_sqlalchemy import SQLAlchemy
# import os
#
# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace with a strong secret key
# app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
# # Create the upload folder if it doesn't exist
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
#
# # Admin credentials
# ADMIN_USERNAME = "Okechukwu"
# ADMIN_PASSWORD = "Ebube"
#
# # Database model for user registration data
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fullname = db.Column(db.String(100), nullable=False)
#     state_of_origin = db.Column(db.String(50), nullable=False)
#     country = db.Column(db.String(50), nullable=False)
#     gender = db.Column(db.String(10), nullable=False)
#     dob = db.Column(db.String(20), nullable=False)
#     picture_path = db.Column(db.String(100), nullable=True)
#     video_path = db.Column(db.String(100), nullable=True)
#
# # Initialize the database
# with app.app_context():
#     db.create_all()
#
# @app.route('/')
# def index():
#     return redirect(url_for('register'))
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Get form data
#         fullname = request.form.get('fullname')
#         state_of_origin = request.form.get('state_of_origin')
#         country = request.form.get('country')
#         gender = request.form.get('gender')
#         dob = request.form.get('dob')
#
#         # Handle file uploads
#         picture = request.files.get('picture')
#         video = request.files.get('video')
#
#         picture_path = None
#         video_path = None
#
#         # Save picture if uploaded
#         if picture:
#             picture_filename = secure_filename(picture.filename)
#             picture_path = picture_filename  # Save only filename
#             picture.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_filename))
#
#         # Save video if uploaded
#         if video:
#             video_filename = secure_filename(video.filename)
#             video_path = video_filename  # Save only filename
#             video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))
#
#         # Create a new user record in the database
#         new_user = User(
#             fullname=fullname,
#             state_of_origin=state_of_origin,
#             country=country,
#             gender=gender,
#             dob=dob,
#             picture_path=picture_path,
#             video_path=video_path
#         )
#         db.session.add(new_user)
#         db.session.commit()
#
#         flash('Registration successful!')
#         return redirect(url_for('register'))
#
#     return render_template('register.html')
#
# @app.route('/admin_login', methods=['GET', 'POST'])
# def admin():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#
#         if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#             session['admin_logged_in'] = True
#             return redirect(url_for('admin_dashboard'))
#         else:
#             flash('Invalid credentials, please try again.')
#             return redirect(url_for('admin'))
#
#     return render_template('admin_login.html')
#
#
# @app.route('/admin_dashboard')
# def admin_dashboard():
#     # Check if the admin is logged in
#     if not session.get('admin_logged_in'):
#         flash('Please log in to access the admin dashboard.')
#         return redirect(url_for('admin'))
#
#     # Retrieve all users from the database
#     users = User.query.all()
#     return render_template('admin.html', users=users)
#
# @app.route('/logout')
# def logout():
#     session.pop('admin_logged_in', None)
#     flash('Logged out successfully.')
#     return redirect(url_for('admin'))
#
# # Serve uploaded files (pictures and videos)
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Admin credentials
ADMIN_USERNAME = "Okechukwu"
ADMIN_PASSWORD = "Ebube"


# Database model for user registration data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    state_of_origin = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(50), nullable=True)
    company = db.Column(db.String(100), nullable=True)
    area_of_expertise = db.Column(db.String(100), nullable=True)
    picture_path = db.Column(db.String(100), nullable=True)
    video_path = db.Column(db.String(100), nullable=True)


# Initialize the database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return redirect(url_for('register'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        state_of_origin = request.form.get('state_of_origin')
        country = request.form.get('country')
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        title = request.form.get('title')
        company = request.form.get('company')
        area_of_expertise = request.form.get('area_of_expertise')

        picture = request.files.get('picture')
        video = request.files.get('video')

        picture_path = None
        video_path = None

        if picture:
            picture_filename = secure_filename(picture.filename)
            picture_path = picture_filename
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_filename))

        if video:
            video_filename = secure_filename(video.filename)
            video_path = video_filename
            video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))

        new_user = User(
            fullname=fullname,
            state_of_origin=state_of_origin,
            country=country,
            gender=gender,
            dob=dob,
            title=title,
            company=company,
            area_of_expertise=area_of_expertise,
            picture_path=picture_path,
            video_path=video_path
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!')
        return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/admin_login', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials, please try again.')
            return redirect(url_for('admin'))

    return render_template('admin_login.html')


@app.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash('Please log in to access the admin dashboard.')
        return redirect(url_for('admin'))

    users = User.query.all()
    return render_template('admin.html', users=users)


@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully.')
    return redirect(url_for('admin'))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)