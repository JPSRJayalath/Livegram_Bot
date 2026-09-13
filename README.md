# 🤖 Livegram Bot

A lightweight Telegram support/contact bot built with **Python** and **Telethon** that routes private messages between users and an administrator.

## ✨ Features & Workflow
- **Two-Way Routing:** Forwards user messages to the admin and routes admin replies back to the correct user.
- **Native Replies:** Admins must use Telegram's native "Reply" feature on the forwarded message to respond properly.

## 📋 Requirements & Setup
- **Python 3.9+** and a **Telegram account**.
- Clone the repo, set up a virtual environment, and install dependencies:
  ```bash
  git clone https://github.com
  cd Livegram_Bot
  python3 -m venv .venv && source .venv/bin/activate  # Or use appropriate Windows activation
  pip install telethon python-dotenv
  ```

## ⚙️ Configuration & Credentials
Open `main.py` (lines 8–11) to configure your credentials directly:
- **API_ID & API_HASH:** Obtain from the [Telegram API Development Tools Portal](https://telegram.org).
- **BOT_TOKEN:** Create a bot via [@BotFather](https://t.me).
- **ADMIN_USER_ID:** Get your numeric ID from [@userinfobot](https://t.me).

Run the bot with `python main.py`. Full license details are available via the [MIT License](LICENSE).
