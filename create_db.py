from app import app, db  # Import your Flask app and db instance

with app.app_context():
    db.create_all()  # Creates the todo.db file and the Todo table inside it
    print("Database and tables created!")