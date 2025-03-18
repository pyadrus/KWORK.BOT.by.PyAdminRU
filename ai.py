# -*- coding: utf-8 -*-
from groq import Groq

from config import GROQ_API_KEY
from proxy_config import setup_proxy


def data_analysis(project):
    """Анализ данных с помощью ИИ"""

    setup_proxy()

    client = Groq(api_key=GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Что хочет заказчик? Ответ должен содержать максимум 1 предложение: {project}",
            }
        ],
        model="qwen-2.5-32b",
    )

    print(chat_completion.choices[0].message.content)
