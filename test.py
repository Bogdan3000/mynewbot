from vkbottle.bot import Message
from vkbottle.user import User
from vkbottle import CaptchaError
from vkbottle.http import AiohttpClient

http = AiohttpClient()
user = User(token="vk1.a.RWWsNazD5-_WD0qQz1JWNoGVLUTbIYyubSAF5VA4JNdtVv9Q6LZefNcT-LfVLTTnzNwLeOY_Qi3nvunb-qk4K9e76t3GX0zGqUUgrS0ofMCLwLvg7NUOhZg2JncKg8SlZgddIT6DLaysiIMiZwYxJORto47Ruiz2GaZjsoEAse6C-ebO73Qs3sHoNcBJbiW-")


async def captcha_handler(e: CaptchaError) -> str:
    solved = await http.request_json(
        url='https://vk-cptch-solver.herokuapp.com/captcha',
        json={
            'token': 'd41bf683e69ddacca23583ca9d3e6b5d75b9a38594620f989cd150a28da7134b',
            'sid': e.sid,
        },
    )

    return solved["solve"]

@user.on.private_message(text = '<text>')
async def spam(message: Message):
    while True:
        await message.answer('Ты пидор?')

user.api.add_captcha_handler(captcha_handler)
user.run_forever()