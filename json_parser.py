import json
from loguru import logger

# Чтение содержимого файла projects.json с указанием кодировки
with open('projects.json', 'r', encoding='UTF-8') as file:
    json_data = file.read()

# Преобразуем строку JSON в список Python
data: list = json.loads(json_data)

# Проверим структуру данных
logger.info(data)

for project in data:
    if 'telegram' in project['title'].lower():
        logger.info(f'Название проекта: {project["title"]}, ссылка: {project["project_url"]}')
    if 'телеграм' in project['title'].lower():
        logger.info(f'Название проекта: {project["title"]}, ссылка: {project["project_url"]}')