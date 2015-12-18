import os


def load_config(app):
    """
    Loads the prod/dev configuration based on the availablity of the 
    OPENSHIFT environment variables
    
    app: The Flask application variable
    """
    if os.environ.get('OPENSHIFT_APP_UUID'):
        app.config.from_pyfile('flaskapp-prod.cfg')
        app.config['CLIENT_SECRET'] = os.environ.get('CLIENT_SECRET')
    else:
        app.config.from_pyfile('flaskapp-dev.cfg')
        import user_settings
        app.config['CLIENT_SECRET'] = user_settings.CLIENT_SECRET