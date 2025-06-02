import os
from dotenv import load_dotenv
import pyrebase
from flask import session
import requests

load_dotenv()

firebase_config = {
  "apiKey": "AIzaSyDGumoDc1Gr0iNcOjFFpwTvU2WUXWV0LLI",
  "databaseURL": "https://ci-cd-app-6589f-default-rtdb.firebaseio.com",
  "projectId": "ci-cd-app-6589f",
  "storageBucket": "ci-cd-app-6589f.appspot.com",
  "messagingSenderId": "518988882520",
  "appId": "1:518988882520:web:0ffbe42be85343cce9a02d",
  "measurementId": "G-JE3KWE671Z",
  "authDomain": "ci-cd-app-6589f.firebaseapp.com"
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

def login_with_google(id_token):
    try:
        api_key = firebase_config["apiKey"]
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key={api_key}"
        payload = {
            "postBody": f"id_token={id_token}&providerId=google.com",
            "requestUri": "http://localhost:5000/login",
            "returnIdpCredential": True,
            "returnSecureToken": True
        }
        res = requests.post(url, json=payload)
        res.raise_for_status()
        user = res.json()
        # Normaliza el token para que siempre esté en la raíz como 'idToken'
        if 'idToken' not in user and 'id_token' in user:
            user['idToken'] = user['id_token']
        session['user'] = user
        return True, None
    except Exception as e:
        return False, str(e)
