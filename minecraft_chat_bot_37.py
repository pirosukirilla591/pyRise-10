from javascript import require, On, AsyncTask
from time import sleep

mineflayer = require('mineflayer')
isFishing = False

bot = mineflayer.createBot({
    'host': 'в данную строку надо вписать IP вашего сервера в Minecraft',
    'username': 'имя вашего бота ( придумайте абсолютно любое)',
    'version': 'версия вашего сервера',
    'port': 'порт вашего сервера ( обычно это 25565 если это локальный сервер... )'
})


@On(bot._client, 'sound_effect')
def sound_handler(this, packet, *args):
    global isFishing
    if isFishing == True:
        soundId = packet
        if soundId['soundId'] == 272:
            bot.activateItem()
            isFishing = False


@On(bot, 'spawn')
def spawn(*args):
    bot.chat(bot.username)


@On(bot, 'chat')
def msgHandler(this, user, message, *args):
    print(message)
    if message == 'fish':
        bot.equip(bot.registry.itemsByName.fishing_rod.id, 'hand')
        @AsyncTask(start=True)
        def fishing(task):
            global isFishing
            while True:
                if isFishing == False:
                    sleep(1)
                    bot.activateItem()
                    isFishing = True









