from flask import render_template, request, session, url_for, redirect
from DFWeb_app import app
from DFWeb_app.forms import SessionForm
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


@app.route('/info', methods=['GET', 'POST'])
def info():
    return render_template('info.html', title='Info')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        session['sex'] = request.form.get('sex')
        session['age'] = request.form.get('age')
        session['df'] = request.form.get('df')

        if session.get('df') == '1':
            return render_template('df_general.html', title='DF_General')
    return render_template('test.html', title='Survey')
