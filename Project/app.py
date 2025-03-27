from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.auth import auth_bp
from controllers.main import main_bp

app = Flask(__name__, template_folder="temps")

# Set secret keys
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['JWT_SECRET_KEY'] = 'jwtsecretkey'

# Configure JWT to use cookies instead of headers
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'
app.config['JWT_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # Disable CSRF for testing

jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(main_bp, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
