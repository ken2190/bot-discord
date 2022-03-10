import discord
from discord.ext import commands 
import requests
import io


client = commands.Bot(command_prefix = "!")

def getLinkDownload(url):
    try:
        c = requests.post("https://api.tikmate.app/api/lookup", data={
            "url":url,
        }).json()
        return f"https://tikmate.app/download/{c['token']}/{c['id']}.mp4"
    except:
        return ""
@client.event
async def on_ready():
    print("Eyyzoooo, Botcute đến rồi đây!!!!")

@client.event
async def on_message(message):
    if message.content.startswith("!tt"):
        url = message.content.split()[1]
        url_download = getLinkDownload(url)
        await message.channel.send(f"Chờ bot xíu nha {message.author.name}!")
        print(f"Get link for {message.author.name}...")
        if url_download == "":
            await message.channel.send("Lỗi rùiiiii!")
            print("error...")
        else:
            resp = requests.get(url_download)
            if resp.status_code != 200:
                print("Can not get link...")
                return await message.channel.send('Xin lũi, không gửi được file...')
            data = io.BytesIO(resp.content)
            print("Send message...")
            await message.channel.send(file=discord.File(data, url_download.split('/')[-1].split('?')[0]), content="Video của bạn nèeee!")
            print("Success...")
            # await message.channel.send(url_download)

client.run('OTUxNTIyNzgyNzUwMDU2NTAw.YiospQ.3uWZAUkiYV0sCwS1FU6cOzTS8pY')
