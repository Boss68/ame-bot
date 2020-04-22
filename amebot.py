import discord, random, time, os
from discord.ext import commands
from discord.ext import tasks

months={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
weekday={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
amPm={0:'AM',1:'PM'}
#month,year,day,hour,minute,second
token="NjkyODEzNzMwODI3OTkzMTQ5.XoO1BA.Kt516dFLWEmyZQ7QLgSo-BxVuYE"
commandPrefix="/"
client = commands.Bot(command_prefix=commandPrefix)
@client.event
async def on_ready():
  printArchive.start()
  print("Logged in as you're mom")
@client.command(help="bruh")
async def bruh(ctx,*,param):
  await ctx.send(param)
@client.command(help="")
async def archive(ctx,*,item):
  if not(',' in item):
    time_=time.localtime()
    time_=str(time_.tm_sec).zfill(2)+str(time_.tm_min).zfill(2)+str(time_.tm_hour).zfill(2)+str(time_.tm_mday).zfill(2)+str(time_.tm_wday).zfill(1)+str(time_.tm_mon).zfill(2)+str(time_.tm_year)
    todo=open("todo.txt","a")
    todo.write(","+item+time_)
    todo.close()
    await ctx.send('added '+item+' to archive.')
  else:
    await ctx.send('\',\' character is not allowed.')
@client.command(help="")
async def archivedel(ctx):
  todo=open("todo.txt","r")
  todoLines=todo.readlines()[0]
  todo.close()
  todo=open("todo.txt","w")
  try:
    todoList=todoLines.split(',')[2:]
    todoString=""
    for i in todoList:
      todoString+=","+i
  except Exception:
    todoList=[]
    todoString=""
  todo.write(todoString)
  await ctx.send("removed "+todoLines.split(',')[1][::-1][15:][::-1]+" from the archive.")
@client.command()
async def archiveclear(ctx):
  todo=open('todo.txt','w')
  todo.close()
  await ctx.send("cleared the archive.")
@client.command()
async def archivelist(ctx):
  embedStr=""
  try:
    todo=open("todo.txt","r")
    todoLines=todo.readlines()[0]
    embedStr=""
    for i in todoLines.split(',')[1:]:
      normalString=i[::-1][15:][::-1]
      timeString=i[::-1][:15][::-1]
      timeString=weekday[int(timeString[8:9])]+", "+months[int(timeString[9:11])]+" "+timeString[6:8]+", "+timeString[11:15]+" at "+str(((int(timeString[4:6])-1)%12)+1)+':'+timeString[2:4]+':'+timeString[0:2]+" "+amPm[int(int(timeString[4:6])>=12)]
      embedStr+=normalString+' - added at '+timeString+" UTC"+"\n\n"
  except Exception:
    None
  embed=discord.Embed(title="Archive",type="rich",description=embedStr,colour=discord.Colour.gold())
  await ctx.send(embed=embed)
  todo.close()

@tasks.loop(seconds=1)
async def printArchive():
  if time.localtime().tm_min!=0:
    sent=False
  if time.localtime().tm_min==0 and sent==False:
    sent=True
    embedStr=""
    try:
      todo=open("todo.txt","r")
      todoLines=todo.readlines()[0]
      embedStr=""
      for i in todoLines.split(',')[1:]:
        embedStr+=i+"\n\n"
    except Exception:
      None
    embed=discord.Embed(title="Archive",type="rich",description=embedStr,colour=discord.Colour.gold())
    await client.get_guild(691343455590547477).get_channel(693153292938903661).send(embed=embed)
    todo.close()
@client.event
async def on_message(message):
  if message.author.id!=692813730827993149 and message.content[0:len(commandPrefix)]!=commandPrefix:
    if "I'm " in message.content:
      reply=message.content[message.content.index("I'm ")+4:]
      await message.channel.send("Hi "+reply+", I'm Dad!")
    if "cannon porn" in message.content.lower() or "cannonporn" in message.content.lower() or "cann0n p0rn" in message.content.lower() or "cannon p0rn" in message.content.lower() or "cann0n porn" in message.content.lower() or "can00n p0rn" in message.content.lower(): 
      await message.delete()
    if "I don't remember asking" in message.content or "i dont remember asking" in message.content or "I dont remember asking" in message.content:
      await message.channel.send("No one give a fuck about your alzheimers ass.")  
    if "God help us" in message.content:
      await message.channel.send("Hell no.")
    if "Roblox bad lol" in message.content:
      await message.channel.send("GG, "+ message.author.mention + ", you just advanced to level "+str(random.randint(0,3641397469861978469786))+"!")      
    if "!" == message.content[len(message.content)-1] or "Vc" in message.content:
      await message.channel.send("FUCK YOU "+message.author.mention+"! If you're dumb enough to buy a new car this weekend, you're a big enough schmuck to come to Big Bill Hell's Cars! Bad deals! Cars that break down! if you think you're gonna find a bargain at Big Bill's, YOU CAN KISS MY ASS! It's our belief that you're such a stupid motherfucker, you'll fall for this bullshit! GUARANTEED! If you find a better deal, SHOVE IT UP YOUR UGLY ASS! You heard us right! SHOVE IT UP YOUR UGLY ASS! Bring your tray, bring your timer, bring your wife! WE'LL FUCK HER! THAT'S RIGHT! WE'LL FUCK YOUR WIFE! Because at Big Bill Hell, you're about six ways from Sunday. Take a hike to Big Bill Hell, HOME OF CHALLENGE PISSING, that's right, challenge pissing! How does it work? If you can piss 60 feet straight up and not get wet, you get no downpayment! Don't wait, don't delay, DON'T FUCK WITH US, or we'll rip your nuts off! Only at Big Bill Hell's, the only dealer that tells you to FUCK OFF! HURRY UP, ASSHOLE! This event ends the minute after you write us a check, and I'd better not bounce or you're a dead motherfucker! GO TO HELL! Big Bill Hell's Cars, all the wares the filthiest, and exclusive home of the meanest sons of bitches in the state of Maryland, GUARANTEED!")
  elif message.content[0:len(commandPrefix)]==commandPrefix:
    await client.process_commands(message)
client.run(token)
