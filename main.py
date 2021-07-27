import discord
import os
import time
import json
client = discord.Client()
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    with open('data.json') as json_file: #Check if bot is alredy working
        data = json.load(json_file)

    if message.author == client.user:
        return
    
    if message.content.startswith('!about'):
        await message.channel.send('Created by EpicMario71, source code: https://github.com/epicmario7133/Video-to-mp3-bot-discord')

    if str(message.attachments) == "[]": # Checks if there is an attachment on the message
        return

    if data["work"] == "1": #Check if bot is working
        await message.channel.send('Bot is working please wait')
        pass

    else: # If there is it gets the filename from message.attachments

        split_v1 = str(message.attachments).split("filename='")[1]
        filename = str(split_v1).split("' ")[0]
        if filename.endswith(".mp4"): # Checks if it is a .mp4 file
            data["work"] = "1"
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            await message.attachments[0].save(fp="mp4/{}".format("video.mp4")) #save flie
            await message.channel.send('I\'m converting the video give me 10 seconds') 
            os.system("ffmpeg -i /home/ubuntu/bot-mp3/mp4/video.mp4 -y /home/ubuntu/bot-mp3/mp3/audio.mp3") #convert whit ffmpeg (-y to overwrite old file)
            time.sleep(10) #Give time for bot to convert, set 20 if your pc is a potato
            await message.channel.send(file=discord.File("/home/ubuntu/bot-mp3/mp3/audio.mp3")) #Send file
            time.sleep(3) #Wait bot upload file
            data["work"] = "0" #set bot to ready
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            await message.channel.send('Now the bot is ready')
            
            
           

    #Convert .mov

    if str(message.attachments) == "[]": # Checks if there is an attachment on the message
        return

    if data["work"] == "1": #Check if bot is working
        await message.channel.send('Bot is working please wait')
        pass

    else: # If there is it gets the filename from message.attachments

        split_v1 = str(message.attachments).split("filename='")[1]
        filename = str(split_v1).split("' ")[0]
        if filename.endswith(".mov"): # Checks if it is a .mov file
            data["work"] = "1"
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            await message.attachments[0].save(fp="mov/{}".format("video.mov")) #save flie
            await message.channel.send('I\'m converting the video give me 10 seconds') 
            os.system("ffmpeg -i /home/ubuntu/bot-mp3/mov/video.mov -y /home/ubuntu/bot-mp3/mp3/audio.mp3") #convert whit ffmpeg
            time.sleep(10) #Give time for bot to convert, set 20 if your pc is a potato
            await message.channel.send(file=discord.File("/home/ubuntu/bot-mp3/mp3/audio.mp3")) #Send file
            time.sleep(3) #Wait bot upload file
            data["work"] = "0" #set bot to ready
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            await message.channel.send('Now the bot is ready')
            
    #for avi video

    if str(message.attachments) == "[]": # Checks if there is an attachment on the message
        return

    if data["work"] == "1": #Check if bot is working
        await message.channel.send('Bot is working please wait')
        pass

    else: # If there is it gets the filename from message.attachments

        split_v1 = str(message.attachments).split("filename='")[1]
        filename = str(split_v1).split("' ")[0]
        if filename.endswith(".avi"): # Checks if it is a .avi file
            data["work"] = "1"
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            await message.attachments[0].save(fp="avi/{}".format("video.avi")) #save flie
            await message.channel.send('I\'m converting the video give me 10 seconds') 
            os.system("ffmpeg -i /home/ubuntu/bot-mp3/avi/video.avi -y /home/ubuntu/bot-mp3/mp3/audio.mp3") #convert whit ffmpeg
            time.sleep(10) #Give time for bot to convert, set 20 if your pc is a potato
            await message.channel.send(file=discord.File("/home/ubuntu/bot-mp3/mp3/audio.mp3")) #Send file
            time.sleep(3) #Wait bot upload file
            data["work"] = "0" #set bot to ready
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            await message.channel.send('Now the bot is ready')



    #for webm video

    if str(message.attachments) == "[]": # Checks if there is an attachment on the message
        return

    if data["work"] == "1": #Check if bot is working
        await message.channel.send('Bot is working please wait')
        pass

    else: # If there is it gets the filename from message.attachments

        split_v1 = str(message.attachments).split("filename='")[1]
        filename = str(split_v1).split("' ")[0]
        if filename.endswith(".webm"): # Checks if it is a .avi file
            data["work"] = "1"
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            await message.attachments[0].save(fp="webm/{}".format("video.webm")) #save flie
            await message.channel.send('I\'m converting the video give me 10 seconds') 
            os.system("ffmpeg -i /home/ubuntu/bot-mp3/webm/video.webm -y /home/ubuntu/bot-mp3/mp3/audio.mp3") #convert whit ffmpeg
            time.sleep(10) #Give time for bot to convert, set 20 if your pc is a potato
            await message.channel.send(file=discord.File("/home/ubuntu/bot-mp3/mp3/audio.mp3")) #Send file
            time.sleep(3) #Wait bot upload file
            data["work"] = "0" #set bot to ready
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            await message.channel.send('Now the bot is ready')
            
client.run(TOKEN)
