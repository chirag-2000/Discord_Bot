async def on_message(message):    
    if str(message.channel)=="👀only-image" and message.content!="": #for deleting text
        await message.channel.purge(limit=1)#purge for deleting text

    message.content==message.content.lower()  #lower all strings
    if message.author==client.user:   #to check if the bot is nor  responding to it self
        return
    if message.content.startswith("!"):
        
        if str(message.author)=="chiiirag#8362":
            await message.channel.send(f"hi {message.author} !") #send for sending text
        else:
            await message.channel.send("hi from the bot ")

    if str(message.channel)=="👀only-image" and message.content!="": #for deleting text
        await message.channel.purge(limit=1)#purge for deleting text