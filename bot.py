import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready() :
    print ('BOT ONLINE - OLÁ MUNDO!')
    print (client.user.name)
    print (client.user.id)
    print ('-----PZ-------')


@client.event
async def on_message(message):
  if message.content.lower().startswith('!comandos'):
        await client.send_message(message.channel,'Comandos da radio =  ;;play    ;;list	;;nowplaying	;;skip  	;;stop  	;;pause 	;;unpause	;;repeat	;;shuffle	;;fwd time	;;rew time	;;seek time	;;split	Takes' )

client.run ('Mzc2NTUyMDE0ODc3ODE4ODgw.DOAC_g.G5gWepLepqOP9jpydL4i5Nm6Ei0')
