from vkbottle.bot import Message
import os
from vkbottle.dispatch.rules.base import *
from vkbottle.tools import *
from vkbottle import CaptchaError, BaseMiddleware
import config
from demotivators import Demotivator, Quote, QuoteB, dphoto
import random
import datetime
import asyncio
from config import *
import time
import json
from gtts import gTTS
x = str(datetime.datetime.now()).partition('.')[0].replace(' ', ' в ')
print(x)
async def reg(user_id):
    db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
    result = db_object.fetchone()
    if not result:
        db_object.execute(
            "INSERT INTO users(id, santimeters, rules, users_count, name_surname, admin, ban) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (user_id, 0, 0, 0, 0, 0, 0))
        db_connection.commit()

class banan(BaseMiddleware[Message]):
    async def pre(self):
        try:
            db_object.execute(f'SELECT ban FROM users WHERE id = {self.event.from_id}')
            result = db_object.fetchone()[0]
            if result == 1:
                self.stop("Пользователь в бане")
            elif self.event.chat_id == 58:
                self.stop("Не тот чат")
        except:
            user_id = self.event.from_id
            await reg(user_id)
            db_object.execute(f'SELECT ban FROM users WHERE id = {self.event.from_id}')
            result = db_object.fetchone()[0]
            if result == 1:
                self.stop("Пользователь в бане")
            elif self.event.chat_id == 58:
                self.stop("Не тот чат")
    async def post(self):
        if self.event.text.startswith('/'):
            db_object.execute(f"UPDATE users SET users_count = users_count + 1 WHERE id = 1")
            db_connection.commit()
        elif self.handlers:
            db_object.execute(f"UPDATE users SET users_count = users_count + 1 WHERE id = 2")
            db_connection.commit()

async def captcha_handler(e: CaptchaError) -> str:
    solved = await http.request_json(
        url='https://vk-cptch-solver.herokuapp.com/captcha',
        json={
            'token': 'd41bf683e69ddacca23583ca9d3e6b5d75b9a38594620f989cd150a28da7134b',
            'sid': e.sid,
        },
    )

    return solved["solve"]

@user.on.chat_message(text=['/сколько у <name> <what>?'])
async def main(message: Message, name, what):
    user_id = message.from_id
    await reg(user_id)
    try:
        random1 = random.randint(40, 50)
        msg_id = await message.reply(f'У {name} {random1} {what}')
        await asyncio.sleep(0.6)
        random2 = random.randint(40, 50)
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'У {name} {random2} {what}.'
        )
        await asyncio.sleep(0.6)
        random3 = random.randint(40, 50)
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'У {name} {random3} {what}..'
        )
        await asyncio.sleep(0.6)
        random4 = random.randint(40, 50)
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'У {name} {random4} {what}...'
        )
        await asyncio.sleep(0.6)
        random5 = random.randint(40, 50)
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'У {name} {random5} {what}'
        )
        await asyncio.sleep(0.6)
        random6 = random.randint(40, 50)
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'У {name} {random6} {what}.'
        )
        await asyncio.sleep(0.6)
        random7 = random.randint(40, 50)
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'У {name} {random7} {what}..'
        )
        await asyncio.sleep(0.6)
        random8 = random.randint(40, 50)
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'У {name} {random8} {what}...'
        )
        await asyncio.sleep(0.6)
        random9 = random.randint(40, 50)
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'У {name} {random9} {what}'
        )
        await asyncio.sleep(5)
        await user.api.messages.delete(
            peer_id=message.peer_id,
            message_ids=msg_id.message_id,
            delete_for_all=1)
        await message.reply('Выполнено и удалено')
    except 'final':
        await message.reply('Диапазон должен быть указан числом')

@user.on.chat_message(text=['/хуй'])
async def wrappe(message: Message):
    user_id = message.from_id
    await reg(user_id)
    db_object.execute(f"UPDATE users SET santimeters = santimeters + 1 WHERE id = {user_id}")
    db_connection.commit()
    db_object.execute(f'SELECT santimeters FROM users WHERE id = {user_id}')
    result = db_object.fetchone()
    msg_id = await message.reply(f"""Теперь твой хуй {result[0]} см""")
    await asyncio.sleep(3)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)
    msg_id_l = await message.reply('Выполнено и удалено')
    await asyncio.sleep(5)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id_l.message_id,
        delete_for_all=1)

@user.on.chat_message(text=['/хуй-'])
async def wrappe(message: Message):
    user_id = message.from_id
    await reg(user_id)
    db_object.execute(f"UPDATE users SET santimeters = santimeters - 1 WHERE id = {user_id}")
    db_connection.commit()
    db_object.execute(f'SELECT santimeters FROM users WHERE id = {user_id}')
    result = db_object.fetchone()
    msg_id = await message.reply(f"""Теперь твой хуй {result[0]} см""")
    await asyncio.sleep(3)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)
    msg_id_l = await message.reply('Выполнено и удалено')
    await asyncio.sleep(5)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id_l.message_id,
        delete_for_all=1)

@user.on.chat_message(text=['/спам <text1> <num>'])
async def spam(message: Message, text1, num):
    user_id = message.from_id
    await reg(user_id)
    if message.from_id == 518705815:
        for i in range(int(num)):
            msg_id = await message.reply(f"""{text1}""")
            await asyncio.sleep(5)
            await user.api.messages.delete(
                peer_id=message.peer_id,
                message_ids=msg_id.message_id,
                delete_for_all=1)
    else:
        msg_id1 = await message.reply("""Ты не достоин""")
        await asyncio.sleep(5)
        await user.api.messages.delete(
            peer_id=message.peer_id,
            message_ids=msg_id1.message_id,
            delete_for_all=1)
        await message.reply('Выполнено и удалено')

@user.on.chat_message(text=['/ban <coutry>'])
async def spam(message: Message, coutry):
    user_id = message.from_id
    await reg(user_id)
    msg_id = await message.reply('Подключаюсь к базе данных')
    await asyncio.sleep(0.5)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)
    msg_id1 = await message.reply('Ищу ключи доступа.')
    await asyncio.sleep(0.5)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id1.message_id,
        delete_for_all=1)
    msg_id2 = await message.reply('Отправляю запросы..')
    await asyncio.sleep(0.5)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id2.message_id,
        delete_for_all=1)
    msg_id3 = await message.reply('Получаю ответы...')
    await asyncio.sleep(0.5)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id3.message_id,
        delete_for_all=1)
    if message.from_id == 518705815:
        msg_id4 = await message.reply(f'{coutry} была успешно забанена Богданом')
        await asyncio.sleep(5)
        await user.api.messages.delete(
            peer_id=message.peer_id,
            message_ids=msg_id4.message_id,
            delete_for_all=1)
        await message.reply('Выполнено и удалено')
    else:
        msg_id5 = await message.reply(f'У тебя нету доступа, попроси у Богдана разрешение')
        await asyncio.sleep(5)
        await user.api.messages.delete(
            peer_id=message.peer_id,
            message_ids=msg_id5.message_id,
            delete_for_all=1)

@user.on.chat_message(text='/статус <stat>')
async def spam(message: Message, stat):
    user_id = message.from_id
    await reg(user_id)
    if message.from_id == 518705815:
        if stat == '1':
            stat1 = await user.api.messages.set_activity(user_id=message.from_id, type='typing',
                                                         peer_id=message.peer_id)
            print(stat1)
            await message.reply('Статус выставлен на печатный')
        elif stat == '2':
            stat2 = await user.api.messages.set_activity(user_id=message.from_id, type='audiomessage',
                                                         peer_id=message.peer_id)
            print(stat2)
            await message.reply('Статус выставлен на голосовой')
        else:
            await message.reply("""Доступно только 2 типа:\n1-Печатный\n2-Голосовой.""")
    else:
        await message.reply('У меня нет доступа к твоему аккаунту. Кидай свой токен в лс быстро')

@user.on.chat_message(text=['/бал'])
async def vkc(message: Message):
    user_id = message.from_id
    await reg(user_id)
    bal = str(merchant.get_balance(message.from_id))
    msg_id = await message.reply(f'Ваш баланс Vk Coin: {bal.partition(":")[2].partition("}")[0]}')
    await asyncio.sleep(120)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text=['/бал @<name>', '/бал [<name>|<rfc>]'])
async def vkc(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    user_id = await user.api.utils.resolve_screen_name(name)
    print(user_id)
    bal = str(merchant.get_balance(user_id.object_id))
    user_name = await user.api.users.get(user_id.object_id)
    msg_id = await message.reply(
        f'Баланс [id{user_id.object_id}|{user_name[0].first_name}] Vk Coin равен: {bal.partition(":")[2].partition("}")[0]}')
    await asyncio.sleep(120)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(AttachmentTypeRule("photo"))
async def wrapper(message: Message):
        user_id = message.from_id
        await reg(user_id)
        if message.text != "" and message.text.find('/дем') == 0:
            text = message.text.splitlines()
            photo = message.attachments[0].photo.sizes[-1].url
            p = requests.get(photo)
            out = open(r'demotivator.jpg', "wb")
            out.write(p.content)
            out.close()
            if len(text) < 2:
                text.append('')
            dem = Demotivator(text[0].partition('/дем')[2], text[1])
            dem.create('demotivator.jpg')
            doc = await PhotoMessageUploader(user.api).upload(
                'demresult.jpg', peer_id=message.peer_id
            )
            await message.reply(attachment=doc)
            os.remove('demresult.jpg')
            os.remove('demotivator.jpg')
        else:
            await asyncio.sleep(0.00000001)

@user.on.chat_message(text='/дем<text>')
async def wrapper(message: Message):
    if message.reply_message is not None:
        user_id = message.from_id
        await reg(user_id)
        text = message.text.splitlines()
        try:
            photo = message.reply_message.attachments[0].photo.sizes[-1].url
        except:
            try:
                photo = message.reply_message.attachments[0].doc.url
            except:
                if message.reply_message.text != '':
                    msg_id = await message.answer('Чтобы продемотивировать текст используйте, /цитата')
                    await asyncio.sleep(60)
                    await user.api.messages.delete(
                        peer_id=message.peer_id,
                        message_ids=msg_id.message_id,
                        delete_for_all=1)
                elif message.reply_message.attachments[0].type.name == 'STICKER':
                    msg_id = await message.reply('Пока что не возможно продемотивировать стикер')
                    await asyncio.sleep(60)
                    await user.api.messages.delete(
                        peer_id=message.peer_id,
                        message_ids=msg_id.message_id,
                        delete_for_all=1)

                else:
                    msg_id = await message.answer('Произошла ошибка, напиши [id518705815|Богдану]')
                    await asyncio.sleep(60)
                    await user.api.messages.delete(
                        peer_id=message.peer_id,
                        message_ids=msg_id.message_id,
                        delete_for_all=1)

        p = requests.get(photo)
        out = open(r'demotivator.jpg', "wb")
        out.write(p.content)
        out.close()
        if len(text) < 2:
            text.append('')
        dem = Demotivator(text[0].partition('/дем')[2], text[1])
        dem.create('demotivator.jpg')
        doc = await PhotoMessageUploader(user.api).upload(
            'demresult.jpg', peer_id=message.peer_id
        )
        msg_id = await message.reply(attachment=doc)
        os.remove('demresult.jpg')
        os.remove('demotivator.jpg')
    else:
        msg_id = await message.reply('Чтобы создать демотиватор надо отметить сообщение')

@user.on.chat_message(text='/ауф')
async def wrapper(message: Message):
    user_id = message.from_id
    await reg(user_id)
    auf = random.choice(data)
    print(auf)
    msg_id = await message.reply(f'{auf}')
    await asyncio.sleep(180)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text='/интересный факт')
async def wrapper(message: Message):
    user_id = message.from_id
    await reg(user_id)
    user_id = message.from_id
    await reg(user_id)
    fact = random.choice(data1)
    msg_id = await message.reply(f'{fact}')
    await asyncio.sleep(240)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.message(text='/команды')
async def wrapper(message: Message):
    user_id = message.from_id
    await reg(user_id)
    msg_id = await message.reply('На данный момент существуют 0 команд:\n\n')
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 1 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> от 40 до 50\n"""
    )
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 2 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 3 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 4 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 5 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 6 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 7 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 8 команд:\n\n
1. /Сколько у <name> <args>? - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - Показывает либо ваш либо размер пользователя.\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 9 команд:\n\n
1. /Сколько у <name> <args>? - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - Показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по размерам.\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 10 команд:\n\n
1. /Сколько у <name> <args>? - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> -показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - Показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по размерам.\n
10. /мем - Отправляет случайный мем.\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 10 команд:\n\n
1. /Сколько у <name> <args>? -Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - Показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по размерам.\n
10. /мем - Отправляет случайный мем.\n
11. /стики <user> - Показывает стикерпаки пользователя.\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 10 команд:\n\n
1. /Сколько у <name> <args>? -Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - Показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по размерам.\n
10. /мем - Отправляет случайный мем.\n
11. /стики <user> - Показывает стикерпаки пользователя.\n
12. /инвайт <ссылка> - Автоматически добавляет бота в беседу\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 10 команд:\n\n
1. /Сколько у <name> <args>? - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - Показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по размерам.\n
10. /мем - Отправляет случайный мем.\n
11. /стики <user> - Показывает стикерпаки пользователя.\n
12. /инвайт <ссылка> - Автоматически добавляет бота в беседу\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 10 команд:\n\n
1. /Сколько у <name> <args>? - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - Показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по размерам.\n
10. /мем - Отправляет случайный мем.\n
11. /стики <user> - Показывает стикерпаки пользователя.\n
12. /инвайт <ссылка> - Автоматически добавляет бота в беседу\n
13. /озвучить <text> - Озвучивает ваш текст\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
    peer_id = message.peer_id,
              message_id = msg_id.message_id,
                           message = f"""На данный момент существуют 10 команд:\n\n
1. /Сколько у <name> <args>? - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - Показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по размерам.\n
10. /мем - Отправляет случайный мем.\n
11. /стики <user> - Показывает стикерпаки пользователя.\n
12. /инвайт <ссылка> - Автоматически добавляет бота в беседу\n
13. /озвучить <text> - Озвучивает ваш текст\n\n
ЭТОТ БОТ РАБОТАЕТ ТОЛЬКО В ЧАТАХ\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 10 команд:\n\n
1. /Сколько у <name> <args>? - Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> - показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по размерам.\n
10. /мем - Отправляет случайный мем.\n
11. /стики <user> - Показывает стикерпаки пользователя.\n
12. /инвайт <ссылка> - Автоматически добавляет бота в беседу (ТОЛЬКО ЛИЧНЫЕ СООБЩЕНИЯ)\n
13. /озвучить <text> - Озвучивает ваш текст\n\n
ЭТОТ БОТ РАБОТАЕТ ТОЛЬКО В ЧАТАХ\n\n
P.S. Бот уже стоит на хосте, но с 28 ноября хост будит стоит денег, так что скидуемся ему [id518705815|Богдан], иначе всем бан(\n""")
    await asyncio.sleep(120)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text='/цитата нью')
async def quote(message: Message):
    user_id = message.from_id
    await reg(user_id)
    if message.reply_message is not None:
        if message.reply_message.text != '':
            user_ava = await user.api.users.get(user_ids=message.reply_message.from_id, fields='photo_max')
            user_photo = user_ava[0].photo_max
            name = user_ava[0].first_name + ' ' + user_ava[0].last_name
            img_data = requests.get(user_photo).content
            with open('userphoto.jpg', 'wb') as handler:
                handler.write(img_data)
            dem = Quote(message.reply_message.text, name)
            dem.create(user_photo, use_url=True)
            photo_upd = await PhotoMessageUploader(user.api).upload(
                'qresult.png', peer_id=message.peer_id
            )
            await message.reply(attachment=photo_upd)
            os.remove('qresult.png')
            os.remove('userphoto.jpg')
            print(message.reply_message.attachments[0].type)
        elif message.reply_message.text == '' and message.reply_message.attachments[0].type.name == 'PHOTO':
            msg_id = await message.reply('Чтобы процитировать фото, надо использовать команду /дем <текст>')
            await asyncio.sleep(60)
            await user.api.messages.delete(
                peer_id=message.peer_id,
                message_ids=msg_id.message_id,
                delete_for_all=1)

        elif message.reply_message.text == '' and message.reply_message.attachments[0].type.name == 'STICKER':
            msg_id = await message.reply('Пока что не возможно процитировать стикер')
            await asyncio.sleep(60)
            await user.api.messages.delete(
                peer_id=message.peer_id,
                message_ids=msg_id.message_id,
                delete_for_all=1)

        else:
            msg_id = await message.answer('Произошла ошибка, напиши [id518705815|Богдану]')
            await asyncio.sleep(60)
            await user.api.messages.delete(
                peer_id=message.peer_id,
                message_ids=msg_id.message_id,
                delete_for_all=1)

    elif message.reply_message is None:
        msg_id = await message.reply('Чтобы процитировать сообщение,ты должен на него ответить')
        await asyncio.sleep(60)
        await user.api.messages.delete(
            peer_id=message.peer_id,
            message_ids=msg_id.message_id,
            delete_for_all=1)

@user.on.chat_message(text='/цитата')
async def quote(message: Message):
    user_id = message.from_id
    await reg(user_id)
    if message.reply_message is not None:
        if message.reply_message.text != '':
            user_ava = await user.api.users.get(user_ids=message.reply_message.from_id, fields='photo_max')
            user_photo = user_ava[0].photo_max
            name = user_ava[0].first_name + ' ' + user_ava[0].last_name
            img_data = requests.get(user_photo).content
            with open('userphoto.jpg', 'wb') as handler:
                handler.write(img_data)
            dem = QuoteB(message.reply_message.text, name)
            dem.create(user_photo, use_url=True)
            photo_upd = await PhotoMessageUploader(user.api).upload(
                'qresult.png', peer_id=message.peer_id
            )
            msg_id = await message.reply('Чтобы создать по новому дизайну, команда /цитата нью')
            await asyncio.sleep(0.5)
            await message.reply(attachment=photo_upd)
            await asyncio.sleep(5)
            await user.api.messages.delete(
                peer_id=message.peer_id,
                message_ids=msg_id.message_id,
                delete_for_all=1)
            os.remove('qresult.png')
            os.remove('userphoto.jpg')
        elif message.reply_message.text == '' and message.reply_message.attachments[0].type.name == 'PHOTO':
            msg_id = await message.reply('Чтобы процитировать фото, надо использовать команду /дем <текст>')
            await asyncio.sleep(60)
            await user.api.messages.delete(
                peer_id=message.peer_id,
                message_ids=msg_id.message_id,
                delete_for_all=1)
        elif message.reply_message.text == '' and message.reply_message.attachments[0].type.name == 'STICKER':
            msg_id = await message.reply('Пока что не возможно процитировать стикер')
            await asyncio.sleep(60)
            await user.api.messages.delete(
                peer_id=message.peer_id,
                message_ids=msg_id.message_id,
                delete_for_all=1)

        else:
            msg_id = await message.answer('Произошла ошибка, напиши [id518705815|Богдану]')
            await asyncio.sleep(60)
            await user.api.messages.delete(
                peer_id=message.peer_id,
                message_ids=msg_id.message_id,
                delete_for_all=1)

    elif message.reply_message is None:
        msg_id = await message.reply('Чтобы процитировать сообщение,ты должен на него ответить')
        await asyncio.sleep(60)
        await user.api.messages.delete(
            peer_id=message.peer_id,
            message_ids=msg_id.message_id,
            delete_for_all=1)

@user.on.chat_message(text='/чекхуй топ')
async def dicktop(message: Message):
    user_id = message.from_id
    await reg(user_id)
    db_object.execute(f'SELECT * FROM users ORDER BY santimeters DESC LIMIT 10')
    result = db_object.fetchall()
    reply_message = "Топ по размерам:\n"
    msg_id = await message.answer(reply_message)
    for i, item in enumerate(result):
        print(item[0])
        users_name = await user.api.users.get(item[0])
        reply_message += f'{i + 1}.  [id{item[0]}|{users_name[0].first_name}] - {item[1]} см.\n'
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'{reply_message}')
    await asyncio.sleep(120)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text='/чекхуй')
async def dickinfo(message: Message):
    user_id = message.from_id
    await reg(user_id)
    db_object.execute(f'SELECT santimeters FROM users WHERE id = {user_id}')
    result123 = db_object.fetchone()
    dem = dphoto(str(result123[0]))
    dem.create()
    photo_upd = await PhotoMessageUploader(user.api).upload(
        'qresult.png', peer_id=message.peer_id
    )
    await asyncio.sleep(0.5)
    msg_id = await message.reply(attachment=photo_upd)
    os.remove('qresult.png')

@user.on.chat_message(text=['/чекхуй @<name>', '/чекхуй [<name>|<rfc>'])
async def dickinfo(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    user_id1 = await user.api.utils.resolve_screen_name(name)
    users_name1 = await user.api.users.get(user_id1.object_id)
    db_object.execute(f'SELECT santimeters FROM users WHERE id = {user_id1.object_id}')
    result = db_object.fetchone()
    msg_id = await message.reply(f'Размер [id{user_id1.object_id}|{users_name1[0].first_name}а] : {result[0]}')
    await asyncio.sleep(60)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text='/сп <name>')
async def spam(message: Message, name):
    a = 0
    db_object.execute(f"SELECT admin FROM users WHERE id = {message.from_id}")
    result = db_object.fetchone()[0]
    if result == 1:
        msg_id = await message.reply(f'{name} {a}')
        while True:
            a += 1
            await message.reply(f'{name} {a}')
    else:
        await asyncio.sleep(0.000001)

@user.on.chat_message(text=['/бан @<name>', '/бан [<name>|<rfc>]'])
async def ban(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    db_object.execute(f"SELECT admin FROM users WHERE id = {message.from_id}")
    result = db_object.fetchone()[0]
    if result == 1:
        user_id = await user.api.utils.resolve_screen_name(name)
        if user_id.object_id is not None:
            db_object.execute(f'SELECT ban FROM users WHERE id = {user_id.object_id}')
            result123 = db_object.fetchone()[0]
            if result123 == 1:
                await message.answer('Пользователь уже в бане')
            else:
                print(user_id.object_id)
                db_object.execute(f"UPDATE users SET ban = 1 WHERE id = {user_id.object_id}")
                db_connection.commit()
                db_object.execute(f'SELECT ban FROM users WHERE id = {user_id.object_id}')
                result = db_object.fetchone()[0]
                print(result)
                if result == 1:
                    await message.answer('Пользователь успешно забанен')
                else:
                    await message.answer('Не удалось забанить пользователя')
        else:
            await message.reply('Пользователь не в найден в базе')
    else:
        await asyncio.sleep(0.0001)

@user.on.chat_message(text=['/разбан @<name>', '/разбан [<name>|<rfc>]'], )
async def ban(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    db_object.execute(f"SELECT admin FROM users WHERE id = {message.from_id}")
    result = db_object.fetchone()[0]
    if result == 1:
        user_id = await user.api.utils.resolve_screen_name(name)
        if user_id.object_id is not None:
            user_id = await user.api.utils.resolve_screen_name(name)
            db_object.execute(f'SELECT ban FROM users WHERE id = {user_id.object_id}')
            result = db_object.fetchone()[0]
            print(result)
            if result == 0:
                await message.answer('Пользователь не забанен')
            else:
                print(user_id.object_id)
                db_object.execute(f"UPDATE users SET ban = 0 WHERE id = {user_id.object_id}")
                db_connection.commit()
                db_object.execute(f'SELECT ban FROM users WHERE id = {user_id.object_id}')
                result = db_object.fetchone()[0]
                print(result)
                if result == 0:
                    await message.answer('Пользователь успешно забанен')
                else:
                    await message.answer('Не удалось забанить пользователя')
        else:
            await message.reply('Пользователь не в найден в базе')
    else:
        await asyncio.sleep(0.0001)

@user.on.chat_message(text=['/адм команды'])
async def command(message: Message):
    msg_id = await message.answer("""Команды администрации:\n\n
1. /спам <text> <num> - Невидимо спамит <text>'ом <num> раз\n
2. /ban <args> - Фейк-бан\n
3. /статус <args> - Меняет статус в беседе (Например: Пользователь печатает...)\n
4. /сп <text> - Спамит в беседе <text>'ом\n
5. /бан <name> & /разбан <name> - Банит/Разбанивает пользователя в боте\n""")
    await asyncio.sleep(60)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text=['/айди @<name>', '/айди [<name>|<rfc>]'])
async def abt(message: Message, name):
    user_id = await user.api.utils.resolve_screen_name(name)
    await message.answer(f'Айди: {user_id.object_id}')

@user.on.chat_message(text='/пинг')
async def ping(message: Message):
    user_id = message.from_id
    await reg(user_id)
    start_time = time.time()
    msg_id = await message.answer('Пингую...')
    await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'Понг: {round(time.time()-start_time, 1)} секунд'
            )
    await asyncio.sleep(10)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text='/мем')
async def meme(message: Message):
    user_id = message.from_id
    await reg(user_id)
    r = random.randint(1, 316)
    if r < 10:
        photo_upd = await PhotoMessageUploader(user.api).upload(
                f'photos/memes/00{r}.jpg', peer_id=message.peer_id
            )
    elif r < 100:
        photo_upd = await PhotoMessageUploader(user.api).upload(
                f'photos/memes/0{r}.jpg', peer_id=message.peer_id
            )
    else:
        photo_upd = await PhotoMessageUploader(user.api).upload(
                f'photos/memes/{r}.jpg', peer_id=message.peer_id
            )
    msg_id = await message.reply(message='https://vk.com/wall599457498_784', attachment=photo_upd)
    await asyncio.sleep(180)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text=['/админ @<name>', '/админ [<name>|<rfc>'])
async def adminn(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    if message.from_id == 518705815:
        user_id = await user.api.utils.resolve_screen_name(name)
        db_object.execute(f"SELECT admin FROM users WHERE id = {user_id.object_id}")
        result = db_object.fetchone()[0]
        if result == 1:
            await message.answer('Пользователь уже является администратором')
        else:
            db_object.execute(f"UPDATE users SET admin = 1 WHERE id = {user_id.object_id}")
            db_connection.commit()
            db_object.execute(f"SELECT admin FROM users WHERE id = {user_id.object_id}")
            result = db_object.fetchone()[0]
            if result == 1:
                await message.answer('Пользователю выдана роль администратора')
            else:
                await message.answer('Не удалось выдать администратора')

@user.on.chat_message(text=['/админ снять @<name>', '/админ снять [<name>|<rfc>'])
async def adminn(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    if message.from_id == 518705815:
        user_id = await user.api.utils.resolve_screen_name(name)
        db_object.execute(f"SELECT admin FROM users WHERE id = {user_id.object_id}")
        result = db_object.fetchone()[0]
        if result == 0:
            await message.answer('Пользователь не является администратором')
        else:
            db_object.execute(f"UPDATE users SET admin = 0 WHERE id = {user_id.object_id}")
            db_connection.commit()
            db_object.execute(f"SELECT admin FROM users WHERE id = {user_id.object_id}")
            result = db_object.fetchone()[0]
            if result == 0:
                await message.answer('Пользователю выдана роль участника')
            else:
                await message.answer('Не удалось выдать роль участника')

@user.on.chat_message(text='/статистика')
async def stats(message: Message):
    db_object.execute(f'SELECT users_count FROM users WHERE id = 1')
    result = db_object.fetchone()[0]
    db_object.execute(f'SELECT users_count FROM users WHERE id = 2')
    result2 = db_object.fetchone()[0]
    await message.answer(f'Надйено команд: {result}\nОбработано команд: {result2}\nНе обработано: {result-result2}')

@user.on.chat_message(text=['/стики @<text>', '/стики [<text>|<rfc>'])
async def stick(message: Message, text):
        user_id1 = await user.api.utils.resolve_screen_name(text)
        user_id = user_id1.object_id
        name = await user.api.users.get(user_id)
        data2 = f'https://stickers.loupg.one/user/{user_id}'
        params = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117',
            'vk-auth': 'vk_access_token_settings=&vk_app_id=7475013&vk_are_notifications_enabled=0&vk_is_app_user=0&vk_is_favorite=0&vk_language=ru&vk_platform=desktop_web&vk_ref=group_menu&vk_ts=1665487420&vk_user_id=518705815&sign=W-A4TrGVXtSNEtMpW5SSPmKBUipEHPmHCJhGCPxW_38'
        }
        y = json.loads(requests.get(data2, headers=params).text)
        a = str(y['all']['items']).count('name')
        b = str(y['all']['styles']).count('name')
        print(f'Всего стикеров и стилей: {a + b}')
        free_count = 0
        free_count1 = 0
        reply_message1 = ''
        reply_message2 = ''
        price = 0
        for i in range(a):
            try:
                x = str(y['all']['items'][i]['price'])
                if x == '0':
                    free_count1 += 1
                else:
                    price += y['all']['items'][i]['price']
            except:
                free_count1 += 1
        for i in range(8):
            try:
                z = y['free'][i]['name']
                stick_free = f'{z}'
                reply_message1 += f'{stick_free}, '
                z = y['paid']['items'][i]['name']
                stick_paid =f'{z}'
                reply_message2 += f'{stick_paid}, '
            except:
                continue
        for v in range(b):
            z = y['all']['styles']['items'][v]['name']
            print(z)
        paid_count = a-free_count1
        print(paid_count)
        if paid_count == 0:
            await message.reply(
                f"✅ [id{user_id}|{name[0].first_name} {name[0].last_name}] имеет {config.pluralForm(a, ['стикерпак', 'стикерпака', 'стикерпаков'])} из них {paid_count} стикерпаков платные и {b} стилей:\n\n🤕Бесплатные стикеры: {reply_message1}и т.д. \n\n🥺 Платных стикерпаков у пользователя нет")
        else:
            await message.reply(
                f"✅ [id{user_id}|{name[0].first_name} {name[0].last_name}] имеет {config.pluralForm(a, ['стикерпак', 'стикерпака', 'стикерпаков'])} из них {paid_count} стикерпаков платные и {b} стилей:\n\n🤕Бесплатные стикеры: {reply_message1}и т.д. \n\n🤑Платные стикеры: {reply_message2}и т.д. \n\n😻Приблизительная цена: {price}₽")

@user.on.private_message(text='/инвайт <text>')
async def invite(message: Message, text):
    print(text)
    try:
        invite = await user.api.messages.join_chat_by_invite_link(link=f'{text}')
        await message.reply(f'Успешно зашёл')
    except:
        await message.reply('Нету доступа к чату')

@user.on.chat_message(text='/стики')
async def stickerr(message: Message):
    user_id = message.from_id
    name = await user.api.users.get(user_id)
    data2 = f'https://stickers.loupg.one/user/{user_id}'
    params = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117',
        'vk-auth': 'vk_access_token_settings=&vk_app_id=7475013&vk_are_notifications_enabled=0&vk_is_app_user=0&vk_is_favorite=0&vk_language=ru&vk_platform=desktop_web&vk_ref=group_menu&vk_ts=1665487420&vk_user_id=518705815&sign=W-A4TrGVXtSNEtMpW5SSPmKBUipEHPmHCJhGCPxW_38'
    }
    y = json.loads(requests.get(data2, headers=params).text)
    a = str(y['all']['items']).count('name')
    b = str(y['all']['styles']).count('name')
    print(f'Всего стикеров и стилей: {a + b}')
    free_count = 0
    free_count1 = 0
    reply_message1 = ''
    reply_message2 = ''
    price = 0
    for i in range(a):
        try:
            x = str(y['all']['items'][i]['price'])
            if x == '0':
                free_count1 += 1
            else:
                price += y['all']['items'][i]['price']
        except:
            free_count1 += 1
    for i in range(8):
        try:
            z = y['free'][i]['name']
            stick_free = f'{z}'
            reply_message1 += f'{stick_free}, '
            z = y['paid']['items'][i]['name']
            stick_paid = f'{z}'
            reply_message2 += f'{stick_paid}, '
        except:
            continue
    for v in range(b):
        z = y['all']['styles']['items'][v]['name']
        print(z)
    paid_count = a - free_count1
    msg_id = await message.reply('Чтобы посмотреть стикеры пользователя: /стики пользователь')
    print(paid_count)
    if paid_count == '0':
        await message.reply(
            f"✅ [id{user_id}|{name[0].first_name} {name[0].last_name}] имеет {config.pluralForm(a, ['стикерпак', 'стикерпака', 'стикерпаков'])} из них {paid_count} стикерпаков платные и {b} стилей:\n\n🤕Бесплатные стикеры: {reply_message1}и т.д. \n\n🥺 Платных стикерпаков у пользователя нет")
    else:
        await message.reply(
            f"✅ [id{user_id}|{name[0].first_name} {name[0].last_name}] имеет {config.pluralForm(a, ['стикерпак', 'стикерпака', 'стикерпаков'])} из них {paid_count} стикерпаков платные и {b} стилей:\n\n🤕Бесплатные стикеры: {reply_message1}и т.д. \n\n🤑Платные стикеры: {reply_message2}и т.д. \n\n😻Приблизительная цена: {price}₽")
    await asyncio.sleep(5)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)

@user.on.chat_message(text='/озвучить <text>')
async def audio(message: Message, text):
    s = gTTS(text=f'{text}', lang='ru').save('sample.mp3')
    audio_upd = await VoiceMessageUploader(user.api).upload(
        f'sample.mp3', file_source=f'sample.mp3', peer_id=message.peer_id
    )
    await message.reply(attachment=audio_upd)

user.labeler.message_view.register_middleware(banan)
user.api.add_captcha_handler(captcha_handler)
user.run_forever()
