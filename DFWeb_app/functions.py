from typing import Union, List, Any

from DFWeb_app.models import User, Answer
from DFWeb_app import db

NUM_OF_ANSWERS = 13     # test.html needs editing (divs + JS event listeners) if answers are added/removed
ANSWERS = ['2', '3', '4', '2,4,5', '3', '2', '1,2,3,4', '4', '4', '3', '3', '2', '3']
MULTI_ANSWER_QUESTION = [4, 7]


def check_answers(answers1: list[str], answers2: list[str]) -> tuple[list[bool], list[bool]]:
    """
    Checks correctness of pre- and post-test answers
    :param answers1: list of pre-test answers
    :param answers2: list of post-test answers
    :return: both lists with replaced elements by true/false to indicate answer's correctness
    """
    for i in range(len(ANSWERS)):
        answers1[i] = answers1[i] == ANSWERS[i]
        answers2[i] = answers2[i] == ANSWERS[i]
    # noinspection PyTypeChecker
    return answers1, answers2


def make_user_data(sex: str, age: str, encountered: str) -> list[bool | int]:
    """
    Prepares user data to correct format for database
    :param sex: '0' for male, '1' for female
    :param age: '0'-'3' for age categories [<18, 18-25, 26-55, >55]
    :param encountered: '1' for encountered, 0 for did not encounter deepfakes
    :return: list(bool, int, bool) with re-typed inputs (0->False and 1->True)
    """
    data = []

    if sex == '0':
        data.append(False)
    else:
        data.append(True)

    data.append(int(age))

    if encountered == '0':
        data.append(False)
    else:
        data.append(True)

    return data


def add_user(data: list[bool | int], answers_1: list[bool], answers_2: list[bool]) -> None:
    """
    Adds user and their survey answers to the database
    :param data: data needed to create a user
    :param answers_1: answers of pre-test
    :param answers_2: answers of post-test
    """
    user = User(sex=data[0], age=data[1], encountered=data[2])
    db.session.add(user)
    db.session.commit()

    for question in range(1, NUM_OF_ANSWERS + 1):
        answer = Answer(user_id=user.id, question=question, answer_1=answers_1[question - 1],
                        answer_2=answers_2[question - 1])
        db.session.add(answer)
    db.session.commit()
    return


def print_query():
    u = User.query.order_by(User.id.desc()).first()
    if u:
        print(u.id, u.sex, u.age, u.encountered, u)
        a = Answer.query.order_by(Answer.id.desc()).first()
        print(a)
        b = Answer.query.filter_by(question=1).all()
        print(b)


def generate_feedback(answers: list[bool], answers_value: list[str]) ->\
        list[list[Union[bool, str]], list[str], int, int]:
    """
    Function generates feedback to post-test
    :param answers: list of correctness of post-test answers
    :param answers_value: list of post-test answers values
    :return: list with 2 lists: 1st contains list of users answers or true if their answer is correct;
                                2nd contains list of correct answers; and 2 ints corresponding to right and all answers
    """
    fb = []
    right = 0
    for i in range(len(ANSWERS)):
        if answers[i]:
            fb.append(True)
            right += 1
        else:
            fb.append(answers_value[i])

    feedback = [fb, ANSWERS, right, len(answers)]
    return feedback
