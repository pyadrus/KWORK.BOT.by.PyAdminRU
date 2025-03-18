# -*- coding: utf-8 -*-
from g4f.client import Client


async def main_module(project):
    client = Client()
    response = client.chat.completions.create(
        model="claude-3-haiku",
        messages=[{"role": "user",
                   "content": f"Что хочет заказчик? Ответ должен содержать максимум 1 предложение: {project}"}],
        # Add any other necessary parameters
    )

    print(response.choices[0].message.content)
