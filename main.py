import yagmail
import telegram

# Connect to Yandex email
yag = yagmail.SMTP("your_email_address@yandex.com", "your_password")

# Connect to Telegram
bot = telegram.Bot(token="your_bot_token")

# Check for new messages
unread_emails = yag.folder("inbox").unseen()

for email in unread_emails:
    sender = email.sent_from
    subject = email.subject
    body = email.body

    # Send message to Telegram chat
    bot.send_message(chat_id="your_chat_id", text=f"From: {sender}\nSubject: {subject}\n{body}")
