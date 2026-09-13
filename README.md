🤖 Livegram Bot

A simple Telegram support/contact bot built with Python + Telethon.

Users can send private messages to the bot, and the bot automatically forwards those messages to the administrator. The administrator can then reply directly to the forwarded message, and the bot sends the reply back to the original user.

✨ Features

* 💬 Receive private messages from Telegram users
* 📩 Automatically forward user messages to an admin
* ↩️ Admin can reply to forwarded messages
* 🔄 Automatically send admin replies back to the original user
* 🔐 Credentials stored using environment variables
* 🐍 Built with Python and Telethon
* ⚡ Lightweight and simple

⸻

📋 Requirements

Before running the bot, you need:

* Python 3.9 or newer
* A Telegram account
* Telegram API_ID
* Telegram API_HASH
* Telegram BOT_TOKEN
* Your Telegram ADMIN_USER_ID

⸻

🚀 Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY

Or download the project as a ZIP and extract it.

⸻

2. Create a virtual environment

Linux / macOS

python3 -m venv .venv
source .venv/bin/activate

Windows

python -m venv .venv
.venv\Scripts\activate

⸻

3. Install dependencies

pip install telethon python-dotenv

If the project contains a requirements.txt file, you can instead use:

pip install -r requirements.txt

⸻

🔑 Telegram API Credentials

This bot uses the Telegram API through Telethon.

You need:

API_ID
API_HASH
BOT_TOKEN
ADMIN_USER_ID

The first two come from Telegram’s API development tools, while the bot token comes from @BotFather.

⸻

🆔 Getting API ID and API Hash

Step 1 — Open Telegram’s API website

Go to:

Telegram API Development Tools

⸻

Step 2 — Log in

Log in using the phone number associated with your Telegram account.

Telegram will send you a login/verification code.

⸻

Step 3 — Open “API development tools”

After logging in, select:

API development tools

⸻

Step 4 — Create an application

Fill in the application form.

For example:

App title: Livegram Bot
Short name: livegrambot
Platform: Desktop
Description: Telegram support bot

The exact application name does not matter much.

⸻

Step 5 — Copy your credentials

Telegram will provide:

api_id
api_hash

For example:

api_id: 12345678
api_hash: abcdef1234567890abcdef1234567890

Do not use the example values.

Use the values provided by Telegram.

📚 Official documentation:

Telegram — Obtaining an API ID

⸻

🤖 Getting the Bot Token

Your bot token is created using Telegram’s official @BotFather.

Step 1 — Open BotFather

Open Telegram and search for:

@BotFather

Make sure you select the official BotFather account.

⸻

Step 2 — Start BotFather

Send:

/start

⸻

Step 3 — Create your bot

Send:

/newbot

BotFather will ask you for a name.

Example:

Livegram Support Bot

⸻

Step 4 — Choose a username

BotFather will ask for a username.

For example:

my_livegram_support_bot

The username must follow Telegram’s bot username rules and normally ends with bot.

⸻

Step 5 — Copy your bot token

BotFather will provide a token similar to:

123456789:AAExampleToken

This is your:

BOT_TOKEN

⚠️ Treat your bot token like a password.

Anyone who gets your bot token may be able to control your bot.

📚 Official documentation:

Telegram Bot API Tutorial

⸻

👤 Getting Your Telegram User ID

The bot needs your Telegram numeric user ID so it knows who the administrator is.

Your ID looks something like:

123456789

You can use a Telegram ID bot such as @userinfobot to find your numeric Telegram user ID.

Send:

/start

It will show your user information, including your numeric ID.

Copy the number and use it as:

ADMIN_USER_ID

Your Telegram username, such as @username, is not the same thing as your numeric user ID.

⸻

⚙️ Configure the Bot

Create a file named:

.env

in the project’s root directory.

Your project should look like:

livegram-bot/
│
├── .env
├── .gitignore
├── requirements.txt
├── main.py
└── README.md

Put your credentials inside .env:

API_ID=12345678
API_HASH=your_api_hash_here
BOT_TOKEN=123456789:your_bot_token_here
ADMIN_USER_ID=123456789

Replace all example values with your actual credentials.

⸻

🔒 Protect Your Credentials

Never upload your .env file to GitHub.

Create a .gitignore file:

.env
.venv/
__pycache__/
*.session

The *.session rule is also important because Telethon can create session files containing authentication information.

Your GitHub repository should not contain:

.env
livegram_bot.session

⸻

🛠️ Update the Python Code

Your credentials should be loaded from .env.

Use:

import os
from telethon import TelegramClient, events
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID"))
# Initialize the bot
bot = TelegramClient(
    "livegram_bot",
    API_ID,
    API_HASH
).start(bot_token=BOT_TOKEN)

Then keep the rest of your bot logic below this section.

Why this is better

Instead of storing:

BOT_TOKEN = "123456789:ABC..."

inside your Python code, the token stays inside:

.env

This makes it much safer to publish your source code on GitHub.

⸻

▶️ Run the Bot

Activate your virtual environment first.

Linux / macOS

source .venv/bin/activate

Then run:

python main.py

Windows

.venv\Scripts\activate
python main.py

If everything is configured correctly, you should see:

Bot is running...

Keep the terminal running while you want the bot online.

⸻

💬 How the Bot Works

The message flow is:

             User
               │
               │ Sends message
               ▼
        ┌──────────────┐
        │ Telegram Bot │
        └──────┬───────┘
               │
               │ Forward
               ▼
            Admin
               │
               │ Reply to forwarded message
               ▼
        ┌──────────────┐
        │ Telegram Bot │
        └──────┬───────┘
               │
               │ Send reply
               ▼
             User

Example

A user sends:

Hello, I need help.

The bot forwards it to the administrator.

The administrator uses Telegram’s Reply function:

↩️ Hello, I need help.
     └── How can I help you?

The bot detects that reply and sends:

How can I help you?

back to the original user.

⸻

⚠️ Important: Reply to the Forwarded Message

The administrator must use Telegram’s Reply feature when responding.

For example:

User message
     ↓
Forwarded to Admin
     ↓
Admin clicks Reply
     ↓
Admin writes response
     ↓
Bot sends response to User

If the admin sends a normal unrelated message, the bot cannot determine which user should receive it.

⸻

🧪 Testing

After starting the bot:

1. Open your bot in Telegram.
2. Press Start.
3. Send a message.
4. Check your administrator account.
5. The message should appear forwarded to you.
6. Reply to that forwarded message.
7. The user should receive your reply.

Recommended test

Use a different Telegram account to test the user side.

⸻

🐛 Troubleshooting

ModuleNotFoundError

If you see:

ModuleNotFoundError: No module named 'telethon'

Install Telethon:

pip install telethon

For dotenv:

pip install python-dotenv

⸻

API_ID or API_HASH error

Check your .env file:

API_ID=12345678
API_HASH=your_api_hash

Make sure there are no unnecessary quotation marks or spaces.

⸻

Bot token error

Check:

BOT_TOKEN=your_bot_token

If you accidentally exposed your bot token publicly, generate a new token through @BotFather.

⸻

Admin does not receive messages

Check:

ADMIN_USER_ID=123456789

Make sure this is your numeric Telegram user ID, not your username.

⸻

Admin reply doesn’t reach the user

Make sure you are replying directly to the forwarded message.

The bot uses the forwarded message ID to identify the original sender.

⸻

🔐 Security Checklist

Before pushing this project to GitHub:

* .env is in .gitignore
* Bot token is not inside Python source code
* API hash is not inside Python source code
* *.session is in .gitignore
* No credentials are visible in screenshots
* No credentials are committed to Git

If credentials were accidentally committed to a public repository, changing/removing the code is not enough. Rotate the exposed credentials.

⸻

📦 Dependencies

The project uses:

Telethon
python-dotenv

Install them with:

pip install telethon python-dotenv

Or create requirements.txt:

telethon
python-dotenv

Then:

pip install -r requirements.txt

⸻

📄 License

Choose a license for your project depending on how you want others to use, modify, and distribute the code.

⸻

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
