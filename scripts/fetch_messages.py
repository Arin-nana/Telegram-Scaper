from datetime import datetime, timedelta
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from entities.telegram_message import TelegramMessage

API_ID = 0 
API_HASH = 'e'  

def fetch_messages(n_hours: int, channel: str, session_string: str):
    client = TelegramClient(StringSession(session_string), API_ID, API_HASH)
    client.start()  

    now = datetime.utcnow()
    since_time = now - timedelta(hours=n_hours)

    messages = []

    async def main():
        async for message in client.iter_messages(channel, offset_date=since_time):
            if message.message: 
                messages.append(TelegramMessage(
                    text=message.message,
                    datetime=message.date,
                    link=message.link_preview.url if message.link_preview else ''
                ))

    with client:
        client.loop.run_until_complete(main())

    return messages
