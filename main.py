import asyncio
import json
import os
from dotenv import load_dotenv
from kwork import Kwork

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение данных для авторизации из переменных окружения
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

async def main():
    # Проверка, если логин и пароль не пустые
    if not login or not password:
        print("Ошибка: Логин и/или пароль не найдены в .env файле.")
        return

    # Создание экземпляра Kwork с логином и паролем
    api = Kwork(login=login, password=password)

    # Получение проектов по указанным категориям
    projects = await api.get_projects(categories_ids=[11])
    print(projects)

    # Сохранение проектов в JSON файл
    with open('projects.json', 'w', encoding='utf-8') as file:
        json.dump(projects, file, indent=4, ensure_ascii=False)

    # Закрытие соединения с API
    await api.close()

if __name__ == "__main__":
    # Запуск основного асинхронного цикла
    asyncio.run(main())
