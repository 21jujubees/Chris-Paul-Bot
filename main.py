import os
import hikari
import lightbulb
import random

cpLaugh = 'https://tenor.com/view/chris-paul-fake-laugh-gif-18365912'
x = 0

bot = lightbulb.BotApp(
    token=(os.getenv('token')),
    default_enabled_guilds=(847259054999994398),
    )
    
def getTextList(fname):
    return open(fname).read().splitlines()

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    newMessage = event.content.lower()
    for x in getTextList('insults.txt'):
        if x in newMessage:
            await event.message.respond(cpLaugh)

@bot.command
@lightbulb.command('cp3', 'Hear an inspirational quote from Chris Paul!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cp3(ctx):
    await ctx.respond(random.choice(getTextList('quotes.txt')))

bot.run()