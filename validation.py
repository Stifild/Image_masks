from txt import language
from main import lang


def validate(list_values: list[str]) -> str:
    """
    Проверка ответа
    :param list_values: Список вариантов ответов
    :return: Ответ пользователя
    """
    choice = input(language[lang]['input']).lower()
    while choice.lower() not in list_values:
        ph = language[lang]['input error'] + list_values + '\n' + language[lang]['input']
        choice = input(ph).lower()
    return choice
