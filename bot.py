import telebot
import requests
import time

# @BotFather bergan oxirgi tokenni shu yerga qo'ying
TOKEN = '7817058089:AAGNX19qjvNZYcAFBLkjrZ9vwLavOjXRBDs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def generate_image(message):
    query = message.text
    chat_id = message.chat.id
    bot.send_message(chat_id, f"🎨 '{query}' chizilyapti, ozgina kuting...")
    
    # Rasm yaratish uchun ochiq API (Render-da bu cheklovsiz ishlaydi)
    url = f"https://pollinations.ai/p/{query.replace(' ', '%20')}?width=1024&height=1024&seed=42"
    
    try:
        # AIga rasm chizishga vaqt beramiz
        time.sleep(5) 
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            bot.send_photo(chat_id, response.content, caption=f"✅ Marhamat: {query}")
        else:
            bot.send_message(chat_id, "❌ AI hozir javob bera olmadi, qaytadan urinib ko'ring.")
    except Exception:
        bot.send_message(chat_id, "❌ Ulanishda xatolik yuz berdi.")

print("Bot Render-da ishga tushdi...")
bot.polling(none_stop=True)
