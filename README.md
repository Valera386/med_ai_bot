Здравствуйте, на проект “Исследование массива медицинских данных для создания предсказательного сервиса” состоит из двух частей:
1) Telegram-bot в качестве оболочки и интерфейса.
2) Нейронная сеть, которая в будущем будет обрабатывать запросы пользователей.
Ну и 3-ий со * - это база данных вместе с админ-панелью написанная на фреймворке Django.

Основные библиотеки, которые мы используем:
python-telegram-bot
Django
Keras
TesorFlow

Основная часть проекта находится в дериктории med_ai_bot/ в ней находятся еще 3 директории: 
med_ai_bot/AI 
med_ai_bot/database 
med_ai_bot/interface

Также в ней находятся директория  
(med_ai_bot/tests, med_ai_bot/Задание второго этапа Сириус.ИИ) Они не входят в ядро проекта.

В директории med_ai_bot/AI  будет находиться наша будущая Нейронная сеть.
В директории med_ai_bot/database у нас будут храниться базы данных и скрипты, которые выстраивают логику их заполнения.
В директории med_ai_bot/interface будет находиться на Telegram-bot, а именно его  кнопки и текста для сообщений.

Основной файл который будет связывать все остальные располагается в med_ai_bot/main.py 

Второй этапа Сириус.ИИ:
Задание находиться в директории med_bot_ai/Jupyter.py Мы в основном рассматривали столбец Жалобы.
В med_ai_bot/Задание второго этапа Сириус.ИИ находиться результат работы скрипта.
Файл CSV находится в med_ai_bot/database/med.csv

Для запуска на вашем ПК файла Jupyter.py требуется изменить путь к локальному расположению файла CSV и локальный путь создания новых файлов.
