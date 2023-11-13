

language = {
    'ru': {
        'hi': 'Привет тут ты можешь применить фильтры к тексту и тем самым его стилизовать.',
        'choosing': 'Выбери из списка что тебе приглянулось.',
        'qw': 'Ты хочешь этот фильтр?',
        'yn': ['да', 'нет'],
        'input': 'Ввод: ',
        'input error': 'Пожалуйста, выберите из предложенных вариантов ',
    },
    'en': {
        'hi': 'Hi here you can apply filters to the text and thereby stylize it',
        'choosing': 'Choose from the list what you liked.',
        'qw': 'Do you want this filter?',
        'yn': ['yes', 'no'],
        'input': 'Input: ',
        'input error': 'Please choose from the suggested options ',
    }
}

masks = {
    'masks_en': {
        '1': {
            'name': 'CAPS',
            'description': 'Makes all letters BIG',
            'filter': None
        },
        '2': {
            'name': 'GOST',
            'description': 'Everything after the dot gets big. Does everything according to GOST.',
            'filter': None
        },
        '3': {
            'name': 'FeNcE',
            'description': 'WeLl, WhAt cAn i sAy fEnCe',
            'filter': None
        },
        '4': {
            'name': 'I🍦Want🍦Ice🍦Cream',
            'description': 'Instead🍦of🍦space🍦ice🍦cream',
            'filter': None
        },
        '0': {
            'name': 'Exit',
            'description': 'Exit from program',
            'filter': exit
        }
    },

    'masks_ru': {
        '1': {
            'name': 'КАПС',
            'description': 'Делает все буквы БОЛЬШИМИ',
            'filter': None
        },
        '2': {
            'name': 'ГОСТ',
            'description': 'Все после точки становится большим. Делает все по ГОСТу.',
            'filter': None
        },
        '3': {
            'name': 'ЗаБоР',
            'description': 'Ну чТо тУт сКаЗаТь зАбОр',
            'filter': None
        },
        '4': {
            'name': 'Я🍦Хочу🍦Мороженку',
            'description': 'Вместо🍦пробела🍦мороженка',
            'filter': None
        },
        '5': {
            'name': 'Выход',
            'description': 'Выход из программы',
            'filter': exit
        }
    }
}