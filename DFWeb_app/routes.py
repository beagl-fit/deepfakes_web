from flask import render_template, request, session, url_for, redirect
from DFWeb_app import app
from DFWeb_app.functions import check_answers, make_user_data, NUM_OF_ANSWERS
from DFWeb_app.models import User, Answer


@app.route('/', methods=['GET', 'POST'])
def index():
    language = 'en'
    lang = request.args.get('lang')
    if session.get('lang'):
        language = session.get('lang')
    if lang:
        language = lang

    session['lang'] = language

    if request.method == 'POST':
        answers1 = []
        answers2 = []
        for i in range(1, NUM_OF_ANSWERS + 1):
            question = 'q' + str(i) + 'a'
            answers1.append(session.get(question))
            answers2.append(request.form.get(question))

        ans1, ans2 = check_answers(answers1, answers2)
        user_data = make_user_data(session.get('sex'), session.get('age'), session.get('df'),)
        # user = User(sex=user_data[0], age=user_data[1], encountered=user_data[2])
        # TODO: remove print and add answers and user to db
        print(ans1, ans2)
        print(user_data)

        # clear session after finishing the course
        session.clear()

    if language == 'en':
        return render_template('index-en.html', title='Deepfakes')
    else:
        return render_template('index-cz.html', title='Deepfakes')


@app.route('/dfg', methods=['GET', 'POST'])
def general():
    if request.method == 'POST':
        for i in range(1, NUM_OF_ANSWERS + 1):
            question = 'q' + str(i) + 'a'
            q = request.form.get(question)
            # TODO: remove '' from an empty list and add None ????
            session[question] = q

    session['pre-test_completed'] = True
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
    # save session language to not lose it upon clearing session
    language = session.get('lang')
    # clear session, mainly to not load any previous test answers upon re-entering
    session.clear()
    session['lang'] = language

    if language == 'en':
        return render_template('info-en.html', title='Info')
    else:
        return render_template('info-cz.html', title='Info')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        session['sex'] = request.form.get('sex')
        session['age'] = request.form.get('age')
        session['df'] = request.form.get('df')

        # if a person chooses to skip the initial survey, go to general deepfakes
        if session.get('df') == '1':
            return redirect(url_for('general'))
    return render_template('test.html', title='Survey')
