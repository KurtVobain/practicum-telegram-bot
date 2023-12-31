import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TENNIS = (
        'У меня есть 3 главных увлечения - кино, программирование и теннис. '
        'Остановимся на последнем. '
        'Теннисом я впервые стал заниматься 4 месяца назад. '
        'Началось все с простого любопытства - хотелось просто попробовать, '
        'но уже с первого занятия меня затянуло и появилось любовь❤️. '
        'Теннис оказался спортом с большим порогом входа '
        ', но именно эта сложность и мотивирует меня заниматься. '
        'Мне нравится ощущение преодоления себя, испытания '
        'которые стоят передо мной на каждом занятии. '
        'Теннис - это не просто спорт, '
        'где нужно “лупить”, это во многом про умственную активность '
        'и координацию всего своего тела для достижения цели. '
        'Советую попробовать поиграть в теннис, если этого еще не делали🎾'
    )
    MY_CHAT_ID=325835886
