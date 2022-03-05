import discord

TOKEN = 'OTQ5Mjc2MDk0NTY0MDI4NDM2.YiIAQQ.c_l4gSYWgNvOn1lO_NvuT5Tj4cs'
client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(msg):
    if msg.author == client.user:       # avoids recursive messages
        return
    if not msg.channel.name == 'bugs':  # checks channel
        return

    await msg.create_thread(name=msg.content)

client.run(TOKEN)
