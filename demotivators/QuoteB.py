from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import os
import datetime
import emoji

x = str(datetime.datetime.now()).partition('.')[0].replace(' ', ' в ')

class QuoteB:
    def __init__(self, quote_text, author_name):
        self._quote_text = quote_text
        self._author_name = author_name

    def create(self, file, result_filename='qresult.png', use_url=False,
            headline_text='Цитаты великих людей') \
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

        user_img = Image.new('RGBA', (1000, 550), color='#000000')

        drawer = ImageDraw.Draw(user_img)
        font_1 = ImageFont.truetype("fonts/Symbola.ttf", 35, encoding="UFT-8")
        font_2 = ImageFont.truetype("fonts/minecraft.ttf", 35, encoding="UFT-8")
        font_3 = ImageFont.truetype("fonts/minecraft.ttf", 30, encoding="UFT-8")

        size_headline = drawer.textsize(headline_text, font=font_2)

        if ":" in emoji.demojize(text):
            drawer = ImageDraw.Draw(user_img)
            font_1 = ImageFont.truetype("fonts/Symbola.ttf", 35,
                                        encoding="UFT-8")
            font_2 = ImageFont.truetype("fonts/minecraft.ttf", 35,
                                        encoding="UFT-8")
            font_3 = ImageFont.truetype("fonts/minecraft.ttf", 30,
                                        encoding="UFT-8")
            size = drawer.textsize(f"«{text[:-1]}»", font=font_1)
            size_a = (1000-size[0])/2
            size_b = ((500-size[1])/2)
            drawer.text((size_a, size_b), f"«{text[:-1]}»", fill='white', font=font_1, align='center', anchor=None)
            drawer.text((230, 400), '© ' + self._author_name, fill='white', font=font_3)
            drawer.text(((1000 - size_headline[0]) / 2, 25), headline_text, fill='white', font=font_2)
            drawer.text((500, 470), '#' + x, fill='white', font=font_3)
        else:
            drawer = ImageDraw.Draw(user_img)
            font_1 = ImageFont.truetype("fonts/minecraft.ttf", 35, encoding="UFT-8")
            font_2 = ImageFont.truetype("fonts/minecraft.ttf", 35, encoding="UFT-8")
            font_3 = ImageFont.truetype("fonts/minecraft.ttf", 30, encoding="UFT-8")
            size = drawer.textsize(f"«{text[:-1]}»", font=font_1)
            size_a = (1000-size[0])/2
            size_b = ((500-size[1])/2)
            drawer.text((size_a, size_b), f"«{text[:-1]}»", fill='white', font=font_1, align='center', anchor=None)
            drawer.text((230, 400), '© ' + self._author_name, fill='white', font=font_3)
            drawer.text(((1000 - size_headline[0]) / 2, 25), headline_text, fill='white', font=font_2)
            drawer.text((500, 470), '#' + x, fill='white', font=font_3)

        if use_url:
            p = requests.get(file)
            out = open(r'quote_picture.jpg', "wb")
            out.write(p.content)
            out.close()

            file = 'quote_picture.jpg'

        """
        Сглаживаем в форме круга фотографию автора цитаты
        """

        user_photo = Image.open(file).resize((150, 150)).convert("RGBA")
        width, height = user_photo.size
        user_photo.crop(((width - height) / 2, 0, (width + height) / 2, height))
        user_photo.resize((150, 150), Image.ANTIALIAS)
        mask = Image.new('L', (150 * 2, 150 * 2), 0)
        ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
        user_photo.putalpha(mask.resize((150, 150), Image.ANTIALIAS))
        user_img.paste(user_photo, (50, 370), mask=user_photo)

        user_img.save(result_filename)

        if use_url:
            os.remove('quote_picture.jpg')

        return True
