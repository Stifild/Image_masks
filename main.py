from PIL import Image
from txt import language, masks
from validation import validate


lang = 'en'
print('Hi User! chose language. / Привет Пользователь! выбери язык.\n'
      'Ru/En')
lang = validate(['ru', 'en'])
mask_lg = 'masks_' + lang
print(language[lang]['hi'])

menu = ''
for option in masks[mask_lg]:
    menu += f'{option}) {masks[mask_lg][str(option)]["name"]}'

img = Image.open(input()).convert('RGB')

while True:
    print(f'{language[lang]["choosing"]} \n {menu}')
    option = validate(masks[mask_lg].keys())
    print(f'{masks[mask_lg][option]["name"]}\n{masks[mask_lg][option]["description"]}\n{language[lang]['qw']}')
    qw = validate(language[lang]['yn'])
    if qw == language[lang]['yn'][0]:
        if option == '0':
            exit()
        print(masks[mask_lg][option]['filter'](input(language[lang]['input'])))
