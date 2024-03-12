from flask import render_template, request, session, url_for, redirect
from DFWeb_app import app
from DFWeb_app.functions import (check_answers, make_user_data, add_user, create_download_files, generate_feedback,
                                 get_last_six, get_publications, add_publication, delete_publication,
                                 get_all_publications, NUM_OF_ANSWERS, MULTI_ANSWER_QUESTION)
from bcrypt import checkpw
from app import ADMIN_PWD


@app.route('/', methods=['GET', 'POST'])
def index():
    # set the default language to english
    language = 'en'
    lang = request.args.get('lang')

    # if there is a language is session, use this language instead
    if session.get('lang'):
        language = session.get('lang')

    # if user chooses to switch language, use it instead
    if lang:
        language = lang

    # if the method is post, survey (test) has been completed
    if request.method == 'POST':
        # clear session after finishing the course
        session.clear()

    # save language selection to session
    session['lang'] = language

    # get the last 6 publications
    publications = get_last_six()

    # renders page in user's language: XXX(-en/-cz).html extend XXX.html which itself is extension of layout.html
    if language == 'en':
        return render_template('index-en.html', title='Deepfakes', language='en',
                               publications=publications)
    else:
        return render_template('index-cz.html', title='Deepfakes', language='cs',
                               publications=publications)


@app.route('/dfg', methods=['GET', 'POST'])
def general():
    if request.method == 'POST':
        # if method is post - pre-test has been completed, therefore save answers to session
        for i in range(1, NUM_OF_ANSWERS + 1):
            answer = 'q' + str(i) + 'a'
            session[answer] = request.form.get(answer)

    if request.method == 'GET':
        # if method is get - pre-test has been skipped, therefore save default answers to session
        for i in range(1, NUM_OF_ANSWERS + 1):
            answer = 'q' + str(i) + 'a'
            session[answer] = ''
            if i not in MULTI_ANSWER_QUESTION:
                session[answer] = '1'

    # skipped or not, pre-test has been completed
    session['pre-test_completed'] = True
    if session.get('lang') == 'en':
        return render_template('df_general-en.html', title='DF_General', language='en')
    else:
        return render_template('df_general-cz.html', title='DF_Obecne', language='cs')


@app.route('/dfi')
def images():
    if session.get('lang') == 'en':
        return render_template('df_images-en.html', title='DF_Images', language='en')
    else:
        return render_template('df_images-cz.html', title='DF_Obrazky', language='cs')


@app.route('/dfv')
def videos():
    if session.get('lang') == 'en':
        return render_template('df_videos-en.html', title='DF_Video', language='en')
    else:
        return render_template('df_videos-cz.html', title='DF_Video', language='cs')


@app.route('/dfa')
def audio():
    if session.get('lang') == 'en':
        return render_template('df_audio-en.html', title='DF_Audio', language='en')
    else:
        return render_template('df_audio-cz.html', title='DF_Zvuk', language='cs')


@app.route('/dfe')
def end():
    if session.get('lang') == 'en':
        return render_template('end-en.html', title='DF_Tips', language='en')
    else:
        return render_template('end-cz.html', title='DF_Tipy', language='cs')


@app.route('/info', methods=['GET', 'POST'])
def info():
    # save session language to not lose it upon clearing session
    language = session.get('lang')
    # clear session, mainly to not load any previous test answers upon re-entering
    session.clear()
    session['lang'] = language

    if language == 'en':
        return render_template('info-en.html', title='Info', language='en')
    else:
        return render_template('info-cz.html', title='Info', language='cs')


@app.route('/test', methods=['GET', 'POST'])
def test():
    # test is called 3 times - after info, after course and then once more to provide feedback
    feedback = None
    # post method and pre-test_completed is not in session means that the previous page was info
    if request.method == 'POST' and not session.get('pre-test_completed'):
        # save form data to session for future use
        session['sex'] = request.form.get('sex')
        session['age'] = request.form.get('age')
        df = request.form.get('df')

        # swap the df value so that 0 (False) means not encountered and 1 (True) means encountered
        if df == '1':
            df = '0'
        else:
            df = '1'
        session['df'] = df

        # if a person chooses to skip the initial survey, go to general deepfakes instead of pre-test
        if df == '0':
            return redirect(url_for('general'))

    # if method is post but pre-test_completed is in session, this means the post-test has just been submitted
    elif request.method == 'POST':
        session['post-test_completed'] = True

        # save data to db and render feedback
        answers1 = []
        answers2 = []

        # get pre-test answers from session and post-test from just submitted form
        for i in range(1, NUM_OF_ANSWERS + 1):
            answer = 'q' + str(i) + 'a'
            answers1.append(session.get(answer))
            answers2.append(request.form.get(answer))

        # prepare user and answer data
        user_data = make_user_data(session.get('sex'), session.get('age'), session.get('df'))
        ans1, ans2 = check_answers(answers1, answers2)

        # add user and their answers to db
        add_user(user_data, ans1, ans2)

        # generate feedback and update session values for test answers
        feedback = generate_feedback(ans2, answers2)
        for i in range(1, NUM_OF_ANSWERS + 1):
            answer = 'q' + str(i) + 'a'
            session[answer] = request.form.get(answer)

    # no matter what the previous page was, render test template
    if session.get('lang') == 'en':
        return render_template('test-en.html', title='Survey', language='en', feedback=feedback)
    else:
        return render_template('test-cz.html', title='Pruzkum', language='cs', feedback=feedback)


@app.route('/playground', methods=['GET', 'POST'])
def pg():
    if session.get('lang') == 'en':
        return render_template('playground-en.html', title='Playground', language='en')
    else:
        return render_template('playground-cz.html', title='Hřiště', language='cs')


@app.route('/publications')
def pubs():
    page = request.args.get('page', 1, type=int)
    per_page = 6

    publications = get_publications(page, per_page)

    if session.get('lang') == 'en':
        return render_template('publications-en.html', title='Publications', language='en',
                               publications=publications, page=page)
    else:
        return render_template('publications-cz.html', title='Publikace', language='cs',
                               publications=publications, page=page)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    failed = False

    # login to admin
    if request.method == 'POST' and not session.get('admin'):
        # get and check password passed to admin page
        entered_password = request.form.get('password')
        if checkpw(entered_password.encode('utf-8'), ADMIN_PWD):
            session['admin'] = True
        else:
            failed = True

    # db manipulation - add/delete publications
    elif request.method == 'POST':
        if request.form.get('name'):
            add_publication(request.form.get('name'), request.form.get('desc'), request.form.get('link'))
        elif request.form.get('hidden_pub_id'):
            delete_publication(int(request.form.get('hidden_pub_id')))

    create_download_files()
    publications = get_all_publications()
    return render_template('admin.html', title='Admin', language='en', failed=failed,
                           pubs=publications)
