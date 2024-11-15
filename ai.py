import os
from dotenv import load_dotenv
from groq import Groq


def data_analysis(project):
    """Анализ данных с помощью ИИ"""

    load_dotenv()  # Загрузка переменных окружения из .env файла

    api_key = os.getenv("GROQ_API_KEY")
    print(api_key)

    client = Groq(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Что хочет заказчик? Ответ должен содержать максимум 1 предложение: {project}",
            }
        ],
        model="llama3-groq-70b-8192-tool-use-preview",
    )

    print(chat_completion.choices[0].message.content)
