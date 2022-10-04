from vkbottle.bot import Message
from vkbottle.user import User
import vkcoin
import os
from vkbottle.dispatch.rules.base import *
from vkbottle.tools import *
from vkbottle import CaptchaError, BaseMiddleware, BaseStateGroup
from vkbottle.http import AiohttpClient
from demotivators import Demotivator, Quote, QuoteB, dphoto
import requests
import random
import psycopg2
import datetime
import asyncio
x = str(datetime.datetime.now()).partition('.')[0].replace(' ', ' в ')
print(x)

async def reg(user_id):
    db_object.execute(f"SELECT id FROM users WHERE id = {user_id}")
    result = db_object.fetchone()
    if not result:
        db_object.execute(
            "INSERT INTO users(id, santimeters, rules, users_count, name_surname, ban) VALUES (%s, %s, %s, %s, %s, %s)",
            (user_id, 0, 0, 0, 0, 0))
        db_connection.commit()


class banan(BaseMiddleware[Message]):
    async def pre(self):
        try:
            db_object.execute(f'SELECT ban FROM users WHERE id = {self.event.from_id}')
            result = db_object.fetchone()[0]
            if result == 1:
                self.stop("Пользователь в бане")
        except:
            user_id = self.event.from_id
            await reg(user_id)
            db_object.execute(f'SELECT ban FROM users WHERE id = {self.event.from_id}')
            result = db_object.fetchone()[0]
            if result == 1:
                self.stop("Пользователь в бане")


http = AiohttpClient()

URI = 'postgres://dentsszcjnzjdd:15ea053f4ae0e465f93242d9440a0853c88a099f4ce9f001ce41f7f0005a063c@ec2-54-228-125-183.eu-west-1.compute.amazonaws.com:5432/dd3rqgjsvt6ujn'
data = requests.get('https://raw.githubusercontent.com/Infqq/auf_gen/main/phrases.txt').text.splitlines()
data1 = requests.get(
    'https://raw.githubusercontent.com/Anatoly333/Info_tasks/af9b0fc8819ea70b6f378f59c86e7250cd20df06/Info_Anatoly/datafacts.txt').text.splitlines()
merchant = vkcoin.VKCoin(user_id=518705815, key='*b;4grVAAdADI9.wQ0!-a77_.EI;pj'
                                                'n&noFn2ZBdV=!RAuaHxT')

db_connection = psycopg2.connect(URI, sslmode='require')
db_object = db_connection.cursor()
user = User(
    token="vk1.a.RWWsNazD5-_WD0qQz1JWNoGVLUTbIYyubSAF5VA4JNdtVv9Q6LZefNcT-LfVLTTnzNwLeOY_Qi3nvunb-qk4K9e76t3GX0zGqUUgrS0ofMCLwLvg7NUOhZg2JncKg8SlZgddIT6DLaysiIMiZwYxJORto47Ruiz2GaZjsoEAse6C-ebO73Qs3sHoNcBJbiW-")


async def captcha_handler(e: CaptchaError) -> str:
    solved = await http.request_json(
        url='https://vk-cptch-solver.herokuapp.com/captcha',
        json={
            'token': 'd41bf683e69ddacca23583ca9d3e6b5d75b9a38594620f989cd150a28da7134b',
            'sid': e.sid,
        },
    )

    return solved["solve"]


async def isk(message):
    if message.from_id == 7296218 or message.from_id == 563739506 or message.from_id == 491848098 or message.from_id == 329152965 or message.from_id == 474978917 or message.from_id == 363852234:
        await asyncio.sleep(0.00000001)


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
            await message.reply('Выполнено и удалено')
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
        await message.reply('Выполнено и удалено')


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
    await message.reply(f'Ваш баланс Vk Coin: {bal.partition(":")[2].partition("}")[0]}')


@user.on.chat_message(text=['/бал @<name>', '/бал [<name>|<rfc>]'])
async def vkc(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    user_id = await user.api.utils.resolve_screen_name(name)
    print(user_id)
    bal = str(merchant.get_balance(user_id.object_id))
    user_name = await user.api.users.get(user_id.object_id)
    await message.reply(
        f'Баланс [id{user_id.object_id}|{user_name[0].first_name}] Vk Coin равен: {bal.partition(":")[2].partition("}")[0]}')


@user.on.chat_message(AttachmentTypeRule("photo"))
async def wrapper(message: Message):
    user_id = message.from_id
    await reg(user_id)
    db_object.execute(f'SELECT ban FROM users WHERE id = {message.from_id}')
    result = db_object.fetchone()[0]
    print(result)
    if result == 0:
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
    else:
        await asyncio.sleep(0.00000001)


@user.on.chat_message(text='/дем<text>')
async def wrapper(message: Message):
    if message.text != "" and message.text.find('/дем') == 0:
        user_id = message.from_id
        await reg(user_id)
        user_id = message.from_id
        await reg(user_id)
        text = message.text.splitlines()
        try:
            photo = message.reply_message.attachments[0].photo.sizes[-1].url
        except:
            try:
                photo = message.reply_message.attachments[0].doc.url
            except:
                await message.answer('Продемотивировать можно только фото, для текста используйте /цитата')
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


@user.on.chat_message(text='/ауф')
async def wrapper(message: Message):
    user_id = message.from_id
    await reg(user_id)
    auf = random.choice(data)
    print(auf)
    await message.reply(f'{auf}')


@user.on.chat_message(text='/интересный факт')
async def wrapper(message: Message):
    user_id = message.from_id
    await reg(user_id)
    user_id = message.from_id
    await reg(user_id)
    fact = random.choice(data1)
    await message.reply(f'{fact}')


@user.on.chat_message(text='/команды')
async def wrapper(message: Message):
    user_id = message.from_id
    await reg(user_id)
    msg_id = await message.reply('На данный момент существуют 0 команд:\n\n')
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 1 команд:\n\n
1. /Сколько у <name> <args >?Рандомно выдает <args>.\n"""
    )
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 2 команд:\n\n
1. /Сколько у <name> <args>? Рандомно выдает <args>.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 3 команд:\n\n
1. /Сколько у <name> <args>? Рандомно выдает <args>.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 4 команд:\n\n
1. /Сколько у <name> <args>? Рандомно выдает <args>.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 5 команд:\n\n
1. /Сколько у <name> <args>? Рандомно выдает <args>.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 6 команд:\n\n
1. /Сколько у <name> <args>? Рандомно выдает <args>.\n
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
1. /Сколько у <name> <args>? Рандомно выдает <args>.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата олд - Создаёт цитату.\n\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 8 команд:\n\n
1. /Сколько у <name> <args>? - Рандомно выдает <args> от 40 до 50.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата нью - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> -показывает либо ваш либо размер пользователя.\n\n""")
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
8. /чекхуй & /чекхуй <user> -показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ - показывает топ 10 по разммерам.\n\n
P.S. Бот уже стоит на хосте, но с 28 ноября хост будит стоит денег, так что скидуемся ему [id518705815|Богдан], иначе всем бан(""")


@user.on.private_message(text='/команды')
async def wrapper(message: Message):
    user_id = message.from_id
    await reg(user_id)
    msg_id = await message.reply('На данный момент существуют 0 команд:\n\n')
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 1 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> в выбранном вами диапазоне.\n"""
    )
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 2 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> в выбранном вами диапазоне.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 3 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> в выбранном вами диапазоне.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 4 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> в выбранном вами диапазоне.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 5 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> в выбранном вами диапазоне.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n""")
    await asyncio.sleep(1)
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 6 команд:\n\n
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> в выбранном вами диапазоне.\n
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
1. /Сколько у <name> <args>? <num1>--<num2> - Рандомно выдает <args> в выбранном вами диапазоне.\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> - показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем - Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф - Отправляет случайные ауф фразы.\n
6. /интересный факт - Отправляет случайный интересный факт.\n
7. /цитата & /цитата олд - Создаёт цитату.\n\n""")
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
7. /цитата & /цитата олд - Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> -показывает либо ваш либо размер пользователя.\n\n""")
    await user.api.messages.edit(
        peer_id=message.peer_id,
        message_id=msg_id.message_id,
        message=f"""На данный момент существуют 9 команд:\n\n
1. /Сколько у <name> <args>? -Рандомно выдает <args> от 40 до 50\n
2. /хуй & /хуй- - Увеличивает/Уменьшает размер вашего...\n
3. /бал & /бал <user> -показывает либо ваш либо баланс пользователя VkCoin'ов.\n
4. /дем -Создаёт демотиватор с вашим фото и текстом.\n
5. /ауф -Отправляет случайные ауф фразы.\n
6. /интересный факт -Отправляет случайный интересный факт.\n
7. /цитата & /цитата олд -Создаёт цитату.\n
8. /чекхуй & /чекхуй <user> -показывает либо ваш либо размер пользователя.\n
9. /чекхуй топ -показывает топ 10 по размерам.\n\n
ЭТОТ БОТ РАБОТАЕТ ТОЛЬКО В ЧАТАХ\n\n
P.S. Бот уже стоит на хосте, но с 28 ноября хост будит стоит денег, так что скидуемся ему [id518705815|Богдан], иначе всем бан(""")


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
        elif message.reply_message.text == '':
            await message.reply('Чтобы процитировать фото, надо использовать команду /дем <текст>')
    elif message.reply_message is None:
        await message.reply('Чтобы процитировать сообщение,ты должен на него ответить')


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
        elif message.reply_message.text == '':
            await message.reply('Чтобы процитировать фото, надо использовать команду /дем <текст>')
    elif message.reply_message is None:
        await message.reply('Чтобы процитировать сообщение,ты должен на него ответить')


@user.on.chat_message(text='/чекхуй топ')
async def dicktop(message: Message):
    user_id = message.from_id
    await reg(user_id)
    db_object.execute(f'SELECT * FROM users ORDER BY santimeters DESC LIMIT 10')
    result = db_object.fetchall()
    reply_message = "Топ по размерам:\n"
    msg_id = await message.answer(reply_message)
    for i, item in enumerate(result):
        users_name = await user.api.users.get(item[0])
        reply_message += f'{i + 1}.  [id{item[0]}|{users_name[0].first_name}] - {item[1]} см.\n'
        await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'{reply_message}')


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
    await message.reply(attachment=photo_upd)
    os.remove('qresult.png')


@user.on.chat_message(text=['/чекхуй @<name>', '/чекхуй [<name>|<rfc>'])
async def dickinfo(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    user_id1 = await user.api.utils.resolve_screen_name(name)
    users_name1 = await user.api.users.get(user_id1.object_id)
    db_object.execute(f'SELECT santimeters FROM users WHERE id = {user_id1.object_id}')
    result = db_object.fetchone()
    await message.reply(f'Размер [id{user_id1.object_id}|{users_name1[0].first_name}а] : {result[0]}')


@user.on.chat_message(text='/сп <name>')
async def spam(message: Message, name):
    a = 0
    if message.from_id == 518705815:
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
    if message.from_id == 518705815 or message.from_id == 599457498:
        user_id = await user.api.utils.resolve_screen_name(name)
        db_object.execute(f'SELECT ban FROM users WHERE id = {user_id.object_id}')
        result = db_object.fetchone()[0]
        print(result)
        if result == 1:
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
        await asyncio.sleep(0.0001)


@user.on.chat_message(text=['/разбан @<name>', '/разбан [<name>|<rfc>]'], )
async def ban(message: Message, name):
    user_id = message.from_id
    await reg(user_id)
    if message.from_id == 518705815 or message.from_id == 599457498:
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
                await message.answer('Пользователь успешно разбанен')
            else:
                await message.answer('Не удалось разбанить пользователя')
    else:
        await asyncio.sleep(0.0001)


@user.on.chat_message(text=['/адм команды'])
async def command(message: Message):
    await message.answer("""Команды администрации:\n\n
1. /спам <text> <num> - Невидимо спамит <text>'ом <num> раз\n
2. /ban <args> - Фейк-бан\n
3. /статус <args> - Меняет статус в беседе (Например: Пользователь печатает...)\n
4. /сп <text> - Спамит в беседе <text>'ом\n
5. /бан <name> & /разбан <name> - Банит/Разбанивает пользователя в боте\n""")


@user.on.chat_message(text=['/айди @<name>', '/айди [<name>|<rfc>]'])
async def abt(message: Message, name):
    user_id = await user.api.utils.resolve_screen_name(name)
    await message.answer(f'Айди: {user_id.object_id}')

@user.on.chat_message(text='/пинг')
async def ping(message: Message):
    user_id = message.from_id
    await reg(user_id)
    start_s = datetime.datetime.now().second
    start_m = datetime.datetime.now().microsecond
    msg_id = await message.answer('Пингую...')
    end_s = datetime.datetime.now().second
    end_m = datetime.datetime.now().minute
    total_ping_s = round(start_s-end_s)
    total_ping_m = round(start_m-end_m)
    await user.api.messages.edit(
            peer_id=message.peer_id,
            message_id=msg_id.message_id,
            message=f'Пинг: {total_ping_s},{total_ping_m} секунд'
            )
    await asyncio.sleep(10)
    await user.api.messages.delete(
        peer_id=message.peer_id,
        message_ids=msg_id.message_id,
        delete_for_all=1)


user.labeler.message_view.register_middleware(banan)
user.api.add_captcha_handler(captcha_handler)
user.run_forever()
