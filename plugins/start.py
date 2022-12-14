from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from helper.txt import mr
from helper.database import insert 
from helper.utils import not_subscribed 

START_PIC = environ.get("START_PIC", "https://i.ibb.co/0C292SX/8de305e8631dbd22facbd0a14622490f.jpg")

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="š¢š¹ššš š¼š¢ šššššš š²ššššššš¢", url=client.invitelink) ]]
    text = "**šš¾ššš š³šš³š“ šš¾šš š½š¾š š¹š¾šøš½š³ š¼š š²š·š°š½š½š“š» š. šæš»š“š°šš“ š¹š¾šøš½ š¼š š²š·š°š½š½š“š» šš¾ ššš“ šš·šøš š±š¾š š**\n\ā¹ļø šš»š š¢ššµš²šæ šš²š¹š½ šš¼š»šš®š°š :- <a href=https://t.me/BotCreator99>@BotCreator99</a>"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""š šš¶š¶ {message.from_user.mention} \nš'šŗ š š¦š¶šŗš½š¹š² šš¶š¹š² š„š²š»š®šŗš²+šš¶š¹š¹š² š§š¼ š©š¶š±š²š¼ šš¼šš²šæšš²šæ šš¼š šŖš¶ššµ š£š²šæšŗš®š»š²š»š š§šµššŗšÆš»š®š¶š¹ & ššššš¼šŗ šš®š½šš¶š¼š» š¦šš½š½š¼šæš!\nā¹ļø šš²š¹š½ šš¼š»šš®š°š :- <a href=https://t.me/BotCreator99>@BotCreator99</a> """,
       reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton('š¢ ššæš³š°šš“š', url='https://t.me/BotMinister'),
                InlineKeyboardButton('ā¹ļø š·š“š»šæ', callback_data='help')
                 ]]
                )
            )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`""",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("š šš“š½š°š¼š“ š½š¾š š",callback_data = "rename")],
        [InlineKeyboardButton("āļø š²š°š½š²š“š» āļø",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""š Hai {query.from_user.mention} \n I am a super renamer bot! š""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton('ā¤ļø ššæš³š°šš“š', url='https://t.me/BotMinister'),
                InlineKeyboardButton('ā¹ļø š·š“š»šæ', callback_data='help')
                 ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("š¤š¤ š·š¾š šš¾ ššš“  š¤š¤", url='https://t.me/BotMinister')
               ],[
               InlineKeyboardButton("š š²š»š¾šš“", callback_data = "close"),
               InlineKeyboardButton("āļø š±š°š²šŗ", callback_data = "start")
               ]]
            )
        )
    
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





