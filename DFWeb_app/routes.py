from flask import render_template, url_for, redirect
from DFWeb_app import app
from DFWeb_app.forms import LoginForm     # TODO: this
from DFWeb_app.models import User, Answer


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
    return render_template('end.html', title='DF_End')


# , methods=['GET', 'POST']
@app.route('/info')
def info():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     flash(f'Login {form.username}', 'success')
    #     return redirect(url_for('index'))
    return render_template('info.html', title='Info')


@app.route('/test')
def test():
    # form = LoginForm()
    # if form.validate_on_submit():
    #     flash(f'Login {form.username}', 'success')
    #     return redirect(url_for('index'))
    return render_template('test.html', title='Survey')