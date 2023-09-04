from os import getenv
from asyncio import sleep
from pyrogram import Client, filters, idle
from pyrogram.types import Message

SESSION = getenv('SESSION')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split(" ")))

M = Client(SESSION, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")

# Dictionary to store command information
commands_info = {
    "/start": "Start the bot.",
    "/broadcast [message]": "Broadcast a message to all joined chats and users.",
    "/stats": "Display statistics about the bot's chats and users.",
    "/help": "Display a list of available commands with their usages and features."
}

@M.on_message(filters.user(SUDO_USERS) & filters.command('start'))
async def start(_, message: Message):
    await message.reply_text("🤖 **I AM STILL ALIVE...**")

@M.on_message(filters.user(SUDO_USERS) & filters.command("broadcast"))
async def broadcast_message(_, message: Message):
    try:
        text = message.text.split(" ", 1)[1]
    except IndexError:
        await message.reply_text("**Usage:**\n`/broadcast [message]`")
        return
    
    async for chat in M.iter_dialogs():
        if chat.chat.type in ['supergroup', 'group']:
            try:
                await M.send_message(chat.chat.id, text)
                await sleep(2)  # Add a sleep to avoid flooding
            except Exception as e:
                print(f"Failed to send message to {chat.chat.id}: {str(e)}")
    
    await message.reply_text("✅ **Broadcasted the message to all joined chats and users.**")

@M.on_message(filters.user(SUDO_USERS) & filters.command("stats"))
async def stats(_, message: Message):
    chat_count = 0
    user_count = 0

    async for chat in M.iter_dialogs():
        if chat.chat.type in ['supergroup', 'group']:
            chat_count += 1
        elif chat.chat.type == 'private':
            user_count += 1

    stats_text = f"**Stats:**\n\nTotal Chats: {chat_count}\nTotal Users: {user_count}"

    await message.reply_text(stats_text)

@M.on_message(filters.user(SUDO_USERS) & filters.command("help"))
async def help_command(_, message: Message):
    help_text = "**Available Commands:**\n\n"
    for command, description in commands_info.items():
        help_text += f"`{command}`: {description}\n"
    
    await message.reply_text(help_text)

M.start()
print("™°‌ 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍 𝗕𝗢𝗧 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗦𝗨𝗦𝗦𝗘𝗦𝗙𝗨𝗟𝗟𝗬")
idle()
M.stop()
