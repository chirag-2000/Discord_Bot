import discord
import random
from random import choice
from itertools import cycle
from discord.activity import Game
from discord.client import Client
from discord.embeds import Embed
from discord.ext import commands,tasks
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO
import praw           

# client = discord.Client()

client = commands.Bot(command_prefix="!",)
client.remove_command('help')#removes default help commands

status=["vibing to music" ," type  !help ", "good vibes",]
@client.event  #to respond to message #piece of code which runs when the bot detects a specific activiy has happned
async def on_ready():
    change_status.start()
    # await client.change_presence(status=discord.Status.online,activity=discord.Game('good vibes'))#bot status
    print("bot is ready")


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))



@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `!help` command for details!')

# @client.event 
# async def on_message(message):    
#     if str(message.channel)=="👀only-image" and message.content!="": #for deleting text
#         await message.channel.purge(limit=1)#purge for deleting text


# <--------------------------------------------------------------------------------->
@client.command(aliases=["heyy","hi"])
async def hey(ctx): #the name of the function is the name of the commandwith a prefix
    await ctx.send(f"hi!!! {ctx.author}")

@client.command(name='hello')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Ssup bro?', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))

@client.command(aliases=["8ball","eightball"])  #command can be given aliase name s as well
async def _8ball(ctx,*,questions):  # * here takes the question and stack them up as  string
    responses=["As I see it, yes.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don’t count on it.",
                "It is certain.",
                "It is decidedly so.",
                "Most likely.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Outlook good.",
                "Reply hazy, try again.",
                "Signs point to yes.",
                "Very doubtful.",
                "Without a doubt.",
                "Yes.",
                "Yes – definitely.",
                "You may rely on it."]
    await ctx.send(random.choice(responses))


@client.command()  #use of piilow library The Python Imaging Library adds image processing capabilities to your Python interpreter.
async def wanted(ctx, user: discord.Member =None):
    if user == None:
        user=ctx.author
    
    
    wanted =Image.open("wanted.jpg") #to open image #pillow 
    dp=user.avatar_url_as(size= 128)#to get dp size needs to be power of two
    data=BytesIO(await dp.read())#to get bytes data
    pfp=Image.open(data)

    pfp=pfp.resize((293,293))
    wanted.paste(pfp,(75,149))

    wanted.save("profile.jpg")
    await ctx.send(file= discord.File("profile.jpg"))   
 



@client.command()  #pil is used  #tweet
async def tweet(ctx,*,text="**To create your own tweet use command  \n  !tweet and enter you text after the command**\n\nHave a great day!!"):
    img = Image.open('tweet.png')#create and open an white inmage
    draw = ImageDraw.Draw(img)# pass the image  
    font=ImageFont.truetype("Helvetica Neue LT 55 Roman.ttf",25) #select font to be used
    # text= "HEY BUDDY"
    draw.text((35,120),text,(0,0,0),font=font)#co ordinates are given first then the string then the rgb values and finally the font drawn
    
    img.save("text.png")
    
    await ctx.send(file = discord.File("text.png"))



@client.command(name='ping')  #gives latency
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')

@client.command()
async def repeat(ctx,*args):      # await ctx.send("!repeat - to make the bot repeat")
    for arg in args:
        strr=" ".join(args)
    await ctx.send(strr)

@client.command()
@commands.has_permissions(manage_messages=True)#checks are performed before cpode is run  
async def clear(ctx, amount : int):      # await ctx.send("!repeat - to make the bot repeat")
    await ctx.channel.purge(limit=amount)  #enter amount after clear command 


@client.command()
async def kick(ctx,member : discord.Member,* ,reason=None):
    await member.kick(reason=reason)


@client.command()   #show dp command
async def avatar(ctx,member : discord.member = None):
    if member==None:
        member=ctx.author
    
    memberAvatar=member.avatar_url


    avaEmbed=discord.Embed(title=f"{member.name}'s Avatar ",
    color=discord.Color.blue())
    avaEmbed.set_image(url=memberAvatar)
  
    await ctx.send(embed=avaEmbed)
    

@client.command()
async def  poll(ctx,*,message): #here asterix is used to take multiple words
    emb=discord.Embed(
        title="Poll Time 🗳️",
        description=f"{message}",
        color=discord.Color.red(),
    )
    msg= await ctx.channel.send(embed=emb)                 #to add mesage reaction we need message id
    await  msg.add_reaction('👍')
    await  msg.add_reaction('👎')

@client.command()
async def toss(ctx):
    n=random.randint(0,1)#Randint is an inbuilt function of the random module in Python3. The random module gives access to various useful functions and one of them being able to generate random numbers, which is randint().
    await ctx.send("Heads" if n==1 else "Tails")


@client.command()
async def invite(ctx):
    icon = str(ctx.guild.icon_url)
    bed=discord.Embed(
    title="Invite link",
    description="Add this bot in your server  \nhttps://discord.com/oauth2/authorize?client_id=835773765442994207&permissions=3693603959&scope=bot",
    colour=discord.Colour.gold()
    )
    bed.set_thumbnail(url=icon)
    await ctx.send(embed=bed)

#embed
@client.command()
async def help(ctx):
    # channel=str(ctx.message.channel)
    memberCount = str(ctx.guild.member_count)#to access member count in the server
    mbed=discord.Embed(
        title='!help ℹ️',
        description="List of commands the bot contains and its funtionality ",
        colour=discord.Colour.dark_orange()
        
    )
    
    mbed.add_field(name='!8ball 🎱',value="(FORTUNE TELLER!!🔮)  ask a YES or NO question after the command and the fortune teller gives you an answer",inline=True)
    mbed.add_field(name='!hey ',value="welcomes u with your name and id 🙏",inline=False)
    mbed.add_field(name='!repeat',value="repeats the text after the command 🔁",inline=False)
    mbed.add_field(name='!ping',value="This command returns the latency 🏓",inline=False)
    mbed.add_field(name='!poll',value="Conduct poll .Ask poll question after the command and the members in the server will be able to vote 🗳️ ",inline=False)
    mbed.add_field(name='!avatar',value="Shows your discord profile picture (avatar) ",inline=False)
    mbed.add_field(name='!memes',value="Gets you the latest  ***memes***  from reddit. You can also get memes from a particular category using ***!memes*** command followed by a topic  (ex:!memes doge) 🐸  ",inline=False)
    mbed.add_field(name='!hello',value="This command returns a random welcome message ",inline=False)
    mbed.add_field(name='!toss',value="Coin Flip 🪙 ",inline=False)
    mbed.add_field(name='!tweet',value="To create your own tweet use command ***!tweet*** and enter you text after the command ",inline=False)
    mbed.add_field(name='!wanted',value="Create a wanted poster for you or Your friends using ***!wanted*** command 😈 ",inline=False)
    mbed.add_field(name='!server',value="Gives a brief description obout the server ℹ️ ",inline=False)
    mbed.add_field(name='!kick',value="Can kick anyone from the server .Just mention the name of the person to be kicked after the command and he/she will be removed (can be used by the person who has admin role)",inline=False)
    mbed.add_field(name='!clear',value="clears  text in the server .Just write the number of lines to be deleted after the command",inline=False)
    mbed.add_field(name='!invite',value="Gives link to add Watermelon BOT to your server 😀",inline=False)
    await ctx.send(embed=mbed)

reddit=praw.Reddit(client_id="BwCsGCoI2YV_tw",     #found after creating ap
                   client_secret="1qVSDq0r1OxurrOeaITb29UHfQfT0w",
                   username="funboi_007",
                   password="*_%5w6nB_qud5HH",
                   user_agent="Watermelon")#can be anything
                                
@client.command()
async def memes(ctx,subred="memes"):
    subreddit =reddit.subreddit(subred)#category
    all_subs=[]
    top = subreddit.top(limit = 50)#top posts

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em =discord.Embed(title=name)

    em.set_image(url =url) 
    await ctx.send(embed=em)



@client.command()  #embeds usually reserved for bots and webhooks
async def server(ctx): #ctx =context
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)
    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)    

#error handling
@client.event #error handling
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found")
    
@clear.error #this function is trigerred when there is error in clear command
async def clear_error(ctx,error):
    if isinstance(error, commands.UserInputError ):  #commands.MissingRequiredArgument
        await ctx.send("please specify amount of message to be cleared (ex: !clear 2)")

        
client.run('ODM1NzczNzY1NDQyOTk0MjA3.YIUU-Q.FHuOPUgUXgiW23oTXOOoAZrZQI0') #token  #makes bot go online
        
    
    
    







