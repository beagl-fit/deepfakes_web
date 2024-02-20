NUM_OF_ANSWERS = 13     # test.html needs editing (divs + JS event listeners) if answers are added/removed
ANSWERS = ['2', '3', '4', '2,4,5', '3', '2', '1,2,3,4', '4', '4', '3', '3', '2', '3']


def check_answers(answers1, answers2):
    """
    Checks correctness of pre- and post-test answers
    :param answers1: list of pre-test answers
    :param answers2: list of post-test answers
    :return: both lists with replaced elements by true/false to indicate answer's correctness
    """
    for i in range(len(ANSWERS)):
        answers1[i] = answers1[i] == ANSWERS[i]
        answers2[i] = answers2[i] == ANSWERS[i]
    return answers1, answers2


def make_user_data(sex, age, encountered):
    """
    Prepares user data to correct format for database
    :param sex: string - 0 for male, 1 for female
    :param age: string - 0-3 for age categories [<18, 18-25, 26-55, >55]
    :param encountered: string - 0 for encountered, 1 for did not encounter deepfakes
    :return: list (bool, int, bool) 0->False and 1->True
    """
    data = []

    if sex == '0':
        data.append(False)
    else:
        data.append(True)

    # print(age)
    data.append(int(age))

    if encountered == '0':
        data.append(False)
    else:
        data.append(True)

    return data
