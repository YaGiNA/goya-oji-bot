import os
import discord
import re

client = discord.Client()


@client.event
async def on_ready():
    # show status of client & send initial message to bot-echo channel
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    a_message = "ゴーヤちゃん準備完了でち"
    channel = discord.utils.get(
        client.get_all_channels(), name='bot-echo')
    await client.send_message(channel, a_message)


@client.event
async def on_message(message):
    # send a response when goya-oji appears
    regex_oji = u"ゴーヤちゃんいるかな(\?|？)?(\^|＾){2}"
    is_oji = re.search(regex_oji, message.content)
    if is_oji:
        # except client sender
        if client.user != message.author:
            react = "はいでち"
            await client.send_message(message.channel, react)


def get_key():
    # get a discord's api key from .env
    key = os.getenv("APIKEY")
    return key


def main():
    key = get_key()
    client.run(key)


main()
