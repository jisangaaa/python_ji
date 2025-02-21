from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7625750945:AAFTUOibK4_AhYQc-z5eCZnfmpNJEKY_jeodwqst"

TRIGGER_WORDS = {
    "안녕":"안녕하세요! 저는 지상이 입니다.",
    "루다":"안녕하세요! 저는 루다 입니다.",
    "라면":"안녕하세요! 저는 너구리 입니다."
}

async def start(update,context):
    await update.message.reply_text("안녕하세요 저는 루다입니다. 무엇을 도와드릴까요?")
async def monitor_chat(update,context):
    user_text = update.message.text #감지된 메세지들
    chat_id = update.message.chat_id #메세지가 온 채팅방

    for key, res in TRIGGER_WORDS.items():
        if key in user_text:
            await context.bot.send_message(chat_id=chat_id, text=res)
            break    #한개의 키워드에만 반응
 
    
def main():
    app=Application.builder().token(TOKEN).build()
    #명령어 #핸들러 추가
    app.add_handler(CommandHandler("start",start))
    #응답 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))
    
    print("텔레그램 봇이 실행중입니다")
    app.run_polling()

if __name__ == "__main__":
    main()