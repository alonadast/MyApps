# -*- coding: utf-8 -*-
import time
import vk_api
#vk = vk_api.VkApi(login = 'login', password = 'password')
vk = vk_api.VkApi(token = '2ab650d2ab40c228a3ff04b6008333d787ad369d39c70e914e3ddc92af479ac62453c5a9770b4e95b671f') #Авторизоваться как сообщество
vk.auth()
values = {'out': 0,'count': 100,'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
            write_msg(item[u'user_id'],u'Привет!\nМы начали разработку нашего бота!\nОткроем мы его после 3000 подписчиков, так что зови друзей!')
    time.sleep(1)
