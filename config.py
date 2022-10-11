from vkbottle.user import User
import vkcoin
from vkbottle.http import AiohttpClient
import requests
import psycopg2

http = AiohttpClient()
URI = 'postgres://jnsnigkg:CqVw_5BKv6NP5TL3L7xIT6OANZJN-6sP@lucky.db.elephantsql.com/jnsnigkg'
data = requests.get('https://raw.githubusercontent.com/Infqq/auf_gen/main/phrases.txt').text.splitlines()
data1 = requests.get('https://raw.githubusercontent.com/Anatoly333/Info_tasks/af9b0fc8819ea70b6f378f59c86e7250cd20df06/Info_Anatoly/datafacts.txt').text.splitlines()
merchant = vkcoin.VKCoin(user_id=518705815, key='*b;4grVAAdADI9.wQ0!-a77_.EI;pj''n&noFn2ZBdV=!RAuaHxT')
db_connection = psycopg2.connect(URI, sslmode='require')
db_object = db_connection.cursor()
user = User(token="vk1.a.RWWsNazD5-_WD0qQz1JWNoGVLUTbIYyubSAF5VA4JNdtVv9Q6LZefNcT-LfVLTTnzNwLeOY_Qi3nvunb-qk4K9e76t3GX0zGqUUgrS0ofMCLwLvg7NUOhZg2JncKg8SlZgddIT6DLaysiIMiZwYxJORto47Ruiz2GaZjsoEAse6C-ebO73Qs3sHoNcBJbiW-")

def pluralForm(amount, variants):
    amount = abs(amount)

    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2

    return f"{amount} {variants[variant]}"