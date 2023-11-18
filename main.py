from PIL import Image
from txt import language, masks
from validation import validate


# print('Hi User! chose language. / Привет Пользователь! выбери язык.\n'
#       'Ru/En')
lang = 'ru'
mask_lg = 'masks_' + 'ru'
print(language[lang]['hi'])

menu = ''
for option in masks[mask_lg]:
    menu += f'{option}) {masks[mask_lg][str(option)]["name"]}\n'

img = Image.open(input('Введите путь к файлу: ')).convert('RGB')
print(type(img))

while True:
    print(f'{language[lang]["choosing"]} \n {menu}')
    option = validate(masks[mask_lg].keys())
    print(f'{masks[mask_lg][option]["name"]}\n{masks[mask_lg][option]["description"]}\n{language[lang]['qw']}')
    qw = validate(language[lang]['yn'])
    if qw == language[lang]['yn'][0]:
        if option == '0':
            exit()
        img = masks[mask_lg][option]['filter'].pixel_apply(img)
        img.save(input('Введите путь для сохранения: '))
