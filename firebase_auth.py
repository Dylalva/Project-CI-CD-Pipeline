import pyrebase
from flask import session

firebase_config = {
    "apiKey": "TU_API_KEY",
    "authDomain": "TU_AUTH_DOMAIN",
    "databaseURL": "TU_DATABASE_URL",
    "projectId": "TU_PROJECT_ID",
    "storageBucket": "TU_STORAGE_BUCKET",
    "messagingSenderId": "TU_MESSAGING_SENDER_ID",
    "appId": "TU_APP_ID"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        session['user'] = user
        return True, None
    except Exception as e:
        return False, str(e)

def register_user(name, email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        # Puedes guardar el nombre en la base de datos si lo deseas
        session['user'] = user
        return True, None
    except Exception as e:
        return False, str(e)

def logout_user():
    session.pop('user', None)

def get_current_user():
    return session.get('user')

