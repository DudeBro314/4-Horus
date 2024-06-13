from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime # Couldn't import name now idk why tf


# NE BEITE POZHALUISTA ETO MOI PERVIY COMMERCHESKIY PROECT :(

class Fix():
    def __init__(self):
        self.progress = 0
        self.user = " "
        self.copy = []
        self.flag = False
        self.orig = [line.strip() for line in open("text.txt", encoding="utf-8")]

    def AppendLogs(self, collected_string):
        with open("logs.txt", "a") as fin:
            fin.write(collected_string)
            fin.write("\n")

    def FormatString(self, user=None, string=None):
        string = f"{user}|{str(datetime.datetime.now())}|{string}"
        self.AppendLogs(collected_string=string)

    def SmartReply(self):
        if self.progress < 4:
            self.progress += 1
            return self.copy[self.progress]
        return self.copy[0]
        

warrior = Bot("API_CENSORED")
dp = Dispatcher(warrior)

bank = Fix()

markup2 = InlineKeyboardMarkup()
tele = InlineKeyboardButton("TELEGRAM", callback_data="telega")
what = InlineKeyboardButton("WHATSAPP", callback_data="whata")
markup2.add(tele, what)

@dp.message_handler()
async def work(message: types.Message):
    if message.text == "/start":
        bank.copy, bank.progress = bank.orig, 0
        await message.answer(bank.SmartReply(), parse_mode="HTML")
        bank.FormatString(user=message.from_user.username, string=message.text)

    elif bank.copy[bank.progress][3:6] == "AT ":
        markup1 = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton("YES", callback_data="positive")
        btn2 = InlineKeyboardButton("I NEED TIME...", callback_data="negative")
        markup1.add(btn1, btn2)
        string = "<b>" + (bank.name).upper() + ", " + bank.SmartReply()
        await message.answer(string, parse_mode="HTML", reply_markup=markup1)
        bank.name = " "
        bank.FormatString(user=message.from_user.username, string=message.text)

    else:
        if bank.progress == 1:
            bank.name = message.text
        await message.answer(bank.SmartReply(), parse_mode="HTML")
        bank.FormatString(user=message.from_user.username, string=message.text)


@dp.callback_query_handler(lambda query: query.data in ['positive', 'negative', "telega", "whata", "agreed", "disagreed"])
async def process_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "positive":
        await warrior.send_message(callback_query.from_user.id, bank.SmartReply(), parse_mode="HTML", reply_markup=markup2)
    elif callback_query.data == "negative":
        await warrior.send_message(callback_query.from_user.id, "<b>WE WISH TO SEE YOU ONCE YOU ARE READY!</b>", parse_mode="HTML")
    elif callback_query.data == "telega":
        await warrior.send_message(callback_query.from_user.id, "<b>THANKS FOR YOUR INTREST AND HONESTY. JOIN OUR CHANNEL https://t.me/silentwarriorstore</b>", parse_mode="HTML")
    elif callback_query.data == "whata":
        await warrior.send_message(callback_query.from_user.id, "<b>PLEASE, ENTER YOUR PHONE NUMBER</b>", parse_mode="HTML")

    

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
