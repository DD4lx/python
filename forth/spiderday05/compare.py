import os

from PIL import Image

from compare_helper import get_compare


def compare():

    rotate_img = os.listdir('./rotate_img')
    crop_img = ['crop_img.png', 'crop_img2.png', 'crop_img3.png', 'crop_img4.png']
    result_list = []

    for i in range(len(crop_img)):
        count = 0
        flag = False
        filename2 = f'./{crop_img[i]}'
        img = Image.open(filename2)
        for j in range(4):
            if j != 0:
                img = img.rotate(-90)
                img.save(filename2)
                count += 1
            for rotate in rotate_img:
                filename1 = './rotate_img/' + rotate
                compare = get_compare(filename1, filename2)
                if compare > 80:
                    # img.show()
                    result_list.append(count)
                    flag = True
                    break
            if flag:
                break
    return result_list

def main():
    # html = get_page()
    # parse_html(html)
    print(compare())


if __name__ == '__main__':
    main()
