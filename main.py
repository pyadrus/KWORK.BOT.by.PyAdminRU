# -*- coding: utf-8 -*-
import asyncio
import json
import time

from loguru import logger

from ai import data_analysis
from config import login, password
from kwork.kwork import Kwork


async def getting_categories(api):
    """Получение списка категорий
    :param api: объект класса Kwork
    """
    categories = await api.get_categories()
    for category in categories:
        logger.info(category)  # Получение категорий заказов на бирже, для дальнейшего поиска проектов по их id


async def receiving_projects_in_the_selected_category_gui():
    """Получение проектов в выбранной категории"""
    api = Kwork(login=login, password=password)
    await receiving_projects_in_the_selected_category(api)
    await api.close()


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


async def main():
    """Главное меню программы"""
    print("Главное меню программы\n",
          "1. Получение списка категорий\n",
          "2. Получение проектов в выбранной категории\n")

    input_data = input("Введите номер пункта меню: ")
    if input_data == "1":
        api = Kwork(login=login, password=password)
        await getting_categories(api)
        await api.close()
    elif input_data == "2":
        await receiving_projects_in_the_selected_category_gui()
    else:
        print("Неверный пункт меню")


if __name__ == '__main__':
    asyncio.run(main())
