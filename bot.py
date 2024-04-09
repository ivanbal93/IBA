import asyncio
import logging
import psycopg2

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from env_config import TOKEN, DATABASE_URL


bot = Bot(token=TOKEN)

# Подключение к БД
DATABASE_URL = DATABASE_URL

# aiogramm Диспетчер
dp = Dispatcher()

# Логгирование
logging.basicConfig(level=logging.INFO)


@dp.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    '''
    Хендлер команды "/start"
    '''
    await message.answer(
        f'Добро пожаловать в библиотеку коктейлей IBA!'
    )


@dp.message()
async def get_the_cocktail(message: types.Message) -> None:
    '''
    Получение коктейля по названию
    '''
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    try:
        cursor.execute(
            f"SELECT * FROM data_cocktail "
            f"WHERE name = '{message.text.lower().capitalize()}';"
        )
        data = cursor.fetchone()
        enter = "\n"
        result = (f'Коктейль {data[1]}{enter*2}'
                  f'Состав:{enter}{data[2]}{enter*2}'
                  f'Приготовление: {data[3]}{enter*2}'
                  f'Категория: {data[-1]}'
        )
    except:
        result = 'Коктейль с таким названием не найден.'
    cursor.close()
    conn.close()

    await message.answer(result)


async def main() -> None:
    '''
    Поллинг объектов
    '''
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
