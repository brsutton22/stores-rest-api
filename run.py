from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():  # Creates tables based on above imports
    db.create_all()
