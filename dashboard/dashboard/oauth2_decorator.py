"""Provides oauth2 decorators in a mockable way."""

from oauth2client.appengine import OAuth2Decorator

decorator = OAuth2Decorator(
    client_id='425761728072.apps.googleusercontent.com',
    client_secret='9g-XlmEFW8ROI01YY6nrQVKq',
    scope=['https://www.googleapis.com/auth/projecthosting',
           'https://www.googleapis.com/auth/userinfo.email'],
    message='Oauth error occurred!',
    callback_path='/oauth2callback')
