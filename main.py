from aiogram import Bot, Dispatcher, executor, types
import logging
from downloader import InstagramDownloader
import shutil

bot = Bot("5904607271:AAH-edy50mxak7BhgfeCB-9oLnlrK5QMPiM")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")


@dp.message_handler()
async def mainpart(message: types.Message):
    global downloaded
    await message.answer("Video yuklanmoqda...")
    if message.text.startswith("https://www.instagram.com/") or message.text.startswith("https://instagram.com/"):
        downloaded = InstagramDownloader(message.text)
        opened = open(downloaded[0], "rb").read()
        edited = str(opened).replace('\n', '').replace('\r', '')
        with open(downloaded[1][0], "rb") as video:
            try:
                await message.answer_video(video=video, caption=edited)
            except:
                try:
                    await message.answer_video(video=video)
                except Exception as e:
                    print(e)
    shutil.rmtree(downloaded[2])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
