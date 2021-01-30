import discord
import env
from discord.ext import commands
from python_graphql_client import GraphqlClient


graphql = GraphqlClient(endpoint="https://yacy.org/graphql")
bot = commands.Bot(command_prefix='=')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def echo(ctx, *args):
    print("PING")
    out = ""
    for word in args:
        out += word + " "
    await ctx.send(out)

level_count = """
    query {
        levelCount
    }
"""
@bot.command()
async def levels(ctx):
    data = graphql.execute(query=level_count)
    await ctx.send("CY Levels: " + str(data["data"]["levelCount"]));

'''
query = """
    query countryQuery($countryCode: String) {
        country(code:$countryCode) {
            code
            name
        }
    }
"""
variables = {"countryCode": "CA"}

# Synchronous request
data = client.execute(query=query, variables=variables)
'''


bot.run(env.DISCORD_TOKEN)