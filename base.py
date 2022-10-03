from vkbottle.bot import Message
from vkbottle.user import User
from vkbottle.tools import DocMessagesUploader

user =User(token="")

@user.on.message(text='qwe123123')
async def wrapper(message: Message):
    doc = await DocMessagesUploader(user.api).upload(
            'img_bg_1_gradient.jpg', file_source='C:/Users/Bogda/PycharmProjects/vkraasilka/img_bg_1_gradient.jpg',
            peer_id=message.peer_id
            )
    await message.answer(attachment=doc)

user.run_forever()