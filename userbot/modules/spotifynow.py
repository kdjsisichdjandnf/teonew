import datetime
import os
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.snow(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    chat = "@SpotifyNowBot"
    now = f"/now"
    await event.edit("```Processing...```")
    async with bot.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=901580071))
              msg = await bot.send_message(chat, now)
              respond = await response
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await event.reply("```Please unblock @SpotifyNowBot and try again```")
              return
          if respond.text.startswith("`You're`"):
              await event.edit("```You're not listening to anything on Spotify at the moment```")
              return
          else:
             await bot.forward_messages(event.chat_id, respond.message)
             await event.client.delete_messages(conv.chat_id,
                                                [msg.id, r.id, respond.id])
    await event.delete()

CMD_HELP.update({
        "spotifynow":
        "`>.snow`"
        "\nUsage: Show what you're listening on spotify."
})