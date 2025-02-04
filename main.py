import telebot
TOKEN = ''
ID = 6725283724
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, "Hello, Send Your Message")

@bot.message_handler(func=lambda message: True)
def forward_to_me(message):
    bot.forward_message(ID, message.chat.id, message.message_id)
    text = f"ID: [Standard](tg://user?id={message.from_user.id}) [Android](tg://openmessage?user_id={message.from_user.id}) [iOS](https://t.me/@{message.from_user.id})\nUsername: @{message.from_user.username}"
    bot.send_message(ID, text=text, parse_mode='MarkdownV2')
    bot.reply_to(message, "Sent.")

bot.polling()
