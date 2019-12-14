from userbot.events import register

@register(outgoing=True, Pattern="^.ciao$")
async def ciao(e):
  await e.edit("**Ciaoo/nMerdaaa**")
  
