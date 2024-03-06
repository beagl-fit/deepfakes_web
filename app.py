from DFWeb_app import app, db
from DFWeb_app.models import Users, Answers


def db_init():
    with app.app_context():
        db.create_all()

        # user = Users()
        # # Add the user to the database session
        # db.session.add(user)
        # # Commit the changes to the database
        # db.session.commit()


if __name__ == '__main__':
    db_init()
    app.run(debug=True)
