import asyncio
import json
import os
import time
from tkinter import *
from tkinter import ttk

from dotenv import load_dotenv
from loguru import logger

from ai import data_analysis
from kwork.kwork import Kwork

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

        time.sleep(5)


def run_async_function(coroutine):
    """Запуск асинхронной функции в GUI"""
    try:
        loop = asyncio.get_running_loop()  # Получаем текущий активный событийный цикл
    except RuntimeError:
        loop = asyncio.new_event_loop()  # Создаем новый цикл, если нет активного
        asyncio.set_event_loop(loop)

    if loop.is_running():
        asyncio.ensure_future(coroutine)
    else:
        loop.run_until_complete(coroutine)


async def getting_categories_gui():
    api = Kwork(login=login, password=password)
    await getting_categories(api)
    await api.close()


async def receiving_projects_in_the_selected_category_gui():
    api = Kwork(login=login, password=password)
    await receiving_projects_in_the_selected_category(api)
    await api.close()


root = Tk()  # создаем корневой объект - окно
root.title("KWORK_BOT_by_PyAdminRU")  # устанавливаем заголовок окна
root.geometry("300x250")  # устанавливаем размеры окна

# стандартная кнопка
btn = ttk.Button(text="Получение списка категорий", command=lambda: run_async_function(getting_categories_gui()))
btn.pack()

btn_1 = ttk.Button(text="Получение проектов в выбранной категории",
                   command=lambda: run_async_function(receiving_projects_in_the_selected_category_gui()))
btn_1.pack()

root.mainloop()
