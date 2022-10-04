from PIL import Image, ImageDraw, ImageFont
import textwrap
import datetime
import random
x = str(datetime.datetime.now()).partition('.')[0].replace(' ', ' в ')
class dphoto:
    def __init__(self, quote_text):
        self._quote_text = quote_text

    def create(self, file='dender.jpg', result_filename='qresult.png', use_url=False) \
            -> bool:
        text = ''
        lines = textwrap.wrap(self._quote_text, width=40)

        for i in lines:
            text = text + i + '\n'

        if len(text.splitlines()) > 5:
            lines = text.splitlines()[0:5]
            text = ''
            for i in lines:
                text = text + i + '\n'

        r = random.randint(1, 3)
        print(r)
        if r == 1:
            fille = ':/photos/dover.jpg'
        elif r == 2:
            fille = ':/photos/dnezer.jpg'
        else:
            fille = ':/photos/dender.jpg'
        user_img = Image.open(fille)
        drawer = ImageDraw.Draw(user_img)
        font_1 = ImageFont.truetype("minecraft.ttf", 100, encoding="UFT-8")

        size = drawer.textsize(f"«Ваш размер: {text[:-1]}»", font=font_1)
        size_a = (1366-size[0])/2
        size_b = ((1366-size[0])/2)+10
        size_c = ((705-size[1])/2)
        size_d = ((705-size[1])/2)+10
        drawer.text((size_b, size_d), f"«Твой размер: {text[:-1]}»", fill='black', font=font_1, align='center', anchor=None)
        drawer.text((size_a, size_c), f"«Твой размер: {text[:-1]}»", fill='white', font=font_1, align='center', anchor=None)
        user_img.save(result_filename)

        return True
