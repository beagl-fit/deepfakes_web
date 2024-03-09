from DFWeb_app import app, db
from getpass import getpass
from bcrypt import gensalt, hashpw


def db_init() -> None:
    """
    Creates database
    """
    with app.app_context():
        db.create_all()


def set_admin() -> bytes:
    """
    Gets password from user and hashes it
    :return: hashed password
    """
    password = True
    password_check = False

    while password != password_check:
        password = getpass("Enter your password: ")
        password_check = getpass("Enter the password again: ")
        if password != password_check:
            print("Passwords do not match, please try again.")

    print("Password was set successfully!")
    return hashpw(password.encode('utf-8'), gensalt())


# ADMIN_PWD = set_admin()
ADMIN_PWD = "a"

if __name__ == '__main__':
    db_init()
    app.run(debug=True)
