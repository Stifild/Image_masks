from masks import Inversion, Uorhal, Contrast, Noise

language = {
    'ru': {
        'hi': 'Привет, тут ты можешь применить маски к фотографиям.',
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
        }
    },

    'masks_ru': {
        '1': {
            'name': 'Инверсия',
            'description': 'Инвертирует цвета',
            'filter': Inversion()
        },
        '2': {
            'name': 'Уорхал',
            'description': 'Делает фото в стиле Энди Уорхала',
            'filter': Uorhal()
        },
        '3': {
            'name': 'Контраст',
            'description': 'Делает изображение контрастней',
            'filter': Contrast()
        },
        '4': {
            'name': 'Шум',
            'description': 'Добавляет шум',
            'filter': Noise()
        },
        '0': {
            'name': 'Выход',
            'description': 'Выход из программы',
        }
    }
}