import asyncio
import json
import os
import time

from dotenv import load_dotenv
from loguru import logger

from ai import data_analysis
from kwork import Kwork

load_dotenv()  # Загрузка переменных окружения из .env файла

# Получение данных для авторизации из переменных окружения
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


async def getting_categories(api):
    """Получение списка категорий
    :param api: объект класса Kwork
    """
    categories = await api.get_categories()
    for category in categories:
        logger.info(category)  # Получение категорий заказов на бирже, для дальнейшего поиска проектов по их id


async def receiving_projects_in_the_selected_category(api):
    """Получение проектов в выбранной категории
    :param api: объект класса Kwork
    """
    projects = await api.get_projects(categories_ids=[11])  # Получение проектов по указанным категориям

    with open('projects.json', 'w', encoding='utf-8') as file:  # Сохранение проектов в JSON файл
        json.dump(projects, file, indent=4, ensure_ascii=False)

    for project in projects:
        logger.info(project)
        data_analysis(project)

        #await main_module(project)

        time.sleep(5)


async def main():
    if not login or not password:  # Проверка, если логин и пароль не пустые
        logger.info("Ошибка: Логин и/или пароль не найдены в .env файле.")
        return

    api = Kwork(login=login, password=password)  # Создание экземпляра Kwork с логином и паролем

    print(
        "\n1. Получение списка категорий"
        "\n2. Получение проектов в выбранной категории")
    user_input = input("Выберите функцию: ")

    if user_input == "1":
        await getting_categories(api)
    elif user_input == "2":
        await receiving_projects_in_the_selected_category(api)
    else:
        logger.info("Ошибка: Выбранная функция не найдена.")

    await api.close()  # Закрытие соединения с API


if __name__ == "__main__":
    asyncio.run(main())  # Запуск основного асинхронного цикла
