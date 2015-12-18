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
        app.config['DB_HOST'] = os.environ.get('OPENSHIFT_MYSQL_DB_HOST')
        app.config['DB_USER'] = os.environ.get('OPENSHIFT_MYSQL_DB_USERNAME')
        app.config['DB_PASS'] = os.environ.get('OPENSHIFT_MYSQL_DB_PASSWORD')
        app.config['DB_PORT'] = os.environ.get('OPENSHIFT_MYSQL_DB_PORT')
        app.config['DB_NAME'] = os.environ.get('OPENSHIFT_APP_NAME')
    else:
        app.config.from_pyfile('flaskapp-dev.cfg')
        import user_settings
        app.config['CLIENT_SECRET'] = user_settings.CLIENT_SECRET
        
def connect_to_db(app):
    """
    Connect to a MySQL database and use the utf8 charset
    Return: The session
    """
    connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(app.config['DB_USER'], app.config['DB_PASS'],
                                                     app.config['DB_HOST'], app.config['DB_PORT'],
                                                     app.config['DB_NAME'])
    engine = create_engine(connect_string, convert_unicode=True, echo=False)
    session = sessionmaker()
    session.configure(bind=engine)
    return session()
        
def get_or_create(session, model, **kwargs):
    """
    Retreives or creates a new items
    
    http://stackoverflow.com/a/6078058/189134
    """
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance