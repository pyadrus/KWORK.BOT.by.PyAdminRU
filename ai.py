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
        model="llama3-groq-70b-8192-tool-use-preview",
    )

    print(chat_completion.choices[0].message.content)
