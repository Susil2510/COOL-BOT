from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    Poll,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)


api_id: int = "API_ID"
api_hash: str = "API_HASH"
bot_token: str = "BOT_TOKEN"


app = Client('viewcounterbot', in_memory=True, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

non_anonymous_poll = filters.create(
    lambda *_: _[2].poll is not None and not _[2].poll.is_anonymous
)

forwardchannel = -1000000000000
startmsg: str = """
start message
"""


@Client.on_message(filters.command("cstart") & filters.private)
async def start(client, message):
    await message.reply(
        startmsg,
    )


@Client.on_message(
    ~filters.service
    & ~filters.game
    & ~filters.channel
    & ~filters.linked_channel
    & ~non_anonymous_poll
)
async def viewcounter(client, message):
    forward = await message.forward(forwardchannel)
    await forward.forward(message.chat.id)
    await forward.delete()


@Client.on_message(
    (filters.service | filters.game | filters.channel | non_anonymous_poll)
)
async def notsupported(client, message):
    await message.reply(
        "sorry but this type of message not supported (non anonymous polls or games (like @gamebot or @gamee) or message from channels or service messages)",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("delete this message", "deleterrormessage")]]
        ),
    )


@Client.on_callback_query(filters.regex("^deleterrormessage"))
async def delerrmsg(client: app, cquery: CallbackQuery):
    await cquery.message.delete()



