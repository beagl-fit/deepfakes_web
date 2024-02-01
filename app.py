import os

from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm

app = Flask(__name__)

# from deepfakes_web.models import (User, Answer)
#
# app.config['SECRET_KEY'] = '1'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#
# db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html', title='Deepfakes')


@app.route('/dfg')
def general():
    return render_template('df_general.html', title='DF_General')


@app.route('/dfi')
def images():
    return render_template('df_images.html', title='DF_Images')


@app.route('/dfv')
def videos():
    return render_template('df_videos.html', title='DF_Video')


@app.route('/dfa')
def audio():
    return render_template('df_audio.html', title='DF_Audio')

@app.route('/dfe')
def end():
    return render_template('end.html', title='DF_Audio')

# @app.route('/info', methods=['GET', 'POST'])
# def get_info():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash(f'Login {form.username}', 'success')
#         return redirect(url_for('index'))
#     return render_template('info.html', title='Info', form=form)


if __name__ == '__main__':
    app.run(debug=True)
