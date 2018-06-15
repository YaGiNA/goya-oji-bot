import os
import discord
import re
from discord.ext import commands

goya_bot = commands.Bot(command_prefix='$')


@goya_bot.event
async def on_ready():
    # show status of goya_bot & send initial message to goya_bot channel
    print('Logged in as')
    print(goya_bot.user.name)
    print(goya_bot.user.id)
    print('------')
    send_message = "ゴーヤちゃん準備完了でち"
    channel = discord.utils.get(
        goya_bot.get_all_channels(), name='bot-echo')
    await goya_bot.send_message(channel, send_message)


@goya_bot.event
async def on_message(message):
    # send a response when goya-oji appears
    regex_oji = u"ゴーヤちゃんいるかな(\?|？)?(\^|＾){2}"
    is_oji = re.search(regex_oji, message.content)
    if is_oji:
        # except goya_bot sender
        if goya_bot.user != message.author:
            react = "はいでち"
            await goya_bot.send_message(message.channel, react)


def get_key():
    # get a discord's api key from .env
    key = os.getenv("APIKEY")
    return key


def main():
    key = get_key()
    goya_bot.run(key)


main()
