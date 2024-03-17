from DFWeb_app import app, db
# from getpass import getpass
# from bcrypt import gensalt, hashpw
from datetime import timedelta


def db_init() -> None:
    """
    Creates database
    """
    with app.app_context():
        db.create_all()


def file_init():
    f = open('/static/files/users.cvs', "w")
    f.writelines('')
    f = open('/static/files/answers.cvs', "w")
    f.writelines('')

    # with open('/static/files/users.cvs', "w") as f:
    #     f.write(pass)

# def set_admin() -> bytes:
#     """
#     Gets password from user and hashes it
#     :return: hashed password
#     """
#     password = True
#     password_check = False
#
#     while password != password_check:
#         password = getpass("Enter your password: ")
#         password_check = getpass("Enter the password again: ")
#         if password != password_check:
#             print("Passwords do not match, please try again.")
#
#     print("Password was set successfully!")
#     return hashpw(password.encode('utf-8'), gensalt())


# ADMIN_PWD = set_admin()

if __name__ == '__main__':
    db_init()
    file_init()
    app.permanent_session_lifetime = timedelta(days=7)
    app.run(debug=True)
