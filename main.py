import discord
import env
from discord.ext import commands
from python_graphql_client import GraphqlClient
 
import graphql_query as q


graphql = GraphqlClient(endpoint="https://yacy.org/graphql")
bot = commands.Bot(command_prefix='=')

@bot.event
async def on_ready():
    print("\n\nBot has connected to Discord!\n")

@bot.command()
async def levels(ctx):
    data = graphql.execute(query=q.level_count)
    await ctx.send("CY Levels: " + str(data["data"]["levelCount"]))

@bot.command()
async def search(ctx, *args):
    term = " ".join(args)
    variables = {"query": term, "page": 1, "pageSize": 10}
    data = graphql.execute(query=q.search_levels, variables=variables)

    output = discord.Embed(title="Search Results")
    for level in data["data"]["searchLevels"]:
        title  = level["title"]
        author = level["author"]
        plays  = str(level["plays"])
        output.add_field(name=title + " by " + author, value="Plays: " + plays)
    await ctx.send(embed=output)

bot.run(env.DISCORD_TOKEN)