from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


# NAV 
# NAV 
# NAV 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.notes'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.notes'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/body', methods=['GET', 'POST'])
def body():
    return render_template("body.html", user=current_user)

@auth.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html", user=current_user)

@auth.route('/workoutPicker', methods=['GET', 'POST'])
def workoutPicker():
    return render_template("workoutPicker.html", user=current_user)


# BODY PARTS
# BODY PARTS
# BODY PARTS

@auth.route('/arms', methods=['GET'])
def arms():
    return render_template("/bodyParts/arms.html", user=current_user)
@auth.route('/back', methods=['GET'])
def back():
    return render_template("/bodyParts/back.html", user=current_user)
@auth.route('/chest', methods=['GET'])
def chest():
    return render_template("/bodyParts/chest.html", user=current_user)
@auth.route('/core', methods=['GET'])
def core():
    return render_template("/bodyParts/core.html", user=current_user)
@auth.route('/legs', methods=['GET'])
def legs():
    return render_template("/bodyParts/legs.html", user=current_user)
@auth.route('/shoulders', methods=['GET'])
def shoulders():
    return render_template("/bodyParts/shoulders.html", user=current_user)
@auth.route('/neck', methods=['GET'])
def neck():
    return render_template("/bodyParts/neck.html", user=current_user)
@auth.route('/glutes', methods=['GET'])
def glutes():
    return render_template("/bodyParts/glutes.html", user=current_user)

# 4 WK 
# 4 WK 
# 4 WK 

@auth.route('/4wk', methods=['GET'])
def FourWk():
    return render_template("/workouts/4wk.html", user=current_user)

@auth.route('/4wkDay1', methods=['GET'])
def FourwkDay1():
    return render_template("/workouts/4wk/4wkDay1.html", user=current_user)

@auth.route('/4wkDay2', methods=['GET'])
def FourwkDay2():
    return render_template("/workouts/4wk/4wkDay2.html", user=current_user)

@auth.route('/4wkDay3', methods=['GET'])
def FourwkDay3():
    return render_template("/workouts/4wk/4wkDay3.html", user=current_user)

@auth.route('/4wkDay4', methods=['GET'])
def FourwkDay4():
    return render_template("/workouts/4wk/4wkDay4.html", user=current_user)

@auth.route('/4wkDay5', methods=['GET'])
def FourwkDay5():
    return render_template("/workouts/4wk/4wkDay5.html", user=current_user)





@auth.route('/5x5', methods=['GET'])
def FiveXFive():
    return render_template("/workouts/5x5.html", user=current_user)
@auth.route('/8wk', methods=['GET'])
def Eightwk():
    return render_template("/workouts/8wk.html", user=current_user)
@auth.route('/power', methods=['GET'])
def power():
    return render_template("/workouts/power.html", user=current_user)
@auth.route('/ppl', methods=['GET'])
def ppl():
    return render_template("/workouts/ppl.html", user=current_user)