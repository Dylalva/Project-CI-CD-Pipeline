from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Email, EqualTo, Length
import csv
from firebase_auth import login_user, register_user, logout_user, get_current_user, login_with_google

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

GOOGLE_CLIENT_ID = "518988882520-vkpu0vaei5em441fk884em3i93fqpvl3.apps.googleusercontent.com"  # Reemplaza por tu Client ID real


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')


class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Repetir Contraseña', validators=[DataRequired(), EqualTo('password', message='Las contraseñas deben coincidir.')])
    submit = SubmitField('Registrarse')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        success, msg = login_user(form.email.data, form.password.data)
        if success:
            return redirect(url_for('home'))
        else:
            error = 'Error al iniciar sesión: ' + (msg or '')
    return render_template('login.html', form=form, error=error, google_client_id=GOOGLE_CLIENT_ID)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        if form.password.data != form.confirm.data:
            error = 'Las contraseñas no coinciden.'
        else:
            success, msg = register_user(form.name.data, form.email.data, form.password.data)
            if success:
                return redirect(url_for('login'))
            else:
                error = 'Error al registrar: ' + (msg or '')
    return render_template('register.html', form=form, error=error)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/login/google/callback', methods=['POST'])
def google_callback():
    id_token = request.json.get('id_token')
    success, msg = login_with_google(id_token)
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'No se pudo iniciar sesión con Google.'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

