import os

from PIL import Image

img_list = os.listdir('./small')
for img in img_list:
    name = img
    img = Image.open(f'./small/{img}')
    img.show()
    save_code = input('Y/N:')
    if save_code == 'Y':
        img.save(f'./rotate_img/{name}')
        continue
    while True:
        img = img.rotate(90)
        img.show()
        save_code = input('Y/N:')
        if save_code == 'Y':
            img.save(f'./rotate_img/{name}')
            break
print('调整完成')
