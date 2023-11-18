from txt import language
# from main import lang


def validate(list_values: list[str]) -> str:
    """
    Проверка ответа
    :param list_values: Список вариантов ответов
    :return: Ответ пользователя
    """
    choice = input(language['ru']['input']).lower()
    while choice.lower() not in list_values:
        choice = input(f'{language['ru']['input error']} {list_values}\n{language['ru']['input']}').lower()
    return choice
