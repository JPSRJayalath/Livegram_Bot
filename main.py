import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_ID = "API ID"
API_HASH = "API HASH"
BOT_TOKEN = "BOT TOKEN"
ADMIN_USER_ID = "Admin User ID (Your Telegram ID)"

# Initialize the bot
bot = TelegramClient("livegram_bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Store a mapping of forwarded messages to their original senders
forwarded_messages = {}

# Handle /start command
@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply(
        "Welcome to the Livegram Bot! Send me a message, and I'll forward it to the admin."
    )

# Forward user messages to the admin
@bot.on(events.NewMessage)
async def forward_to_admin(event):
    if event.is_private and event.sender_id != ADMIN_USER_ID:
        # Forward the message to the admin
        forwarded_message = await bot.forward_messages(ADMIN_USER_ID, event.message)

        # Store the original sender's ID with the forwarded message ID
        forwarded_messages[forwarded_message.id] = event.sender_id

        # Notify the user
        # await event.reply("Your message has been forwarded to the admin.")

# Handle admin replies to users
@bot.on(events.NewMessage(chats=ADMIN_USER_ID))
async def reply_to_user(event):
    if event.is_reply:
        replied_message = await event.get_reply_message()
        # Get the original sender's ID from the forwarded_messages map
        original_user_id = forwarded_messages.get(replied_message.id)

        if original_user_id:
            try:
                # Send the admin's reply to the original user
                await bot.send_message(original_user_id, event.message)
                # await event.reply("Your reply has been sent to the user.")
            except Exception as e:
                await event.reply(f"Error sending the reply: {e}")
        else:
            await event.reply(
                "The message you replied to was not found in the forwarded messages map. Please ensure you reply to a forwarded message."
            )
    else:
        await event.reply(
            "To reply to a user, use the Telegram client’s reply feature by right-clicking a message and selecting 'Reply'."
        )

# Start the bot
print("Bot is running...")
bot.run_until_disconnected()