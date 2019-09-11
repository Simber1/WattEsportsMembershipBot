import discord
from discord.ext import commands

print(discord.version_info)
token = open("token.txt","r").readline()
client = commands.Bot(command_prefix='!', case_insensitive=True, description='Membership Verification bot')

@client.event
async def on_ready():
        print("We have logged in as {0.user}".format(client))
        await client.change_presence(activity=discord.Game(name='verifying your membership'))



@client.command()
async def member(ctx,*args):
    await ctx.message.delete()
    if len(args) == 1:
        postRoom = client.get_channel(621401128990539777)
        await postRoom.send(ctx.message.author.mention + ": " + args[0])
        return
    await ctx.channel.send(ctx.message.author.mention + ": " + "You Provided too many or too few arguments, please do !member <Hnumber>")
    


client.run(token.strip())

