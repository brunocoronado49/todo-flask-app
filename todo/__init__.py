from flask import Flask


def create_app():
    app = Flask(__name__)
    
    # Basic configurations
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'braunydev'
    )
    
    @app.route('/')
    def index():
        return 'Hello World'
    
    return app
