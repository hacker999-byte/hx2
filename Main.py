import discord

client = discord.Client()

token = input ("hy") 
@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send("https://discord.gg/fr1ends")#ADD HERE THAT YOU WANNA SEND TO YOUR FRIENDS
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('token', bot=False)
