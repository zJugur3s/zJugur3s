from userbot.events import register

@register(outgoing=True, pattern="^.ciao$")
async def ciao(e):
  await e.edit("**Ciaoo/nMerdaaa**")
  
