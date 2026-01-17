from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(_name_)
app.config('SECRET KEY') = 
app.config('SQLALCHEMY_DATABBASE_URI') = ''
db = SQLAlchemy(app)

from task-manager-app import routes



