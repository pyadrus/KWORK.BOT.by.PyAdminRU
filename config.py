# -*- coding: utf-8 -*-
import configparser

# Чтение конфигурации из config.ini
config = configparser.ConfigParser()
config.read('config.ini')

login = config['kwork']['login']
password = config['kwork']['password']

GROQ_API_KEY = config['API_Groq']['GROQ_API_KEY']

proxy_user = config['proxy_data']['user']
proxy_password = config['proxy_data']['password']
proxy_port = config['proxy_data']['port']
proxy_ip = config['proxy_data']['ip']
